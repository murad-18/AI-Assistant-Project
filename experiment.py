from speak import speak, speak2
from alarm import callAlarm
import json
from word2number import w2n
import elevenlabs
import requests
from bs4 import BeautifulSoup
import subprocess
import wikipedia.exceptions
import webbrowser
import pywhatkit
import wikipedia
import speech_recognition as sr
from pydub.playback import play
from pydub import AudioSegment
import io
import os
import pyautogui
import pyttsx3
from time import sleep
import datetime
from pynput.keyboard import Key, Controller
import random

keyboard = Controller()


def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)


def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)


dictapp = {"commandprompt": "cmd", "paint": "paint", "word": "winword",
           "excel": "excel", "chrome": "chrome", "vscode": "code", "powerpoint": "powerpnt", "spotify": "spotify"}


def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("Emma", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")


def close_tabs(query):
    # Try to extract a spoken number first
    try:
        spoken_number = ''.join(
            filter(lambda x: x.isalpha() or x.isspace(), query))
        number = w2n.word_to_num(spoken_number)
    except ValueError:
        pass

    # If spoken number extraction fails, try to extract numeric digits
    try:
        numeric_digits = int(''.join(filter(str.isdigit, query)))
        number = numeric_digits
    except ValueError:
        print("No valid spoken number found in the query.")
    # Close tabs based on the extracted number
    for _ in range(number):
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
    # Speak the result
    speak("All tabs closed")


# close_tabs("close twenty tabs")


def closeappweb(query):
    speak("Closing,sir")
    keys = list(dictapp.keys())
    for app in keys:
        if app in query:
            os.system(f"taskkill /f /im {dictapp[app]}.exe")
            break
        else:
            close_tabs(query)
            break


def get_current_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"Sir, the time is {current_time}")


def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
    except:
        return ""

    query = str(query).lower()
    print("You Said :", query)
    return query


def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = replaceWords(query)
        speak("This is what I found on Google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 2)
            speak(result)

        except:
            speak("Sorry Sir, No speakable output available")


def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4a70461e98544daba33eb124e1699b08",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=4a70461e98544daba33eb124e1699b08",
        "health": "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=4a70461e98544daba33eb124e1699b08",
        "science": "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=4a70461e98544daba33eb124e1699b08",
        "sports": "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=4a70461e98544daba33eb124e1699b08",
        "technology": "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=4a70461e98544daba33eb124e1699b08"
    }

    content = None
    url = None
    speak(
        "Which field news do you want, [business], [health], [technology], [sports], [entertainment], [science]")
    field = input("Type the field of news that you want: ")

    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = f'https://newsapi.org/v2/top-headlines?apiKey=4a70461e98544daba33eb124e1699b08&category={key.lower()}'
            print(url)
            print("URL was found")
            break
    else:
        url = None
        print("URL not found")

    if url:
        news = requests.get(url).text
        news = json.loads(news)
        speak("Here is the first news.")

        arts = news["articles"]
        for articles in arts:
            article = articles["title"]
            print(article)
            speak(article)
            news_url = articles["url"]
            print(f"For more info visit: {news_url}")

            a = input("[Press 1 to continue] and [Press 2 to stop]")
            if str(a) == "1":
                pass
            elif str(a) == "2":
                break

        speak("That's all")


def translateText(text):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    speak("To which language")
    if "urdu" in text:
        payload = {
            "q": "Hello, world!",
            "target": "ur",
            "source": "en"
        }
    elif "german" or "duetch" in text:
        payload = {
            "q": "Hello, world!",
            "target": "ur",
            "source": "en"
        }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "application/gzip",
        "X-RapidAPI-Key": "3129d9460bmsh5e467d04a6888cap13f4fcjsn7c3ce3b8431a",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)
    data = response.json()['data']
    translatedText = data['translations'][0]['translatedText']
    # print(translatedText.sort(ascending=False))
    return translatedText


def get_weather(city: str, query_type: str):
    search = f"{query_type} in {city}"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    result = data.find("div", class_="BNeawe").text
    speak(f"Current {search} is {result}")


def spotify_pause():
    pyautogui.press("space")  # Assuming "space" pauses the music in Spotify
    speak("music paused")


def spotify_play():
    pyautogui.press("space")  # Assuming "space" plays the music in Spotify
    speak("music played")


def replaceWords(query):
    replaceable = ["Emma", "emma", "youtube search", "google search", "wikipedia search",
                   "Open", "open youtube", "open google", "open wikipedia", "search on youtube", "search on google", "search on wikipedia", "youtube", "google", "wikipedia", "and search", "search"]
    for word in replaceable:
        query = query.replace(word, "")
    return query


def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found for your search!")
        query = replaceWords(query)
        print(query)
        try:
            web = "https://www.youtube.com/results?search_query=" + query
            subprocess.Popen(["start", "chrome", web], shell=True)
            # pywhatkit.playonyt(query)
            speak("Here is your search, Sir")
        except:
            speak("Sorry Sir, No searchable output found!")


def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        replaceWords(query)
        Results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia..")
        print(Results)
        speak(Results)


def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hello! Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Hello! Good Afternoon, Sir")
    else:
        speak("Hello! Good Evening, Sir")

    speak("Please tell me how can I assist you today?")


def main():
    # greet()
    queries = ["google", "youtube", "wikipedia", "temperature", "time", ]
    while True:
        query = takecommand()
        if "exit all" in query:
            speak("Goodbye Sir, I am shutting down, have a good day")
            break
        elif "wake up" in query:
            greet()
            while True:
                query = takecommand()

                if "exit" in query:
                    speak("Goodbye Sir, you can call me anytime later")
                    break
                elif "google" in query:
                    searchGoogle(query)
                elif "youtube" in query:
                    searchYoutube(query)
                elif "wikipedia" in query:
                    searchWikipedia(query)
                elif "temperature" in query or "weather" in query:
                    speak(
                        "Sure, which city would you like to know the information about?")
                    city_query = takecommand().lower()
                    query_type = "temperature" if "temperature" in query else "weather"
                    get_weather(city_query, query_type)
                elif "time" in query:
                    get_current_time()
                elif "open" in query:
                    openappweb(query)
                elif "close" in query:
                    closeappweb(query)
                elif "set an alarm" in query:
                    speak(
                        "Kindly provide me the time, for example you can say : set an alarm for 7:29 PM")
                    callAlarm()
                elif "volume up" in query:
                    speak("Turning volume up, sir")
                    volumeup()
                elif "volume down" in query:
                    speak("Turning volume down, sir")
                    volumedown()
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "pause spotify" in query:
                    spotify_pause()
                elif "play spotify" in query:
                    spotify_play()
                elif "music" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1, 2, 3)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open(
                            "https://youtu.be/gIo9vL9I928?si=6aDGHCuCIbMh3MCm")
                    if b == 2:
                        webbrowser.open(
                            "https://youtu.be/J4nvbKBuEBU?si=OvL0ClJpVXBKkiQj")
                    if b == 3:
                        webbrowser.open(
                            "https://youtu.be/K86IxKir8do?si=DOtDHWrQcaEv_N1L")
                elif "news" in query:
                    latestnews()


if __name__ == "__main__":
    main()
