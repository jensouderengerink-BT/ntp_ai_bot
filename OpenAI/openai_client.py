# openai_client.py
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No OpenAI API key found. Please set it in the .env file.")

# Set the API key in the openai client
openai.api_key = api_key

# Now, `openai` can be used for API calls
