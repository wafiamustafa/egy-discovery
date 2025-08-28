from dataclasses import dataclass
from typing import Optional, Any, Dict
from datetime import date

@dataclass
class CampaignIn:
    platform: str
    name: str
    objective: Optional[str] = None
    status: Optional[str] = "draft"
    budget_daily: Optional[float] = 0
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    targeting: Dict[str, Any] = None
    external_id: Optional[str] = None

@dataclass
class CampaignOut(CampaignIn):
    id: int
    
    def __post_init__(self):
        if self.targeting is None:
            self.targeting = {}

@dataclass
class MetricIn:
    campaign_id: Optional[int] = None
    date: date
    impressions: Optional[int] = 0
    clicks: Optional[int] = 0
    spend: Optional[float] = 0
    conversions: Optional[int] = 0
    revenue: Optional[float] = 0
    metrics: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metrics is None:
            self.metrics = {}

@dataclass
class MetricOut(MetricIn):
    id: int

@dataclass
class TxIn:
    date: date
    type: str
    account: str
    counterparty: Optional[str] = None
    currency: str = "USD"
    amount: float
    category: str
    description: Optional[str] = None
    meta: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.meta is None:
            self.meta = {}

@dataclass
class TxOut(TxIn):
    id: int
    created_at: str

@dataclass
class InsightIn:
    topic: str
    data: Dict[str, object] = None
    
    def __post_init__(self):
        if self.data is None:
            self.data = {}

@dataclass
class InsightOut:
    id: int
    topic: str
    summary: str
    score: int
    data: Dict[str, object]

@dataclass
class SuggestionIn:
    title: str
    body: str
    tags: str = "analysis,plan"

@dataclass
class SuggestionOut(SuggestionIn):
    id: int
