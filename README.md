# Egy Discovery - Full-Stack Business Intelligence Platform

A comprehensive business intelligence platform built with clean architecture principles, featuring a modern React frontend and Flask backend with intelligent agent routing, automated workflows, and comprehensive business operations management.

## 🏗️ Architecture Overview

The application follows clean architecture principles with clear separation of concerns:

```
egy_discovery/
├── server/                 # Backend (Python/Flask)
│   ├── config/            # Configuration management
│   ├── controllers/       # Request handlers (MVC Controller)
│   ├── models/            # Data models (MVC Model)
│   ├── routes/            # API route definitions
│   ├── services/          # Business logic layer
│   ├── workflows/         # N8N workflow definitions
│   └── main.py            # Main server entry point
├── frontend/              # Frontend (React/TypeScript)
│   ├── src/               # Source code
│   │   ├── App.tsx        # Main application with all components
│   │   │   ├── Analysis   # Market insights dashboard
│   │   │   ├── Marketing  # Campaign management
│   │   │   └── Accounting # Financial tracking
│   │   ├── index.css      # Comprehensive styling
│   │   └── main.tsx       # Application entry point
│   ├── public/            # Static assets
│   └── package.json       # Node.js dependencies
├── requirements.txt        # Python dependencies
├── Dockerfile             # Multi-stage Docker build
├── docker-compose.yml     # Container orchestration
├── .env                   # Environment variables
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.11+**
- **Node.js 20+** (for local development)
- **Docker & Docker Compose** (recommended)
- **pip & npm**

### Quick Start with Docker (Recommended)

1. **Clone and start the application**
   ```bash
   git clone <repository-url>
   cd egy_discovery
   
   # Start with Docker (builds React frontend automatically)
   make docker-up
   
   # Or manually
   docker compose up -d
   ```

2. **Access the application**
   - **Frontend**: http://127.0.0.1:8000
   - **API Health**: http://127.0.0.1:8000/api/health

3. **Test the platform**
   ```bash
   # Run comprehensive API tests
   make api-test
   
   # View container logs
   make docker-logs
   ```

### Local Development

1. **Backend Setup**
   ```bash
   # Create and activate virtual environment
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   
   # Install Python dependencies
   pip install -r requirements.txt
   
   # Run Flask server
   make start
   ```

2. **Frontend Development**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## 🆕 New Features & Capabilities

### **🎯 Business Intelligence Dashboard**
- **Market Analysis** - Create insights with ROAS/CTR scoring
- **Marketing Management** - Multi-platform campaign tracking
- **Financial Operations** - Complete transaction management
- **Strategic Planning** - Automated suggestion generation

### **🤖 Intelligent Agent System**
- **Smart Routing** - Automatic agent selection based on prompts
- **Specialized Agents**:
  - **Lead Generation** - Prospect identification and scoring
  - **Market Research** - Automated market analysis
  - **Web Scraping** - Content extraction with BeautifulSoup
  - **Data Enrichment** - Hurghada-specific scoring algorithms
  - **Accounting** - Financial transaction processing
  - **Marketing** - Campaign optimization

### **📊 Data Models & Analytics**
- **AccountingTransaction** - Financial tracking with metadata
- **AdCampaign** - Multi-platform campaign management
- **AdMetric** - Performance analytics and KPIs
- **MarketInsight** - Automated scoring and analysis
- **PlanSuggestion** - Strategic planning support

### **🔌 N8N Workflow Integration**
- **Lead Processing** - Automated lead ingestion and enrichment
- **Metrics Collection** - Real-time advertising performance data
- **Financial Automation** - Transaction processing workflows

## 🏛️ Backend Architecture (MVC)

### Models (`server/models/`)
- **`n8n_request.py`**: Data models for N8N requests and responses
- **`accounting.py`**: Business data models (transactions, campaigns, insights)
- Uses Python classes for in-memory storage (production-ready database integration available)

### Views (`server/routes/`)
- **`api_routes.py`**: Comprehensive API endpoint definitions using Flask blueprints
- **RESTful API design** with proper HTTP status codes and error handling
- **Blueprint organization** for modular route management

### Controllers (`server/controllers/`)
- **`n8n_controller.py`**: Handles HTTP requests and coordinates with services
- **`accounting_controller.py`**: Business operations management
- Input validation, error handling, and business logic coordination

### Services (`server/services/`)
- **`n8n_service.py`**: Business logic for N8N operations
- **`agent_service.py`**: Intelligent routing and agent management
- Handles API calls, response processing, and business intelligence

### Configuration (`server/config/`)
- **`settings.py`**: Centralized configuration management
- Environment variable handling with sensible defaults

### Workflows (`server/workflows/`)
- **N8N workflows**: JSON workflow definitions for business automation
- **Lead processing**, **metrics collection**, **financial operations**

## 🎨 Frontend Architecture (React)

### **Modern React Implementation**
- **TypeScript support** for type safety
- **Consolidated component architecture** - All components in single App.tsx
- **Responsive design** with CSS Grid and Flexbox
- **Real-time API integration** with error handling

### **Unified Component Structure**
- **`App.tsx`** - Single file containing all components:
  - **Analysis Component** - Market insights with interactive forms
  - **Marketing Component** - Campaign management dashboard
  - **Accounting Component** - Financial transaction interface
  - **Navigation System** - Clean routing between components

### **User Experience Features**
- **Interactive forms** with real-time validation
- **JSON response display** for debugging and verification
- **Professional styling** with gradients and hover effects
- **Mobile-responsive** design for all device sizes
- **Clean CSS architecture** with organized class-based styling

## 🔌 API Endpoints

### **Health Check**
- `GET /api/health` - API health status

### **Business Operations**
- `POST /accounting/transactions` - Create financial transactions
- `GET /accounting/transactions` - List transactions with filtering
- `POST /marketing/campaigns` - Create ad campaigns
- `GET /marketing/campaigns` - List campaigns by platform
- `POST /marketing/metrics` - Ingest performance metrics
- `GET /marketing/metrics` - Retrieve metrics with filtering

### **Market Intelligence**
- `POST /analysis/insights` - Create market insights with automatic scoring
- `GET /analysis/insights` - List market insights
- `POST /analysis/plan` - Create strategic suggestions
- `GET /analysis/plan` - List planning suggestions

### **Intelligent Agents**
- `POST /agents/route` - Run intelligent agent routing
- **Automatic agent selection** based on prompt content
- **Specialized processing** for different business operations

### **N8N Integration**
- `POST /n8n/execute` - Execute N8N workflows
- **Webhook mode** and **REST API mode** support

## 🐳 Docker & Deployment

### **Multi-Stage Build**
- **Node 20** for React frontend compilation
- **Python 3.11** for backend services
- **Gunicorn** for production WSGI deployment
- **Automatic React build** during container creation

### **Container Management**
```bash
# Build and start
make docker-up

# View logs
make docker-logs

# Stop services
make docker-down

# Rebuild
make docker-build
```

### **Current Status**
✅ **Backend**: Running on http://localhost:8000  
✅ **Frontend**: Served from backend at http://localhost:8000  
✅ **API**: All endpoints functional and tested  
✅ **Docker**: Multi-stage build working correctly  

## 🛠️ Development

### **Backend Development**
- Follow Flask best practices and clean architecture
- Use type hints and comprehensive error handling
- Implement proper validation and business logic
- Add unit tests for new features

### **Frontend Development**
- **Consolidated structure**: All components in App.tsx for easy maintenance
- Use modern React patterns (hooks, functional components)
- Follow TypeScript best practices
- Implement responsive design principles
- Add proper error handling and user feedback

### **Code Style**
- **Python**: Follow PEP 8 guidelines
- **TypeScript/React**: Use consistent formatting and patterns
- **HTML/CSS**: Follow semantic HTML principles

## 🧪 Testing

### **API Testing**
```bash
# Health check
curl http://127.0.0.1:8000/api/health

# Create market insight
curl -X POST http://127.0.0.1:8000/analysis/insights \
  -H "Content-Type: application/json" \
  -d '{"topic":"Test","data":{"roas":2.5,"ctr":0.04}}'

# Test intelligent agent
curl -X POST http://127.0.0.1:8000/agents/route \
  -H "Content-Type: application/json" \
  -d '{"prompt":"enrich this lead","params":{"agent":"enrich","payload":{"extract":"photography in Hurghada"}}}'
```

### **Comprehensive Testing**
```bash
# Run all API tests
make api-test

# Quick health check
make test
```

## 📦 Production Deployment

### **Environment Configuration**
```bash
# Required environment variables
FLASK_DEBUG=False
HOST=0.0.0.0
PORT=8000
SECRET_KEY=your-secret-key

# Optional N8N configuration
N8N_BASE_URL=https://your-n8n-instance.com
N8N_API_KEY=your-api-key
N8N_TIMEOUT_SECONDS=30
```

### **Scaling Considerations**
- **Database**: Replace in-memory storage with PostgreSQL/MySQL
- **Caching**: Add Redis for session and data caching
- **Load Balancing**: Use Nginx for reverse proxy and SSL termination
- **Monitoring**: Implement health checks and logging

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes following the architecture patterns
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the API documentation
- Review the code examples and workflows

## 🔄 Version History

- **v3.1.0**: Cleaned up frontend structure, consolidated components, Docker optimization
- **v3.0.0**: Full business intelligence platform with React frontend and intelligent agents
- **v2.0.0**: Clean architecture implementation with MVC pattern
- **v1.0.0**: Initial Flask application with basic N8N integration
