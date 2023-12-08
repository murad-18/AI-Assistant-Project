import speech_recognition as sr
import eel


def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)  # Listening Mode.....

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
    except:
        return ""

    query = str(query).lower()
    return query


@eel.expose
def takecommand():
    query = Listen()  # Assuming Listen is a valid function
    print(query)
    return query
    eel.DispalyMessage(query)
    eel.ShowHood()
