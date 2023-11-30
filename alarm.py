import pyttsx3
import datetime
import os

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


extractedtime = open("DataBase\\alarm.txt", "rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("DataBase\\alarm.txt", "r+")
deletetime.truncate(0)
deletetime.close()


def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis", "")
    timenow = timenow.replace("set an alarm", "")
    timenow = timenow.replace(" and ", ":")
    Alarmtime = str(timenow)
    print(Alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing,sir")
            os.startfile("music.mp3")
        elif currenttime + "00:00:30" == Alarmtime:
            exit()


ring(time)
