from setuptools import setup, find_packages

setup(
    name="linkedin-automation",
    version="0.1.0",
    packages=find_packages(include=['ae', 'ae.*', 'app', 'app.*']),
    install_requires=[
        "playwright>=1.39.0",
        "autogen>=1.0.16",
        "beautifulsoup4>=4.12.2",
        "openai>=1.3.5",
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "python-dotenv>=0.19.0",
        "supabase>=0.7.1",
        "apscheduler>=3.9.1",
    ],
)
