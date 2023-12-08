# import os
# import eel
# eel.init("frontend")
# os.system("start chrome.exe --app=\"http://localhost:8000/index.html\"")

# eel.start("index.html", mode=None, host="localhost", block=True)
import os
import eel
from Body.Listen import MicExecution
from Brain.AIBrain import ReplyBrain
from Body.Speak import Speak
import datetime
import wikipedia
import pygame


def playAssistantSound():
    music_dir = r'DataBase\Startup2.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        Speak("Good Morning!")
    elif 12 <= hour < 18:
        Speak("Good Afternoon!")
    else:
        Speak("Good Evening!")
    Speak("I'm Emma, I'm Ready To Assist You Sir.. What can I do for you?")


def MainExecution():
    # Initialize the Eel application
    eel.init("frontend")

    # Open the webpage
    os.system("start msedge.exe --app=\"http://localhost:8000/index.html\"")

    # Play the sound
    playAssistantSound()

    # Greet the user
    Speak("Hello Sir")
    wishMe()

    # Start the Eel application
    eel.start("index.html", mode=None, host="localhost", block=False)

    # Start listening for commands
    while True:
        data = MicExecution()
        data = str(data).lower()
        if len(data) < 3:
            continue
        if "bye" in data.lower():
            Speak("Goodbye Sir, have a great day!")
            break
        reply = ReplyBrain(data)
        Speak(reply)


if __name__ == "__main__":
    MainExecution()
