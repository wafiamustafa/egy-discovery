import os
import sys
import mimetypes

# Add the server directory to Python path
server_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, server_dir)

from flask import Flask, send_from_directory, jsonify
from config.settings import Config
from routes.api_routes import register_routes

# Ensure proper MIME types for JavaScript modules
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('text/html', '.html')

def create_app():
    """Application factory pattern"""
    # Validate configuration on startup
    Config.validate_config()
    
    # Prefer React build if present, fallback to legacy www
    project_root = os.path.abspath(os.path.join(server_dir, '..'))
    react_dist_path = os.path.join(project_root, 'frontend', 'dist')
    legacy_www_path = os.path.join(project_root, 'www')
    static_root = react_dist_path if os.path.isdir(react_dist_path) else legacy_www_path

    app = Flask(
        __name__,
        static_folder=static_root,
        static_url_path=''  # serve static at root
    )
    
    # Load configuration
    app.config.from_object(Config)
    
    # Register API routes FIRST (higher priority)
    register_routes(app)
    
    # Serve frontend
    @app.route('/')
    def serve_frontend():
        if not app.static_folder:
            return jsonify({"error": "Static folder not configured"}), 500
        return send_from_directory(app.static_folder, 'index.html')
    
    # Catch-all route for frontend routing (LOWER priority, exclude API routes)
    @app.route('/<path:path>')
    def serve_static(path):
        # Skip API routes - they should be handled by the blueprints
        if path.startswith('api/'):
            return jsonify({"error": "API endpoint not found"}), 404
        
        if not app.static_folder:
            return jsonify({"error": "Static folder not configured"}), 500
            
        # Check if it's a static file
        full_path = os.path.join(app.static_folder, path)
        if os.path.exists(full_path):
            # Get the MIME type for the file
            mimetype, _ = mimetypes.guess_type(full_path)
            return send_from_directory(app.static_folder, path, mimetype=mimetype)
        
        # For SPA routing, serve index.html
        return send_from_directory(app.static_folder, 'index.html')
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not found"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )
