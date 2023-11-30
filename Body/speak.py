# # Speak Functions - Two Speak Functions

# # Windows Based - pip install pyttsx3
# # Chrome Based - pip install selenium==4.1.3

# # Windows Based
# # Advantages = Fast , Offline.
# # Disadvantages =  OverSpeak , Less Voices.
# import pyttsx3


# def Speak(Text):
#     engine = pyttsx3.init("sapi5")
#     voices = engine.getProperty('voices')
#     engine.setProperty('voices', voices[1].id)
#     engine.setProperty('rate', 170)
#     print("")
#     print(f"You : {Text}.")
#     print("")
#     engine.say(Text)
#     engine.runAndWait()
import pyttsx3


def Speak(text):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

    # Set the voice to the specified ID
    engine.setProperty("voice", voice_id)

    # Speak the text
    engine.say(text=text)

    # Wait until the speech is finished
    engine.runAndWait()
