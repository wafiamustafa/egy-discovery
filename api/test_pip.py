"""
Test script to verify pip installation and dependencies
This file can be removed after successful deployment
"""
import sys
import subprocess
import importlib

def test_pip_installation():
    """Test if pip is available and working"""
    try:
        # Test pip version
        result = subprocess.run([sys.executable, '-m', 'pip', '--version'], 
                              capture_output=True, text=True, timeout=30)
        print(f"✅ Pip version: {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"❌ Pip test failed: {e}")
        return False

def test_dependencies():
    """Test if all required dependencies are installed"""
    dependencies = [
        'flask',
        'requests', 
        'dotenv',
        'gunicorn',
        'bs4',  # beautifulsoup4
        'lxml',
        'watchdog'
    ]
    
    results = {}
    for dep in dependencies:
        try:
            importlib.import_module(dep)
            results[dep] = "✅ Installed"
        except ImportError:
            results[dep] = "❌ Missing"
    
    print("\n📦 Dependency Status:")
    for dep, status in results.items():
        print(f"  {dep}: {status}")
    
    return all("✅" in status for status in results.values())

if __name__ == "__main__":
    print("🔍 Testing pip installation and dependencies...")
    
    pip_ok = test_pip_installation()
    deps_ok = test_dependencies()
    
    if pip_ok and deps_ok:
        print("\n🎉 All tests passed! Pip and dependencies are working correctly.")
    else:
        print("\n⚠️  Some tests failed. Check the output above for details.")
