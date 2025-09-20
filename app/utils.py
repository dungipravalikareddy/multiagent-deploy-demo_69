# app/utils.py
from dotenv import load_dotenv
import os

load_dotenv()

def check_openai_key():
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise EnvironmentError("OPENAI_API_KEY is not set. Add it to environment or .env")
    return key
