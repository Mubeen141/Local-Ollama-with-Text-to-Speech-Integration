import pyttsx3

engine = pyttsx3.init()
engine.save_to_file("Volunteering at a cancer treatment center has helped me discover my path. When I see patients trapped in not only the hospital but also a moment in time by their diseases, I talk to them. For six hours a day, three times a week, Ivana is surrounded by IV stands, empty walls, and busy nurses that quietly yet constantly remind her of her breast cancer. Her face is pale and tired, yet kind--not unlike my grandmother’s. I need only to smile and say hello to see her brighten up as life returns to her face. Upon our first meeting, she opened up about her two sons, her hometown, and her knitting group--no mention of her disease. Without even standing up, the three of us—Ivana, me, and my grandmother--had taken a walk together.", "output.wav")
engine.runAndWait()

from pydub import AudioSegment
from pydub.effects import normalize

# Load your TTS-generated WAV file
sound = AudioSegment.from_wav("output.wav")

# Create echo by adding silence before a quieter copy of the sound
delay = AudioSegment.silent(duration=200)  # 200 ms delay
quiet_echo = sound - 12  # lower volume
echo = delay + quiet_echo

# Overlay echo on top of original
combined = sound.overlay(echo)

# Optional: normalize volume
final = normalize(combined)

# Export to new file
final.export("jarvis_effect.wav", format="wav")
