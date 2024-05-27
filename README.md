# Ollama-template
LLM test with OLLAMA models

## 1. Install the Ollama Libraries
```SHELL
curl -fsSL https://ollama.com/install.sh | sh
```

## 2. Run Ollama server
```SHELL
ollama serve
```

## 3. Download a model
```SHELL
ollama pull [model_name]
```

## 4. Run the model
```SHELL
ollama run [model_name] [data_string]
```

## 5. Try API requests to the server
format: the format to return a response in. Currently the only accepted value is json
options: additional model parameters listed in the documentation for the Modelfile such as temperature
system: system message to (overrides what is defined in the Modelfile)
template: the prompt template to use (overrides what is defined in the Modelfile)
context: the context parameter returned from a previous request to /generate, this can be used to keep a short conversational memory
stream: if false the response will be returned as a single response object, rather than a stream of objects
raw: if true no formatting will be applied to the prompt. You may choose to use the raw parameter if you are specifying a full templated prompt in your request to the API
keep_alive: controls how long the model will stay loaded into memory following the request (default: 5m)
```SHELL
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "llama2",
  "prompt": "Why is the cielo azúl?",
  "system": "Responde como si fueras Satoru Gojo y en español",
  "stream": false
}'
```

## 6. Creating custom models
You need to train
```SHELL
ollama create [cmodel_name] -f Modelfile
```
