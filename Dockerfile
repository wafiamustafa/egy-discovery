###############################
# Stage 1: Build React frontend
###############################
FROM node:20-alpine AS frontend-builder
WORKDIR /frontend
COPY frontend/package*.json ./
RUN npm ci || npm install
COPY frontend .
RUN npm run build

###############################
# Stage 2: Python backend image
###############################
FROM python:3.11-slim AS app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# System deps (add as needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Install Python deps first (better layer caching)
COPY requirements.txt ./
RUN python -m pip install --upgrade pip setuptools wheel && \
    pip install -r requirements.txt

# Copy backend
COPY server ./server

# Copy built frontend to serve as static files
COPY --from=frontend-builder /frontend/dist ./frontend/dist

EXPOSE 8000

# Use gunicorn with app factory
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "server.main:create_app()"]

 