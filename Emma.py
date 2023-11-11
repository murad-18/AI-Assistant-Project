from Body.Listen import MicExecution
from Brain.AIBrain import ReplyBrain
from Body.Speak import Speak


def MainExecution():
    Speak("Hello Sir")
    Speak("I'm Emma, I'm Ready To Assist You Sir.")

    while True:
        data = MicExecution()
        data = str(data)

        # Check if the word "bye" is in the user's input
        if "bye" or "BYE" in data:
            Speak("Goodbye Sir, have a great day!")
            break  # Exit the loop to terminate the program

        reply = ReplyBrain(data)
        Speak(reply)


MainExecution()
