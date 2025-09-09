from setuptools import setup, find_packages

setup(
    name="egy-discovery-api",
    version="1.0.0",
    description="Egy Discovery API - Business Intelligence Platform",
    packages=find_packages(),
    install_requires=[
        "Flask==3.0.3",
        "requests==2.32.4",
        "python-dotenv==1.0.1",
        "gunicorn==23.0.0",
        "beautifulsoup4==4.12.2",
        "lxml==4.9.3",
        "watchdog==5.0.3",
    ],
    python_requires=">=3.11",
)
