# Vercel Full-Stack Deployment Guide

## 🚀 Overview

This guide covers the complete Vercel deployment setup for a full-stack application with:
- **Frontend**: React + Vite (served as static assets)
- **Backend**: Python + Flask (serverless functions)
- **Build System**: Dual build configuration with optimized routing

## 🔧 Current Architecture

### 1. **Current Vercel Configuration**
The latest `vercel.json` includes multiple builds for both frontend and backend:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "build.sh",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "./frontend/dist",
        "outputDirectory": "/"
      }
    },
    {
      "src": "api/index.py",
      "use": "@vercel/python",
      "config": {
        "maxLambdaSize": "50mb",
        "installCommand": "pip install --upgrade pip && pip install -r api/requirements.txt"
      }
    }
  ],
  "rewrites": [
    { "source": "/api/(.*)", "destination": "/api/index.py" },
    { "source": "/((?!assets).*)", "destination": "/index.html" }
  ],
  "env": {
    "FLASK_ENV": "production",
    "FLASK_DEBUG": "false"
  }
}
```

### 2. **Python Version Specification**
- `runtime.txt`: `python-3.11`
- `vercel.json`: `"runtime": "python3.11"`

### 3. **Dependencies Structure**
```
api/
├── requirements.txt    # Clean, minimal dependencies
├── setup.py          # Alternative installation method
├── pip.conf          # Pip configuration
└── test_pip.py       # Verification script
```

## 🚀 Deployment Steps

### 1. **Pre-deployment Check**
```bash
# Test locally
cd api
python test_pip.py

# Test frontend build
cd ../frontend
npm install
npm run build

# Test build script
cd ..
chmod +x build.sh
./build.sh
```

### 2. **Vercel Environment Variables**
Set these in Vercel dashboard:
```
PYTHON_VERSION=3.11
PIP_INDEX_URL=https://pypi.org/simple/
PIP_TRUSTED_HOST=pypi.org
FLASK_ENV=production
FLASK_DEBUG=false
```

### 3. **Build Configuration**
The current setup uses:
- **Frontend Build**: `@vercel/static-build` with `build.sh` script
- **Backend Build**: `@vercel/python` for API routes
- **Output Directory**: Frontend assets served from root (`/`)
- **Max Lambda Size**: 50MB for Python functions

### 4. **Build Logs to Check**
Look for these in Vercel build logs:

**Frontend Build:**
- ✅ "Running build.sh"
- ✅ "Frontend build completed"
- ✅ "Static assets generated in ./frontend/dist"

**Backend Build:**
- ✅ "Installing pip dependencies"
- ✅ "Successfully installed Flask"
- ✅ "Python 3.11 detected"
- ✅ "Lambda size under 50MB"

## 🔍 Troubleshooting

### Frontend Build Issues:
1. **Build script permissions**: Ensure `build.sh` is executable
2. **Node.js dependencies**: Check `frontend/package.json` and `package-lock.json`
3. **Build output**: Verify `frontend/dist` directory is created
4. **Static assets**: Check if assets are properly copied to root

### Backend (Python) Issues:
1. **Check Python version**: Ensure `runtime.txt` has `python-3.11`
2. **Verify requirements.txt**: Ensure it's in `api/` directory
3. **Lambda size**: If >50MB, optimize dependencies or increase `maxLambdaSize`
4. **Environment variables**: Set `FLASK_ENV` and `FLASK_DEBUG` in Vercel dashboard

### Routing Issues:
1. **API routes**: Should match `/api/(.*)` pattern
2. **Static assets**: Excluded from SPA fallback with `/((?!assets).*)`
3. **SPA routing**: Non-API routes fallback to `/index.html`

### Alternative approaches:
**For pip issues:**
```json
{
  "config": {
    "installCommand": "python setup.py install"
  }
}
```

**For build issues:**
```json
{
  "config": {
    "buildCommand": "npm run vercel-build",
    "outputDirectory": "../"
  }
}
```

## 📋 Key Configuration Files

### Core Files:
- ✅ `vercel.json` - Main deployment configuration
- ✅ `build.sh` - Frontend build script
- ✅ `runtime.txt` - Python version specification

### Frontend Files:
- ✅ `frontend/package.json` - Node.js dependencies
- ✅ `frontend/vite.config.js` - Build configuration
- ✅ `frontend/dist/` - Build output directory

### Backend Files:
- ✅ `api/requirements.txt` - Python dependencies
- ✅ `api/index.py` - Main API entry point
- ✅ `api/setup.py` - Alternative installation method
- ✅ `api/pip.conf` - Pip configuration
- ✅ `api/test_pip.py` - Verification script

## 🎯 Key Features of Current Setup

1. **Dual Build System**: Separate builds for frontend (React/Vite) and backend (Python/Flask)
2. **Smart Routing**: API requests routed to Python, everything else to SPA
3. **Asset Optimization**: Static assets excluded from SPA fallback routing
4. **Environment Management**: Production-specific Flask configuration
5. **Lambda Optimization**: 50MB limit for efficient serverless functions
