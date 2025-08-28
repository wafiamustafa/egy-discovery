from flask import request, jsonify
from datetime import datetime, date
from typing import Dict, Any, List
import json

class AccountingController:
    """Controller for accounting, marketing, and analysis operations"""
    
    def __init__(self):
        # In-memory storage for demo purposes
        # In production, use database
        self.transactions = []
        self.campaigns = []
        self.metrics = []
        self.insights = []
        self.suggestions = []
        self._counter = 1
    
    def _get_next_id(self) -> int:
        """Get next available ID"""
        self._counter += 1
        return self._counter - 1
    
    def create_transaction(self) -> Dict[str, Any]:
        """Create a new accounting transaction"""
        try:
            data = request.get_json()
            
            # Validate required fields
            required_fields = ['date', 'type', 'account', 'amount', 'category']
            for field in required_fields:
                if field not in data:
                    return jsonify({"error": f"Missing required field: {field}"}), 400
            
            # Create transaction
            transaction = {
                "id": self._get_next_id(),
                "date": data['date'],
                "type": data['type'],
                "account": data['account'],
                "counterparty": data.get('counterparty'),
                "currency": data.get('currency', 'USD'),
                "amount": float(data['amount']),
                "category": data['category'],
                "description": data.get('description'),
                "meta": data.get('meta', {}),
                "created_at": datetime.now().isoformat()
            }
            
            self.transactions.append(transaction)
            return jsonify(transaction), 201
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def list_transactions(self) -> Dict[str, Any]:
        """List accounting transactions with optional filtering"""
        try:
            account = request.args.get('account')
            category = request.args.get('category')
            
            filtered_transactions = self.transactions
            
            if account:
                filtered_transactions = [t for t in filtered_transactions if t['account'] == account]
            if category:
                filtered_transactions = [t for t in filtered_transactions if t['category'] == category]
            
            # Sort by ID descending and limit to 200
            filtered_transactions.sort(key=lambda x: x['id'], reverse=True)
            return jsonify(filtered_transactions[:200])
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def create_campaign(self) -> Dict[str, Any]:
        """Create a new ad campaign"""
        try:
            data = request.get_json()
            
            # Validate required fields
            if 'platform' not in data or 'name' not in data:
                return jsonify({"error": "Missing required fields: platform, name"}), 400
            
            # Create campaign
            campaign = {
                "id": self._get_next_id(),
                "platform": data['platform'],
                "external_id": data.get('external_id'),
                "name": data['name'],
                "objective": data.get('objective'),
                "status": data.get('status', 'draft'),
                "budget_daily": float(data.get('budget_daily', 0)),
                "start_date": data.get('start_date'),
                "end_date": data.get('end_date'),
                "targeting": data.get('targeting', {}),
                "created_at": datetime.now().isoformat()
            }
            
            self.campaigns.append(campaign)
            return jsonify(campaign), 201
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def list_campaigns(self) -> Dict[str, Any]:
        """List ad campaigns with optional filtering"""
        try:
            platform = request.args.get('platform')
            
            filtered_campaigns = self.campaigns
            
            if platform:
                filtered_campaigns = [c for c in filtered_campaigns if c['platform'] == platform]
            
            # Sort by ID descending and limit to 200
            filtered_campaigns.sort(key=lambda x: x['id'], reverse=True)
            return jsonify(filtered_campaigns[:200])
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def create_metric(self) -> Dict[str, Any]:
        """Create a new ad metric"""
        try:
            data = request.get_json()
            
            # Validate required fields
            if 'date' not in data:
                return jsonify({"error": "Missing required field: date"}), 400
            
            # Create metric
            metric = {
                "id": self._get_next_id(),
                "campaign_id": data.get('campaign_id'),
                "date": data['date'],
                "impressions": int(data.get('impressions', 0)),
                "clicks": int(data.get('clicks', 0)),
                "spend": float(data.get('spend', 0)),
                "conversions": int(data.get('conversions', 0)),
                "revenue": float(data.get('revenue', 0)),
                "metrics": data.get('metrics', {}),
                "created_at": datetime.now().isoformat()
            }
            
            self.metrics.append(metric)
            return jsonify(metric), 201
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def list_metrics(self) -> Dict[str, Any]:
        """List ad metrics with optional filtering"""
        try:
            campaign_id = request.args.get('campaign_id')
            
            filtered_metrics = self.metrics
            
            if campaign_id:
                filtered_metrics = [m for m in filtered_metrics if m['campaign_id'] == int(campaign_id)]
            
            # Sort by date descending, then ID descending, and limit to 500
            filtered_metrics.sort(key=lambda x: (x['date'], x['id']), reverse=True)
            return jsonify(filtered_metrics[:500])
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def create_insight(self) -> Dict[str, Any]:
        """Create a new market insight with automatic scoring"""
        try:
            data = request.get_json()
            
            # Validate required fields
            if 'topic' not in data:
                return jsonify({"error": "Missing required field: topic"}), 400
            
            # Calculate score based on data
            score = 0
            insight_data = data.get('data', {})
            
            if 'roas' in insight_data:
                roas = float(insight_data['roas'] or 0)
                score += min(int(roas * 20), 60)
            
            if 'ctr' in insight_data:
                ctr = float(insight_data['ctr'] or 0)
                score += min(int(ctr * 100), 40)
            
            # Create summary
            summary = f"Insight for {data['topic']}: ROAS={insight_data.get('roas', 0)}, CTR={insight_data.get('ctr', 0)}. Score={score}/100."
            
            # Create insight
            insight = {
                "id": self._get_next_id(),
                "topic": data['topic'],
                "summary": summary,
                "score": score,
                "data": insight_data,
                "created_at": datetime.now().isoformat()
            }
            
            self.insights.append(insight)
            return jsonify(insight), 201
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def list_insights(self) -> Dict[str, Any]:
        """List market insights"""
        try:
            # Sort by ID descending and limit to 200
            sorted_insights = sorted(self.insights, key=lambda x: x['id'], reverse=True)
            return jsonify(sorted_insights[:200])
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def create_suggestion(self) -> Dict[str, Any]:
        """Create a new plan suggestion"""
        try:
            data = request.get_json()
            
            # Validate required fields
            if 'title' not in data or 'body' not in data:
                return jsonify({"error": "Missing required fields: title, body"}), 400
            
            # Create suggestion
            suggestion = {
                "id": self._get_next_id(),
                "title": data['title'],
                "body": data['body'],
                "tags": data.get('tags', 'analysis,plan'),
                "created_at": datetime.now().isoformat()
            }
            
            self.suggestions.append(suggestion)
            return jsonify(suggestion), 201
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    def list_suggestions(self) -> Dict[str, Any]:
        """List plan suggestions"""
        try:
            # Sort by ID descending and limit to 200
            sorted_suggestions = sorted(self.suggestions, key=lambda x: x['id'], reverse=True)
            return jsonify(sorted_suggestions[:200])
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
