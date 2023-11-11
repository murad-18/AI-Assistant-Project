from Body.Listen import MicExecution
from Brain.AIBrain import ReplyBrain
from Body.Speak import Speak


def MainExecution():
    Speak("Hello Sir")
    Speak("I'm Emma, I'm Ready To Assist You Sir.")

    while True:
        data = MicExecution()
        data = str(data)
        reply = ReplyBrain(data)
        Speak(reply)


MainExecution()
