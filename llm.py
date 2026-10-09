
import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY missing. Add it to your .env file "
        "or Streamlit Cloud Secrets."
    )

client = Groq(api_key=GROQ_API_KEY)


def generate_response(
    prompt,
    temperature=0.2,
    max_tokens=500
):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content
