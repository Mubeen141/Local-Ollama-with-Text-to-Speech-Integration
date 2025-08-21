import subprocess
import pyttsx3

def query_ollama(prompt):
    # Call Ollama using subprocess
    process = subprocess.Popen(
        ["C:\\Users\\dell\\AppData\\Local\\Programs\\Ollama\\ollama.exe", "run", "phi3"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate(input=prompt.encode())
    return stdout.decode().strip()

def speak(text):
    # Use pyttsx3 for text-to-speech
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)  # Adjust speech speed
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
