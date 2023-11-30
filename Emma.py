from Body.Listen import MicExecution
from Brain.AIBrain import ReplyBrain
from Body.Speak import Speak
import datetime
import wikipedia


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
    Speak("Hello Sir")
    wishMe()

    # Call the wishMe function to greet the user initially

    while True:
        data = MicExecution()
        data = str(data).lower()
        if len(data) < 3:
            continue  # Skip the rest of the loop if the input is too short

        # Check if the word "bye" is in the user's input
        if "bye" in data.lower():
            Speak("Goodbye Sir, have a great day!")
            break  # Exit the loop to terminate the program

        reply = ReplyBrain(data)
        Speak(reply)


if __name__ == "__main__":
    MainExecution()
