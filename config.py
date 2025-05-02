# config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Default models
DEFAULT_MODEL = "gpt-3.5-turbo"