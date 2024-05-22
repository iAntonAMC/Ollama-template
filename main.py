import json
import requests

# Preparar los datos para enviar:
model = input("Selecciona el modelo a usar: \n 1-LLAMA2 | 2-TINYLLAMA:\n")
llmodel = str
if int(model) == 1:
    llmodel = "llama2"
elif int(model) == 2:
    llmodel = "tinymodel"
message = str(input("Mensaje/Ask\n>> "))
system = str(input("Cómo deseas que te responda el modelo?\n>> "))

data = {
    "model": llmodel,
    "prompt": message,
    "system": system,
    "stream": False
}

data = json.dumps(data)

print(f"\n",data,"\n")

response = requests.post('http://localhost:11434/api/generate', data)
answer = response.json()
print(f"Llama2 >> " + answer['response'])
