import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()


HF_TOKEN = os.getenv("HF_TOKEN")


if not HF_TOKEN:
    raise ValueError(
        "HF_TOKEN is not found. Please add your "
        "Hugging Face token to the .env file."
    )


client = InferenceClient(
    token=HF_TOKEN
)


def generate_response(
    prompt,
    temperature=0.2,
    max_tokens=500
):

    response = client.chat_completion(
        model="Qwen/Qwen2.5-72B-Instruct",

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