import sys
import base64
import requests
from my_api import ACY_API


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


if __name__ == '__main__':
    
    api_key = ACY_API
    image_path = "images/Snipaste_2023-12-02_00-26-43.png"
    user_text = "How to plot a figure like this using Python?" # default: What’s in this image?
    output_file_name = "output.md"
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_text
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 4000
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    original_stdout = sys.stdout
    with open(f'outputs/{output_file_name}', 'w') as f:
        sys.stdout = f
        print(response.json()['choices'][0]['message']['content'])
    sys.stdout = original_stdout