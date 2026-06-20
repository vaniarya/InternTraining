from huggingface_hub import InferenceClient
import os
import json

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)


def score_conversion(user_message, npc_reply):

    prompt = f"""
You are a sales trainer.

Evaluate ONLY the STUDENT'S performance.

NPC Shopkeeper:
{npc_reply}

Student:
{user_message}

Score the STUDENT on:

1. Confidence (1-10)
2. Communication (1-10)
3. Sales Skill (1-10)
4. Rapport Building (1-10)

Return ONLY JSON:

{{
    "confidence": 0,
    "communication": 0,
    "sales_skill": 0,
    "rapport": 0,
    "xp": 0,
    "feedback": ""
}}

Do NOT evaluate the NPC.
Evaluate only the student.
"""

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        max_tokens=200
    )

    try:
        return json.loads(
            response.choices[0].message.content
        )

    except:
        return {
            "confidence":5,
            "politeness":5,
            "negotiation":5,
            "feedback":"Could not parse score"
        }