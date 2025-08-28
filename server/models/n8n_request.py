from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class N8NWebhookRequest:
    """Model for N8N webhook requests"""
    webhook_url: str
    method: str = "POST"
    headers: Optional[Dict[str, str]] = None
    body: Optional[Dict[str, Any]] = None

@dataclass
class N8NWorkflowRequest:
    """Model for N8N workflow execution requests"""
    workflow_id: str
    base_url: Optional[str] = None
    api_key: Optional[str] = None
    payload: Optional[Dict[str, Any]] = None

@dataclass
class N8NResponse:
    """Model for N8N API responses"""
    status_code: int
    body: Any
    success: bool
