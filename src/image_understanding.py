import sys
import base64
import requests
from my_api import ACY_API


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Function to understand image and save output
def call_gpt4v_for_image_understanding(image_path, user_text, output_file_name="output.md", max_tokens=4000):
    base64_image = encode_image(image_path)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ACY_API}"
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
        "max_tokens": max_tokens,
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    original_stdout = sys.stdout
    with open(f'outputs/{output_file_name}', 'w') as f:
        sys.stdout = f
        print(response.json()['choices'][0]['message']['content'])
    sys.stdout = original_stdout


if __name__ == '__main__':
    
    image_path = "images/ponyo036.jpg"
    user_text = "How to plot a figure like this using Python?" # default: What’s in this image?
    output_file_name = "output2.md"
    max_tokens = 4000
    
    call_gpt4v_for_image_understanding(image_path, user_text, output_file_name, max_tokens)