from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)

def generate_npc_response(message):
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {
                "role":"system",
                "content":"You are a friendly marketplace shopkeeper."
            },
            {
                "role":"user",
                "content":message
            }
        ]
    )
    return response.choices[0].message.content