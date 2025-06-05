import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Bonjour, que peux-tu faire ?"}
    ]
)

print(response.choices[0].message["content"])