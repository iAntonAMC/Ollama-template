import json
import requests

response = requests.get('http://localhost:11434/api/tags')

print('Success!')
answer = response.json()
print(answer["done"])
