from datetime import datetime
from typing import Dict, Any

class AccountingTransaction:
    """Simple transaction model for in-memory storage"""
    
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.date = kwargs.get('date')
        self.type = kwargs.get('type')
        self.account = kwargs.get('account')
        self.counterparty = kwargs.get('counterparty')
        self.currency = kwargs.get('currency', 'USD')
        self.amount = kwargs.get('amount')
        self.category = kwargs.get('category')
        self.description = kwargs.get('description')
        self.meta = kwargs.get('meta', {})
        self.created_at = kwargs.get('created_at', datetime.now().isoformat())

class AdCampaign:
    """Simple ad campaign model for in-memory storage"""
    
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.platform = kwargs.get('platform')
        self.external_id = kwargs.get('external_id')
        self.name = kwargs.get('name')
        self.objective = kwargs.get('objective')
        self.status = kwargs.get('status', 'draft')
        self.budget_daily = kwargs.get('budget_daily', 0)
        self.start_date = kwargs.get('start_date')
        self.end_date = kwargs.get('end_date')
        self.targeting = kwargs.get('targeting', {})
        self.created_at = kwargs.get('created_at', datetime.now().isoformat())

class AdMetric:
    """Simple ad metric model for in-memory storage"""
    
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.campaign_id = kwargs.get('campaign_id')
        self.date = kwargs.get('date')
        self.impressions = kwargs.get('impressions', 0)
        self.clicks = kwargs.get('clicks', 0)
        self.spend = kwargs.get('spend', 0)
        self.conversions = kwargs.get('conversions', 0)
        self.revenue = kwargs.get('revenue', 0)
        self.metrics = kwargs.get('metrics', {})
        self.created_at = kwargs.get('created_at', datetime.now().isoformat())

class MarketInsight:
    """Simple market insight model for in-memory storage"""
    
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.topic = kwargs.get('topic')
        self.summary = kwargs.get('summary')
        self.score = kwargs.get('score', 0)
        self.data = kwargs.get('data', {})
        self.created_at = kwargs.get('created_at', datetime.now().isoformat())

class PlanSuggestion:
    """Simple plan suggestion model for in-memory storage"""
    
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.title = kwargs.get('title')
        self.body = kwargs.get('body')
        self.tags = kwargs.get('tags')
        self.created_at = kwargs.get('created_at', datetime.now().isoformat())
