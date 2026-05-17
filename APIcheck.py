import os
from openai import OpenAI

VENICE_API_KEY = "VENICE_ADMIN_KEY_hg4MQxMOQ9h59qADUUSHI8u_3C5XXTacCoGmSQE61_"  # Replace with your actual key


client = OpenAI(
    base_url="https://api.venice.ai/v1",
    api_key=VENICE_API_KEY
)

try:
    completion = client.chat.completions.create(
        model="e2ee-glm-4-7-p",
        messages=[{"role": "user", "content": "Reply with exactly: OK"}],
        max_tokens=10,
        temperature=0.0
    )
    reply = completion.choices[0].message.content
    print(f"✅ SUCCESS! Response: '{reply}'")
    print(f"Full response object: {completion}")
except Exception as e:
    print(f"❌ ERROR: {e}")