# Vercel Python Setup Guide

## 🔧 Ensuring Pip Works on Vercel

### 1. **Explicit Install Command**
```json
{
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python",
      "config": {
        "installCommand": "pip install --upgrade pip && pip install -r api/requirements.txt"
      }
    }
  ]
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
```

### 2. **Vercel Environment Variables**
Set these in Vercel dashboard:
```
PYTHON_VERSION=3.11
PIP_INDEX_URL=https://pypi.org/simple/
PIP_TRUSTED_HOST=pypi.org
```

### 3. **Build Logs to Check**
Look for these in Vercel build logs:
- ✅ "Installing pip dependencies"
- ✅ "Successfully installed Flask"
- ✅ "Python 3.11 detected"

## 🔍 Troubleshooting

### If pip still fails:
1. **Check Python version**: Ensure `runtime.txt` has `python-3.11`
2. **Verify requirements.txt**: Ensure it's in `api/` directory
3. **Check install command**: Should be in `vercel.json` config
4. **Environment variables**: Set `PIP_INDEX_URL` and `PIP_TRUSTED_HOST`

### Alternative approach:
If pip still fails, use `setup.py` instead:
```json
{
  "config": {
    "installCommand": "python setup.py install"
  }
}
```

## 📋 Files Created

- ✅ `api/requirements.txt` - Clean dependencies
- ✅ `api/setup.py` - Alternative installation
- ✅ `api/pip.conf` - Pip configuration
- ✅ `api/test_pip.py` - Verification script
- ✅ `runtime.txt` - Python version
- ✅ Updated `vercel.json` - Install command
