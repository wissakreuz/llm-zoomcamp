# %%
import openai

# %%
from openai import OpenAI

# %%
client=OpenAI()

# %%
import os

# %%
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "is it too late to join the course?"}
    ]
)


# %%
response.choices[0].message["content"]
