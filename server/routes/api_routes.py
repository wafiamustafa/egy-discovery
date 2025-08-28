from flask import Blueprint, request
from controllers.accounting_controller import AccountingController

# Create blueprints
api_bp = Blueprint('api', __name__, url_prefix='/api')
accounting_bp = Blueprint('accounting', __name__, url_prefix='/api/accounting')
marketing_bp = Blueprint('marketing', __name__, url_prefix='/api/marketing')
analysis_bp = Blueprint('analysis', __name__, url_prefix='/api/analysis')
agents_bp = Blueprint('agents', __name__, url_prefix='/api/agents')

# Initialize controllers
accounting_controller = AccountingController()

# API routes
@api_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return {"status": "ok", "message": "API is running"}

# Accounting routes
@api_bp.route('/accounting/transactions', methods=['POST'])
def create_transaction():
    """Create accounting transaction"""
    return accounting_controller.create_transaction()

@api_bp.route('/accounting/transactions', methods=['GET'])
def list_transactions():
    """List accounting transactions"""
    return accounting_controller.list_transactions()

# Marketing routes
@api_bp.route('/marketing/campaigns', methods=['POST'])
def create_campaign():
    """Create ad campaign"""
    return accounting_controller.create_campaign()

@api_bp.route('/marketing/campaigns', methods=['GET'])
def list_campaigns():
    """List ad campaigns"""
    return accounting_controller.list_campaigns()

@api_bp.route('/marketing/metrics', methods=['POST'])
def create_metric():
    """Create ad metric"""
    return accounting_controller.create_metric()

@api_bp.route('/marketing/metrics', methods=['GET'])
def list_metrics():
    """List ad metrics"""
    return accounting_controller.list_metrics()

# Analysis routes
@api_bp.route('/analysis/insights', methods=['POST'])
def create_insight():
    """Create market insight"""
    return accounting_controller.create_insight()

@api_bp.route('/analysis/insights', methods=['GET'])
def list_insights():
    """List market insights"""
    return accounting_controller.list_insights()

@api_bp.route('/analysis/plan', methods=['POST'])
def create_suggestion():
    """Create plan suggestion"""
    return accounting_controller.create_suggestion()

@api_bp.route('/analysis/plan', methods=['GET'])
def list_suggestions():
    """List plan suggestions"""
    return accounting_controller.list_suggestions()

# Agents routes
@api_bp.route('/agents/route', methods=['POST'])
def run_agent():
    """Run intelligent agent routing"""
    from services.agent_service import AgentService
    
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        params = data.get('params', {})
        
        agent_service = AgentService()
        result = agent_service.run(prompt, params)
        
        return {"ok": True, "result": result}
        
    except Exception as e:
        return {"error": str(e)}, 500

def register_routes(app):
    """Register all API blueprints with the Flask app"""
    app.register_blueprint(api_bp)
    app.register_blueprint(accounting_bp)
    app.register_blueprint(marketing_bp)
    app.register_blueprint(analysis_bp)
    app.register_blueprint(agents_bp)
