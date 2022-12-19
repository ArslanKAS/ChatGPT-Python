import os
import openai

openai.api_key = "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"

while True:
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=input("\n::: "),
    temperature=0,
    max_tokens=600,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0
    )
    print(response["choices"][0]["text"])