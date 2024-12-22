from setuptools import setup, find_packages

setup(
    name="linkedin-automation",
    version="0.1.0",
    packages=find_packages(include=['app', 'app.*']),
    package_dir={'': '.'},
    package_data={'app': ['**/*.py']},
    install_requires=[
        "playwright>=1.41.1",
        "autogen>=1.0.16",
        "beautifulsoup4>=4.12.2",
        "openai>=1.3.5",
        "fastapi>=0.109.0",
        "uvicorn>=0.27.0",
        "python-dotenv>=1.0.0",
        "supabase>=2.3.0",
        "apscheduler>=3.10.4",
        "pydantic>=2.5.3",
        "python-jose>=3.3.0",
        "python-multipart>=0.0.6",
        "requests>=2.31.0",
        "uuid>=1.30",
        "aiohttp>=3.9.1",
        "asyncio>=3.4.3",
        "python-dateutil>=2.8.2",
        "pytz>=2023.3.post1",
        "postgrest>=0.13.0",
        "httpx>=0.26.0",
        "websockets>=12.0",
        "typing-extensions>=4.9.0"
    ],
)
