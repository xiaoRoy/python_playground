from google import genai
from google.genai import types
import os

api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)
# response = client.models.generate_content(model="gemini-2.0-flash", contents="tell me about RAG")

# print(response.text)

ROLE_USER = "user"


def get_completion(prompt, model="gemini-2.0-flash"):
    generate_content_config = types.GenerateContentConfig(temperature=0.0, system_instruction=[
        types.Part.from_text(
            text="You are a pirate who is good at gemini. And your job is to teach me to learn how to use Gemini in the form of calling the API using pyhon.")
    ])
    contents = [types.Content(role=ROLE_USER, parts=[types.Part.from_text(text=prompt)])]

    responses = client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config
    )

    for chunk in responses:
        print(chunk.text, end="")


get_completion(prompt="tell me about the function generate_content_stream")
