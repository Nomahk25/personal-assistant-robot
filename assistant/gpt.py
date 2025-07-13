import openai
import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()

# Get the key securely
openai.api_key = os.getenv("API_KEY")

def chat_with_gpt(prompt):
    if not openai.api_key:
        return "OpenAI API key is missing. Please check your .env file."

    response = openai.ChatCompletion.create(
        model="gpt-4",  # or use "gpt-3.5-turbo" if you're on free-tier
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()
