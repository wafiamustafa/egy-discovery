import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration class"""
    
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    
    # Server settings
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 8000))
    
    # N8N settings
    N8N_BASE_URL = os.getenv('N8N_BASE_URL', 'http://localhost:5678')
    N8N_API_KEY = os.getenv('N8N_API_KEY', '')
    N8N_TIMEOUT_SECONDS = float(os.getenv('N8N_TIMEOUT_SECONDS', '30'))
    N8N_WEBHOOK_URL = os.getenv('N8N_WEBHOOK_URL', '')
    
    # OpenAI settings
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    OPENAI_MAX_TOKENS = int(os.getenv('OPENAI_MAX_TOKENS', '1000'))
    OPENAI_TEMPERATURE = float(os.getenv('OPENAI_TEMPERATURE', '0.7'))
    
    # Database settings
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///egy_discovery.db')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
    
    # Security settings
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'dev-jwt-secret')
    
    # External services
    GOOGLE_ANALYTICS_ID = os.getenv('GOOGLE_ANALYTICS_ID', '')
    SENTRY_DSN = os.getenv('SENTRY_DSN', '')
    
    # Feature flags
    ENABLE_AI_AGENTS = os.getenv('ENABLE_AI_AGENTS', 'true').lower() == 'true'
    ENABLE_N8N_WORKFLOWS = os.getenv('ENABLE_N8N_WORKFLOWS', 'true').lower() == 'true'
    ENABLE_WEB_SCRAPING = os.getenv('ENABLE_WEB_SCRAPING', 'true').lower() == 'true'
    
    @classmethod
    def validate_config(cls):
        """Validate required configuration values"""
        required_vars = []
        
        if cls.ENABLE_N8N_WORKFLOWS and not cls.N8N_API_KEY:
            required_vars.append('N8N_API_KEY')
        
        if cls.ENABLE_AI_AGENTS and not cls.OPENAI_API_KEY:
            required_vars.append('OPENAI_API_KEY')
        
        if required_vars:
            print(f"Warning: Missing required environment variables: {', '.join(required_vars)}")
            print("Some features may not work properly.")
        
        return len(required_vars) == 0
