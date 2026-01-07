import os
import requests
from errors import AIClientError
from dotenv import load_dotenv
from pathlib import Path
from huggingface_hub import InferenceClient  # <-- must be exactly like this
from errors import AIClientError
from profile_data import profile_info

SYSTEM_MESSAGE = f"""
You are Tendo's AI Helper 2026. 
You answer questions about Tendo Taliq professionally. 
Here is the information you know:
- Name: {profile_info['name']}
- Role: {profile_info['role']}
- Bio: {profile_info['bio']}
- Skills: {', '.join(profile_info['skills'])}
- Projects: {', '.join(profile_info['projects'].keys())}
- Contact: Email: {profile_info['contact']['email']}, LinkedIn: {profile_info['contact']['linkedin']}, Website: {profile_info['contact']['website']}
"""
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)


HF_API_KEY = os.getenv("HF_API_KEY")
print("HF_API_KEY loaded:", bool(HF_API_KEY))

if not HF_API_KEY:
    raise AIClientError("Hugging Face API key not found. Set HF_API_KEY.")
 #Create the client (it chooses a provider automatically)
client = InferenceClient(token=HF_API_KEY)


def get_ai_response(prompt):
    if not prompt.strip():
        raise AIClientError("Prompt cannot be empty")

    try:
        # Chat-style request
        result = client.chat_completion(
            model="deepseek-ai/DeepSeek-V3.2",  # one model known to work
            messages=[
                {"role": "user", "content": prompt}
            ],
        )

        # Extract text
        if result.choices:
            return result.choices[0].message.content.strip()

        return "(no answer)"

    except Exception as e:
        raise AIClientError(f"Hugging Face error: {str(e)}")