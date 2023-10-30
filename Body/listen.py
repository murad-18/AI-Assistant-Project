# Urdu or English - Command
# Jarvis will reply in English
import speech_recognition as sr
from googletrans import Translator
# Listen function
def listen():
    mcrphn = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening. . .")
        mcrphn.pause_threshold = 1
        audio = mcrphn.listen(source, 0, 9) #Listening.....
        # mcrphn.adjust_for_ambient_noise(source, duration=3)
        # audio = mcrphn.listen(source)

    try:
        print("Recognizing. . .")
        query = mcrphn.recognize_google(audio, language="ur")
        # print("Query:", query)
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""
    
    query = str(query).lower()
    return query

# Translating function
def translateUrduToEng(text):
    line = str(text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}." )
    return data

# connecting function
def micConnection():
    input = listen()
    output = translateUrduToEng(input)
    return output

micConnection()
