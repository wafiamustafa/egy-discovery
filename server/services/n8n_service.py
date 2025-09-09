import requests
from typing import Dict, Any
from models.n8n_request import N8NWebhookRequest, N8NWorkflowRequest, N8NResponse
from config.settings import Config

class N8NService:
    """Service for executing N8N workflows and webhooks"""
    
    def __init__(self):
        self.base_url = Config.N8N_BASE_URL
        self.api_key = Config.N8N_API_KEY
        self.timeout = Config.N8N_TIMEOUT_SECONDS
        self.webhook_url = Config.N8N_WEBHOOK_URL
    
    def execute_webhook(self, request: N8NWebhookRequest) -> N8NResponse:
        """Execute a webhook request to N8N"""
        if not Config.ENABLE_N8N_WORKFLOWS:
            return N8NResponse(
                success=False,
                status_code=0,
                body={"error": "N8N workflows are disabled"}
            )
        
        try:
            response = requests.request(
                method=request.method,
                url=request.webhook_url or self.webhook_url,
                headers=request.headers or {},
                json=request.body or {},
                timeout=self.timeout
            )
            
            return N8NResponse(
                success=response.status_code < 400,
                status_code=response.status_code,
                body=response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text
            )
            
        except requests.exceptions.RequestException as e:
            return N8NResponse(
                success=False,
                status_code=0,
                body={"error": str(e)}
            )
    
    def execute_workflow(self, request: N8NWorkflowRequest) -> N8NResponse:
        """Execute a workflow via N8N REST API"""
        if not Config.ENABLE_N8N_WORKFLOWS:
            return N8NResponse(
                success=False,
                status_code=0,
                body={"error": "N8N workflows are disabled"}
            )
        
        if not self.api_key:
            return N8NResponse(
                success=False,
                status_code=0,
                body={"error": "N8N API key not configured"}
            )
        
        try:
            # Build the API URL
            base_url = request.base_url or self.base_url
            api_url = f"{base_url}/api/v1/workflows/{request.workflow_id}/execute"
            
            headers = {
                "Content-Type": "application/json"
            }
            
            # Use request API key if provided, otherwise use config
            api_key = request.api_key or self.api_key
            if api_key:
                headers["X-N8N-API-Key"] = api_key
            
            response = requests.post(
                url=api_url,
                headers=headers,
                json=request.payload or {},
                timeout=self.timeout
            )
            
            return N8NResponse(
                success=response.status_code < 400,
                status_code=response.status_code,
                body=response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text
            )
            
        except requests.exceptions.RequestException as e:
            return N8NResponse(
                success=False,
                status_code=0,
                body={"error": str(e)}
            )
    
    def get_workflow_status(self, workflow_id: str) -> N8NResponse:
        """Get the status of a specific workflow"""
        if not Config.ENABLE_N8N_WORKFLOWS:
            return N8NResponse(
                success=False,
                status_code=0,
                body={"error": "N8N workflows are disabled"}
            )
        
        if not self.api_key:
            return N8NResponse(
                success=False,
                status_code=0,
                body={"error": "N8N API key not configured"}
            )
        
        try:
            api_url = f"{self.base_url}/api/v1/workflows/{workflow_id}"
            
            headers = {
                "X-N8N-API-Key": self.api_key
            }
            
            response = requests.get(
                url=api_url,
                headers=headers,
                timeout=self.timeout
            )
            
            return N8NResponse(
                success=response.status_code < 400,
                status_code=response.status_code,
                body=response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text
            )
            
        except requests.exceptions.RequestException as e:
            return N8NResponse(
                success=False,
                status_code=0,
                body={"error": str(e)}
            )
