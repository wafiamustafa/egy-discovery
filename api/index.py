"""
Vercel serverless function entry point for Egy Discovery Flask API
"""
import sys
import os
from flask import Flask, request, jsonify

# Add the server directory to Python path
# Vercel puts everything at /var/task
vercel_root = '/var/task'
server_dir = os.path.join(vercel_root, 'server')
if os.path.exists(server_dir):
    sys.path.insert(0, server_dir)
else:
    # Fallback for local development
    server_dir = os.path.join(os.path.dirname(__file__), '..', 'server')
    sys.path.insert(0, os.path.abspath(server_dir))

try:
    # Import Flask app components
    from config.settings import Config
    from routes.api_routes import register_routes
    
    def create_vercel_app():
        """Create Flask app optimized for Vercel serverless"""
        app = Flask(__name__)
        
        # Load configuration
        app.config.from_object(Config)
        app.config['ENV'] = 'production'
        app.config['DEBUG'] = False
        
        # Register API routes
        register_routes(app)
        
        return app
    
    # Create the Flask app instance
    app = create_vercel_app()
    
except ImportError as e:
    # Fallback if imports fail
    app = Flask(__name__)
    
    @app.route('/api/health')
    def health():
        return jsonify({"status": "ok", "message": "API is running", "error": f"Import error: {str(e)}"})
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "API endpoint not found"}), 404

# Vercel serverless handler
def handler(request):
    """Vercel serverless function handler"""
    with app.app_context():
        return app.full_dispatch_request()

# For testing
if __name__ == "__main__":
    print("Flask app created successfully")
    print(f"App name: {app.name}")
    print(f"Routes: {list(app.url_map.iter_rules())}")
