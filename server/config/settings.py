import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration class"""
    
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    # N8N settings
    N8N_BASE_URL = os.getenv('N8N_BASE_URL', '')
    N8N_API_KEY = os.getenv('N8N_API_KEY', '')
    N8N_TIMEOUT_SECONDS = float(os.getenv('N8N_TIMEOUT_SECONDS', '30'))
    
    # Server settings
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 8000))
