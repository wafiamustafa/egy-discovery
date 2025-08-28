SHELL := /bin/zsh

.PHONY: dev run start docker-build docker-up docker-down docker-logs test clean frontend-dev api-test help

# Development Commands
dev:
	FLASK_DEBUG=1 python /Users/wafiamustafa/egy_discovery/server/main.py

# Run without debug
run:
	python /Users/wafiamustafa/egy_discovery/server/main.py

# Alias
start: run

# Frontend Development
frontend-dev:
	cd frontend && npm run dev

# Docker Commands
docker-build:
	docker build -t egy-discovery:latest .

docker-up:
	docker compose up -d --build

docker-down:
	docker compose down

docker-logs:
	docker compose logs -f app | cat

# Testing Commands
test:
	@echo "Testing API endpoints..."
	@curl -s http://127.0.0.1:8000/api/health | jq . || echo "Health check failed"
	@echo "Testing Analysis API..."
	@curl -s -X POST http://127.0.0.1:8000/api/analysis/insights \
		-H "Content-Type: application/json" \
		-d '{"topic":"Test","data":{"roas":2.5,"ctr":0.04}}' | jq . || echo "Analysis API failed"

api-test:
	@echo "🧪 Testing Business Intelligence APIs..."
	@echo "📍 Health Check..."
	@curl -s http://127.0.0.1:8000/api/health | jq .
	@echo -e "\n📍 Market Analysis..."
	@curl -s -X POST http://127.0.0.1:8000/api/analysis/insights \
		-H "Content-Type: application/json" \
		-d '{"topic":"Test Insight","data":{"roas":3.0,"ctr":0.05}}' | jq .
	@echo -e "\n📍 Marketing Campaign..."
	@curl -s -X POST http://127.0.0.1:8000/api/marketing/campaigns \
		-H "Content-Type: application/json" \
		-d '{"platform":"meta","name":"Test Campaign"}' | jq .
	@echo -e "\n📍 Financial Transaction..."
	@curl -s -X POST http://127.0.0.1:8000/api/accounting/transactions \
		-H "Content-Type: application/json" \
		-d '{"date":"2025-08-28","type":"expense","account":"marketing","amount":150,"category":"advertising"}' | jq .
	@echo -e "\n📍 Intelligent Agent..."
	@curl -s -X POST http://127.0.0.1:8000/api/agents/route \
		-H "Content-Type: application/json" \
		-d '{"prompt":"enrich this lead","params":{"agent":"enrich","payload":{"extract":"photography services in Hurghada"}}}' | jq .

# Utility Commands
clean:
	@echo "🧹 Cleaning up..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name "*.egg-info" -exec rm -rf {} +
	@echo "✨ Cleanup complete!"

# Help
help:
	@echo "🚀 Egy Discovery - Business Intelligence Platform"
	@echo ""
	@echo "📋 Available Commands:"
	@echo "  dev           - Start Flask server in debug mode"
	@echo "  run/start     - Start Flask server"
	@echo "  frontend-dev  - Start React development server"
	@echo ""
	@echo "🐳 Docker Commands:"
	@echo "  docker-build  - Build Docker image"
	@echo "  docker-up     - Start services with Docker Compose"
	@echo "  docker-down   - Stop Docker services"
	@echo "  docker-logs   - View container logs"
	@echo ""
	@echo "🧪 Testing:"
	@echo "  test          - Quick API health check"
	@echo "  api-test      - Comprehensive API testing"
	@echo ""
	@echo "🛠️  Utilities:"
	@echo "  clean         - Clean Python cache files"
	@echo "  help          - Show this help message"
	@echo ""
	@echo "💡 Quick Start:"
	@echo "  make docker-up    # Start the full platform"
	@echo "  make api-test     # Test all features"
	@echo "  make help         # Show available commands"


