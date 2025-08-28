from typing import Dict, Any
import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup

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
        return {
            "echo": prompt,
            "agent": "default",
            "timestamp": datetime.now().isoformat()
        }
    
    def run_leadgen(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Lead generation agent"""
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
            "timestamp": datetime.now().isoformat()
        }
    
    def run_research(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Market research agent"""
        topic = params.get('topic') or prompt
        return {
            "summary": f"Desk research on: {topic}",
            "agent": "research",
            "topic": topic,
            "timestamp": datetime.now().isoformat()
        }
    
    def run_scrape(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Web scraping agent with BeautifulSoup"""
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
            
            return {
                "url": url,
                "title": title,
                "description": description,
                "extract": text,
                "agent": "scrape",
                "status": "success",
                "content_length": len(response.text)
            }
        except Exception as e:
            return {
                "url": url,
                "error": str(e),
                "agent": "scrape",
                "status": "failed"
            }
    
    def run_enrich(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Data enrichment agent with Hurghada-specific scoring"""
        payload = params.get("payload") or {}
        score = 0
        
        # Extract text for analysis
        text = (payload.get("bio") or payload.get("extract") or prompt or "").lower()
        
        # Hurghada-specific scoring logic
        if "photography" in text or "videography" in text:
            score += 40
        if "hurghada" in text:
            score += 30
        if "booking" in text or "inquiry" in text:
            score += 20
        if "contact" in text or "email" in text:
            score += 10
        
        return {
            "score": min(score, 100),
            "agent": "enrich",
            "text_analyzed": text[:200],
            "factors": {
                "photography_videography": "photography" in text or "videography" in text,
                "hurghada_mention": "hurghada" in text,
                "booking_inquiry": "booking" in text or "inquiry" in text,
                "contact_email": "contact" in text or "email" in text
            }
        }
    
    def run_accounting(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Accounting transaction agent"""
        tx = params.get("tx") or {
            "type": "expense",
            "account": "ops",
            "amount": 0
        }
        return {
            "transaction": tx,
            "agent": "accounting",
            "timestamp": datetime.now().isoformat()
        }
    
    def run_marketing(self, prompt: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Marketing campaign agent"""
        camp = {
            "name": params.get("name", "Auto Campaign"),
            "platform": params.get("platform", "meta"),
            "objective": params.get("objective", "LINK_CLICKS")
        }
        return {
            "campaign": camp,
            "agent": "marketing",
            "timestamp": datetime.now().isoformat()
        }
