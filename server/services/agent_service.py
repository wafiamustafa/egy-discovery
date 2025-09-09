from typing import Dict, Any
import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup
from config.settings import Config

class AgentService:
    """Intelligent agent routing service for business operations"""
    
    def __init__(self):
        self.agents = {
            'leadgen': self.run_leadgen,
            'research': self.run_research,
            'scrape': self.run_scrape,
            'enrich': self.run_enrich,
            'accounting': self.run_accounting,
            'marketing': self.run_marketing
        }
        self.openai_available = bool(Config.OPENAI_API_KEY and Config.ENABLE_AI_AGENTS)
    
    def smart_route(self, prompt: str, params: Dict[str, Any] = None) -> str:
        """Intelligently route requests to appropriate agents"""
        params = params or {}
        
        # Check if agent is explicitly specified
        if 'agent' in params and params['agent']:
            return params['agent']
        
        # Route based on prompt content
        low = prompt.lower()
        if any(k in low for k in ['lead', 'buyer', 'prospect']):
            return 'leadgen'
        if any(k in low for k in ['research', 'scan', 'find', 'market']):
            return 'research'
        if any(k in low for k in ['scrape', 'url', 'http']):
            return 'scrape'
        if any(k in low for k in ['enrich', 'score']):
            return 'enrich'
        if any(k in low for k in ['account', 'invoice', 'transaction']):
            return 'accounting'
        if any(k in low for k in ['campaign', 'ads', 'meta', 'google ads']):
            return 'marketing'
        
        return 'default'
    
    def run(self, prompt: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Run the appropriate agent based on smart routing"""
        params = params or {}
        agent = self.smart_route(prompt, params)
        
        if agent in self.agents:
            return self.agents[agent](prompt, params)
        else:
            return self.run_default(prompt, params)
    
    def run_default(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Default agent for unrecognized requests"""
        if self.openai_available:
            return self._enhance_with_openai(prompt, params)
        
        return {
            "echo": prompt,
            "agent": "default",
            "timestamp": datetime.now().isoformat(),
            "note": "OpenAI integration not available"
        }
    
    def _enhance_with_openai(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance response using OpenAI API"""
        try:
            headers = {
                "Authorization": f"Bearer {Config.OPENAI_API_KEY}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": Config.OPENAI_MODEL,
                "messages": [
                    {"role": "system", "content": "You are a business intelligence assistant. Provide concise, actionable insights."},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": Config.OPENAI_MAX_TOKENS,
                "temperature": Config.OPENAI_TEMPERATURE
            }
            
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                ai_response = result['choices'][0]['message']['content']
                
                return {
                    "echo": prompt,
                    "agent": "default",
                    "ai_enhanced": True,
                    "response": ai_response,
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "echo": prompt,
                    "agent": "default",
                    "ai_enhanced": False,
                    "error": f"OpenAI API error: {response.status_code}",
                    "timestamp": datetime.now().isoformat()
                }
                
        except Exception as e:
            return {
                "echo": prompt,
                "agent": "default",
                "ai_enhanced": False,
                "error": f"OpenAI integration error: {str(e)}",
                "timestamp": datetime.now().isoformat()
            }
    
    def run_leadgen(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Lead generation agent"""
        if self.openai_available:
            return self._enhance_leadgen_with_openai(prompt, params)
        
        return {
            "items": [
                {
                    "name": "Example Lead",
                    "platform": "instagram",
                    "score": 0.8,
                    "source": prompt
                }
            ],
            "agent": "leadgen",
            "timestamp": datetime.now().isoformat(),
            "note": "OpenAI integration not available"
        }
    
    def _enhance_leadgen_with_openai(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance lead generation with OpenAI insights"""
        try:
            headers = {
                "Authorization": f"Bearer {Config.OPENAI_API_KEY}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": Config.OPENAI_MODEL,
                "messages": [
                    {"role": "system", "content": "You are a lead generation expert. Analyze the request and provide strategic insights for finding potential leads."},
                    {"role": "user", "content": f"Help me generate leads for: {prompt}"}
                ],
                "max_tokens": Config.OPENAI_MAX_TOKENS,
                "temperature": Config.OPENAI_TEMPERATURE
            }
            
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                ai_insights = result['choices'][0]['message']['content']
                
                return {
                    "items": [
                        {
                            "name": "AI-Enhanced Lead Strategy",
                            "platform": "multi-platform",
                            "score": 0.9,
                            "source": prompt,
                            "ai_insights": ai_insights
                        }
                    ],
                    "agent": "leadgen",
                    "ai_enhanced": True,
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return self.run_leadgen(prompt, params)  # Fallback to basic version
                
        except Exception as e:
            return self.run_leadgen(prompt, params)  # Fallback to basic version
    
    def run_research(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Market research agent"""
        topic = params.get('topic') or prompt
        
        if self.openai_available:
            return self._enhance_research_with_openai(topic, params)
        
        return {
            "summary": f"Desk research on: {topic}",
            "agent": "research",
            "topic": topic,
            "timestamp": datetime.now().isoformat(),
            "note": "OpenAI integration not available"
        }
    
    def _enhance_research_with_openai(self, topic: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance research with OpenAI analysis"""
        try:
            headers = {
                "Authorization": f"Bearer {Config.OPENAI_API_KEY}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": Config.OPENAI_MODEL,
                "messages": [
                    {"role": "system", "content": "You are a market research expert. Provide comprehensive analysis and insights on the given topic."},
                    {"role": "user", "content": f"Research and analyze: {topic}"}
                ],
                "max_tokens": Config.OPENAI_MAX_TOKENS,
                "temperature": Config.OPENAI_TEMPERATURE
            }
            
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                ai_analysis = result['choices'][0]['message']['content']
                
                return {
                    "summary": f"AI-enhanced research on: {topic}",
                    "agent": "research",
                    "topic": topic,
                    "ai_analysis": ai_analysis,
                    "ai_enhanced": True,
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return self.run_research(topic, params)  # Fallback to basic version
                
        except Exception as e:
            return self.run_research(topic, params)  # Fallback to basic version
    
    def run_scrape(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Web scraping agent with BeautifulSoup"""
        if not Config.ENABLE_WEB_SCRAPING:
            return {
                "error": "Web scraping is disabled",
                "agent": "scrape",
                "prompt": prompt
            }
        
        url = params.get("url") or (re.search(r'https?://\S+', prompt).group(0) if re.search(r'https?://\S+', prompt) else None)
        
        if not url:
            return {
                "error": "No URL detected",
                "agent": "scrape",
                "prompt": prompt
            }
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # Use BeautifulSoup for better content extraction
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract title
            title = soup.title.string if soup.title else ""

            # Extract meaningful text content
            text_elements = soup.find_all(['p', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            text = " ".join([elem.get_text(' ', strip=True) for elem in text_elements if elem.get_text(strip=True)])[:2000]

            # Extract meta description if available
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            description = meta_desc.get('content', '') if meta_desc else ""

            result = {
                "url": url,
                "title": title,
                "description": description,
                "extract": text,
                "agent": "scrape",
                "status": "success",
                "content_length": len(response.text)
            }
            
            # Enhance with OpenAI if available
            if self.openai_available:
                result.update(self._enhance_scraping_with_openai(text, params))
            
            return result
            
        except Exception as e:
            return {
                "error": f"Scraping failed: {str(e)}",
                "agent": "scrape",
                "prompt": prompt,
                "url": url
            }
    
    def _enhance_scraping_with_openai(self, content: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance scraped content with OpenAI analysis"""
        try:
            headers = {
                "Authorization": f"Bearer {Config.OPENAI_API_KEY}",
                "Content-Type": "application/json"
            }
            
            # Truncate content to fit within token limits
            truncated_content = content[:1500]  # Leave room for prompt and response
            
            data = {
                "model": Config.OPENAI_MODEL,
                "messages": [
                    {"role": "system", "content": "You are a content analyst. Provide key insights and summary of the given content."},
                    {"role": "user", "content": f"Analyze this content and provide key insights: {truncated_content}"}
                ],
                "max_tokens": min(Config.OPENAI_MAX_TOKENS, 500),  # Shorter response for content analysis
                "temperature": Config.OPENAI_TEMPERATURE
            }
            
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                ai_insights = result['choices'][0]['message']['content']
                
                return {
                    "ai_enhanced": True,
                    "ai_insights": ai_insights
                }
            else:
                return {"ai_enhanced": False}
                
        except Exception as e:
            return {"ai_enhanced": False}
    
    def run_enrich(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Data enrichment agent"""
        if self.openai_available:
            return self._enhance_enrichment_with_openai(prompt, params)
        
        return {
            "enriched_data": {
                "original": prompt,
                "score": 0.7,
                "confidence": "medium"
            },
            "agent": "enrich",
            "timestamp": datetime.now().isoformat(),
            "note": "OpenAI integration not available"
        }
    
    def _enhance_enrichment_with_openai(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Enhance data enrichment with OpenAI"""
        try:
            headers = {
                "Authorization": f"Bearer {Config.OPENAI_API_KEY}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": Config.OPENAI_MODEL,
                "messages": [
                    {"role": "system", "content": "You are a data enrichment specialist. Enhance and score the given data with insights."},
                    {"role": "user", "content": f"Enrich this data: {prompt}"}
                ],
                "max_tokens": Config.OPENAI_MAX_TOKENS,
                "temperature": Config.OPENAI_TEMPERATURE
            }
            
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                ai_enrichment = result['choices'][0]['message']['content']
                
                return {
                    "enriched_data": {
                        "original": prompt,
                        "ai_enhanced": ai_enrichment,
                        "score": 0.9,
                        "confidence": "high"
                    },
                    "agent": "enrich",
                    "ai_enhanced": True,
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return self.run_enrich(prompt, params)  # Fallback to basic version
                
        except Exception as e:
            return self.run_enrich(prompt, params)  # Fallback to basic version
    
    def run_accounting(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Accounting agent"""
        return {
            "transaction_type": "analysis",
            "amount": 0,
            "description": prompt,
            "agent": "accounting",
            "timestamp": datetime.now().isoformat()
        }
    
    def run_marketing(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Marketing agent"""
        return {
            "campaign_type": "analysis",
            "budget": 0,
            "description": prompt,
            "agent": "marketing",
            "timestamp": datetime.now().isoformat()
        }
