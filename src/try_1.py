import os
from openai import OpenAI
from my_api import ACY_API

if __name__ == '__main__':
    
    CLIENT = OpenAI(api_key=ACY_API)
    MODEL = "gpt-4-vision-preview"
    SYSTEM_CONTENT = ""
    USER_CONTENT = "What’s in this image?"
    MAX_TOKENS = 300
    
    response = CLIENT.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": USER_CONTENT},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                        },
                    },
                ],
            }
        ],
        max_tokens=MAX_TOKENS,
    )

    print(response.choices[0].message.content)