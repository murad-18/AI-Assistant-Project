
import pyttsx3


def speak(text):
    engine = pyttsx3.init("sapi5")  # api to use windows voice
    voices = engine.getProperty("voices")
    engine.setProperty("voices", voices[0].id)
    engine.setProperty("rate", 170)
    print("")
    print(f"You : {text}.")
    engine.say(text)
    engine.runAndWait()


speak("I ask you till what end, dread it, run from it, destiny arives all the same")
