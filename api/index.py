"""
Vercel serverless function entry point for Egy Discovery Flask API
"""
import sys
import os

# Add the server directory to Python path
server_dir = os.path.join(os.path.dirname(__file__), '..', 'server')
sys.path.insert(0, server_dir)

# Import and create the Flask app
from server.main import create_app

# Create the Flask app instance
app = create_app()

# Vercel expects the app to be named 'app'
# This is the entry point for serverless functions

# For debugging - you can remove this in production
if __name__ == "__main__":
    print("Flask app created successfully")
    print(f"App name: {app.name}")
    print(f"App debug: {app.debug}")
