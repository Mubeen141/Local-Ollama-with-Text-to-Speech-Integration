#Local Ollama with Text to Speech
#Mubeen Ahmed Jawad
#mubeenjawad87@gmail.com

import subprocess
import pyttsx3
import requests

engine = pyttsx3.init()
engine.setProperty('rate', 200)

def query_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "phi3", "prompt": prompt, "stream": False}
        )
        data = response.json()
        return data.get('response', '').strip()
    except requests.exceptions.RequestException as e:
        return f"[Request failed: {e}]"
    except ValueError:
        return "[Invalid JSON received from Ollama]"

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop: you talk, Ollama answers
print("Jarvis is online. Type 'exit' to quit.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    response = query_ollama(user_input)
    print("Jarvis:", response)
    speak(response)
