import base64
import os
import json
import requests


image_path = str(input("\nRuta de la imagen a describir: "))

with open(image_path, "rb") as image_file:
    image_data = image_file.read()
    encoded_image_data = base64.b64encode(image_data)
    base64_string = str(encoded_image_data.decode('utf-8'))

data = {
    "model": "llava",
    "prompt": "Describe la siguiente imagen",
    "images": [base64_string],
    "stream": False
}

data = json.dumps(data)

print(f"\nData: ",data,"\n")

response = requests.post('http://localhost:11434/api/generate', data)
answer = response.json()

print(f"\nLlava >> " + answer['response'])
