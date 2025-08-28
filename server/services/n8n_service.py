import requests
from typing import Dict, Any
from models.n8n_request import N8NWebhookRequest, N8NWorkflowRequest, N8NResponse

class N8NService:
    """Service for executing N8N workflows and webhooks"""
    
    def __init__(self):
        self.timeout = 30  # Default timeout in seconds
    
    def execute_webhook(self, request: N8NWebhookRequest) -> N8NResponse:
        """Execute a webhook request to N8N"""
        try:
            response = requests.request(
                method=request.method,
                url=request.webhook_url,
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
        try:
            # Build the API URL
            api_url = f"{request.base_url}/api/v1/workflows/{request.workflow_id}/execute"
            
            headers = {
                "Content-Type": "application/json"
            }
            
            if request.api_key:
                headers["X-N8N-API-Key"] = request.api_key
            
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
