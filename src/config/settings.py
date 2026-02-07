# src/config/settings.py
from dotenv import load_dotenv
import os

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "doc-agent-pipeline")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

