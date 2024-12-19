import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160)  # Speed (words per minute)

def read_text(text):
    engine.say(text)
    engine.runAndWait()
