from google import genai
import os
from google.genai import types


def setup_gemini():
    api_key = os.getenv("GOOGLE_API_KEY")
    return genai.Client(api_key=api_key)


ROLE_USER = "user"
ROLE_MODEL = "model"

def generate_content(role, text):
    return types.Content(role=role, parts=[types.Part.from_text(text=text)])
