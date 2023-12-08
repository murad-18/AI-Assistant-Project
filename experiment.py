# # import json
# # import requests
# # from bs4 import BeautifulSoup
# # import subprocess
# # import wikipedia.exceptions
# # import webbrowser
# # import speech_recognition as sr
# # import pyttsx3
# # import pywhatkit
# # import wikipedia
# # import datetime
# # import os
# # import pyautogui
# # from pynput.keyboard import Key, Controller
# # import random
# # from time import sleep
# # from datetime import timedelta
# # from plyer import notification
# # from pygame import mixer


# # keyboard = Controller()


# # def translategl(query):
# #     speak("SURE SIR")
# #     print(googletrans.LANGUAGES)
# #     translator = Translator()
# #     speak("Choose the language in which you want to translate")
# #     b = input("To_Lang :- ")
# #     text_to_translate = translator.translate(query, src="auto", dest=b,)
# #     text = text_to_translate.text
# #     try:
# #         speakgl = gTTS(text=text, lang=b, slow=False)
# #         speakgl.save("voice.mp3")
# #         playsound("voice.mp3")

# #         time.sleep(5)
# #         os.remove("voice.mp3")
# #     except:
# #         print("Unable to translate")


# # def volumeup():
# #     for i in range(5):
# #         keyboard.press(Key.media_volume_up)
# #         keyboard.release(Key.media_volume_up)
# #         sleep(0.1)


# # def volumedown():
# #     for i in range(5):
# #         keyboard.press(Key.media_volume_down)
# #         keyboard.release(Key.media_volume_down)
# #         sleep(0.1)


# # # engine = pyttsx3.init("sapi5")
# # # voices = engine.getProperty("voices")
# # # engine.setProperty("voice", voices[0].id)
# # # engine.setProperty("rate", 200)


# # def alarm(query):
# #     timehere = open("Alarmtext.txt", "a")
# #     timehere.write(query)
# #     timehere.close()
# #     os.startfile("alarm.py")


# # # def speak(audio):
# # #     engine.say(audio)
# # #     engine.runAndWait()


# # def alarm(query):
# #     timehere = open("Alarmtext.txt", "a")
# #     timehere.write(query)
# #     timehere.close()
# #     os.startfile("alarm.py")


# # dictapp = {"commandprompt": "cmd", "paint": "paint", "word": "winword",
# #            "excel": "excel", "chrome": "chrome", "vscode": "code", "powerpoint": "powerpnt", "spotify": "spotify"}


# # def openappweb(query):
# #     speak("Launching, sir")
# #     if ".com" in query or ".co.in" in query or ".org" in query:
# #         query = query.replace("open", "")
# #         query = query.replace("Emma", "")
# #         query = query.replace("launch", "")
# #         query = query.replace(" ", "")
# #         webbrowser.open(f"https://www.{query}")
# #     else:
# #         keys = list(dictapp.keys())
# #         for app in keys:
# #             if app in query:
# #                 os.system(f"start {dictapp[app]}")


# # def closeappweb(query):
# #     speak("Closing,sir")
# #     if "one tab" in query or "1 tab" in query:
# #         pyautogui.hotkey("ctrl", "w")
# #         speak("All tabs closed")
# #     elif "2 tab" in query:
# #         pyautogui.hotkey("ctrl", "w")
# #         sleep(0.5)
# #         pyautogui.hotkey("ctrl", "w")
# #         speak("All tabs closed")
# #     elif "3 tab" in query:
# #         pyautogui.hotkey("ctrl", "w")
# #         sleep(0.5)
# #         pyautogui.hotkey("ctrl", "w")
# #         sleep(0.5)
# #         pyautogui.hotkey("ctrl", "w")
# #         speak("All tabs closed")

# #     elif "4 tab" in query:
# #         pyautogui.hotkey("ctrl", "w")
# #         sleep(0.5)
# #         pyautogui.hotkey("ctrl", "w")
# #         sleep(0.5)
# #         pyautogui.hotkey("ctrl", "w")
# #         sleep(0.5)
# #         pyautogui.hotkey("ctrl", "w")
# #         speak("All tabs closed")
# #     elif "5 tab" in query:
# #         pyautogui.hotkey("ctrl", "w")
# #         sleep(0.5)
# #         pyautogui.hotkey("ctrl", "w")
# #         sleep(0.5)
# #         pyautogui.hotkey("ctrl", "w")
# #         sleep(0.5)
# #         pyautogui.hotkey("ctrl", "w")
# #         sleep(0.5)
# #         pyautogui.hotkey("ctrl", "w")
# #         speak("All tabs closed")

# #     else:
# #         keys = list(dictapp.keys())
# #         for app in keys:
# #             if app in query:
# #                 os.system(f"taskkill /f /im {dictapp[app]}.exe")


# # def get_current_time():
# #     current_time = datetime.datetime.now().strftime("%I:%M %p")
# #     speak(f"Sir, the time is {current_time}")


# # def speak(text):
# #     engine = pyttsx3.init()
# #     voices = engine.getProperty('voices')
# #     voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# #     engine.setProperty("voice", voice_id)
# #     engine.say(text=text)
# #     engine.runAndWait()


# # def takecommand():
# #     r = sr.Recognizer()

# #     with sr.Microphone() as source:
# #         print("Listening...")
# #         r.pause_threshold = 1
# #         audio = r.listen(source, 0, 8)  # Listening Mode.....

# #     try:
# #         print("Recognizing...")
# #         query = r.recognize_google(audio, language="en")
# #     except:
# #         return ""

# #     query = str(query).lower()
# #     return query


# # def searchGoogle(query):
# #     if "google" in query:
# #         import wikipedia as googleScrap
# #         query = query.replace("Emma", "")
# #         query = query.replace("google search", "")
# #         query = query.replace("google", "")
# #         speak("This is what I found on Google")

# #         try:
# #             pywhatkit.search(query)
# #             result = googleScrap.summary(query, 2)
# #             speak(result)

# #         except:
# #             speak("No speakable output available")


# # # def get_weather(city: str, query_type: str):
# # #     search = f"{query_type} in {city}"
# # #     url = f"https://www.google.com/search?q={search}"
# # #     r  = requests.get(url)
# # #     data = BeautifulSoup(r.text,"html.parser")
# # #     result = data.find("div", class_ = "BNeawe").text
# # #     speak(f"current {search} is {result}")

# # # city = input("Enter the city: ")
# # # query_type = input("Enter the query type (temperature or weather): ")
# # # get_weather(city, query_type)


# # def latestnews():
# #     api_dict = {
# #         "business": "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=4a70461e98544daba33eb124e1699b08",
# #         "entertainment": "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=4a70461e98544daba33eb124e1699b08",
# #         "health": "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=4a70461e98544daba33eb124e1699b08",
# #         "science": "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=4a70461e98544daba33eb124e1699b08",
# #         "sports": "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=4a70461e98544daba33eb124e1699b08",
# #         "technology": "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=4a70461e98544daba33eb124e1699b08"
# #     }

# #     content = None
# #     url = None
# #     speak(
# #         "Which field news do you want, [business], [health], [technology], [sports], [entertainment], [science]")
# #     field = input("Type the field of news that you want: ")

# #     for key, value in api_dict.items():
# #         if key.lower() in field.lower():
# #             url = f'https://newsapi.org/v2/top-headlines?apiKey=4a70461e98544daba33eb124e1699b08&category={key.lower()}'
# #             print(url)
# #             print("URL was found")
# #             break
# #     else:
# #         url = None
# #         print("URL not found")

# #     if url:
# #         news = requests.get(url).text
# #         news = json.loads(news)
# #         speak("Here is the first news.")

# #         arts = news["articles"]
# #         for articles in arts:
# #             article = articles["title"]
# #             print(article)
# #             speak(article)
# #             news_url = articles["url"]
# #             print(f"For more info visit: {news_url}")

# #             a = input("[Press 1 to continue] and [Press 2 to stop]")
# #             if str(a) == "1":
# #                 pass
# #             elif str(a) == "2":
# #                 break

# #         speak("That's all")


# # def get_weather(city: str, query_type: str):
# #     search = f"{query_type} in {city}"
# #     url = f"https://www.google.com/search?q={search}"
# #     r = requests.get(url)
# #     data = BeautifulSoup(r.text, "html.parser")
# #     result = data.find("div", class_="BNeawe").text
# #     speak(f"Current {search} is {result}")


# # def spotify_pause():
# #     pyautogui.press("space")  # Assuming "space" pauses the music in Spotify
# #     speak("music paused")


# # def spotify_play():
# #     pyautogui.press("space")  # Assuming "space" plays the music in Spotify
# #     speak("music played")


# # def searchYoutube(query):
# #     if "youtube" in query:
# #         speak("This is what I found for your search!")
# #         query = query.replace("youtube search", "")
# #         query = query.replace("youtube", "")
# #         query = query.replace("Emma", "")
# #         web = "https://www.youtube.com/results?search_query=" + query

# #         # Use subprocess to open the URL
# #         subprocess.Popen(["start", "chrome", web], shell=True)

# #         pywhatkit.playonyt(query)
# #         speak("Done, Sir")


# # def searchWikipedia(query):
# #     if "wikipedia" in query:
# #         speak("Searching from wikipedia....")
# #         query = query.replace("wikipedia", "")
# #         query = query.replace("search wikipedia", "")
# #         query = query.replace("Emma", "")
# #         Results = wikipedia.summary(query, sentences=2)
# #         speak("According to wikipedia..")
# #         print(Results)
# #         speak(Results)


# # def game_play():
# #     speak("Lets Play ROCK PAPER SCISSORS !!")
# #     print("LETS PLAYYYYYYYYYYYYYY")
# #     i = 0
# #     Me_score = 0
# #     Com_score = 0
# #     while (i < 5):
# #         choose = ("rock", "paper", "scissors")  # Tuple
# #         com_choose = random.choice(choose)
# #         query = takeCommand().lower()
# #         if (query == "rock"):
# #             if (com_choose == "rock"):
# #                 speak("ROCK")
# #                 print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
# #             elif (com_choose == "paper"):
# #                 speak("paper")
# #                 Com_score += 1
# #                 print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
# #             else:
# #                 speak("Scissors")
# #                 Me_score += 1
# #                 print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

# #         elif (query == "paper"):
# #             if (com_choose == "rock"):
# #                 speak("ROCK")
# #                 Me_score += 1
# #                 print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

# #             elif (com_choose == "paper"):
# #                 speak("paper")
# #                 print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
# #             else:
# #                 speak("Scissors")
# #                 Com_score += 1
# #                 print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

# #         elif (query == "scissors" or query == "scissor"):
# #             if (com_choose == "rock"):
# #                 speak("ROCK")
# #                 Com_score += 1
# #                 print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
# #             elif (com_choose == "paper"):
# #                 speak("paper")
# #                 Me_score += 1
# #                 print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
# #             else:
# #                 speak("Scissors")
# #                 print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
# #         i += 1

# #     print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}")


# # def main():
# #     speak("Hello! I am Emma. How can I assist you today?")

# #     while True:
# #         query = takecommand()

# #         if "exit" in query:
# #             speak("Goodbye! Have a great day.")
# #             break

# #         if "google" in query:
# #             searchGoogle(query)
# #         elif "youtube" in query:
# #             searchYoutube(query)
# #         elif "wikipedia" in query:
# #             searchWikipedia(query)
# #         elif "temperature" in query or "weather" in query:
# #             speak("Sure, which city would you like to know the information about?")
# #             city_query = takecommand().lower()
# #             query_type = "temperature" if "temperature" in query else "weather"
# #             get_weather(city_query, query_type)
# #         elif "time" in query:
# #             get_current_time()
# #         elif "open" in query:
# #             openappweb(query)
# #         elif "close" in query:
# #             closeappweb(query)
# #         elif "set an alarm" in query:
# #             print("input time example:- 10 and 10 and 10")
# #             speak("Set the time")
# #             a = input("Please tell the time :- ")
# #             alarm(a)
# #             speak("Done, sir")
# #         elif "volume up" in query:
# #             speak("Turning volume up, sir")
# #             volumeup()
# #         elif "volume down" in query:
# #             speak("Turning volume down, sir")
# #             volumedown()
# #         elif "pause" in query:
# #             pyautogui.press("k")
# #             speak("video paused")
# #         elif "play" in query:
# #             pyautogui.press("k")
# #             speak("video played")
# #         elif "mute" in query:
# #             pyautogui.press("m")
# #             speak("video muted")
# #         elif "pause spotify" in query:
# #             spotify_pause()
# #         elif "play spotify" in query:
# #             spotify_play()
# #         elif "music" in query:
# #             speak("Playing your favorite songs, sir")
# #             a = (1, 2, 3)
# #             b = random.choice(a)
# #             if b == 1:
# #                 webbrowser.open(
# #                     "https://youtu.be/gIo9vL9I928?si=6aDGHCuCIbMh3MCm")
# #             if b == 2:
# #                 webbrowser.open(
# #                     "https://youtu.be/J4nvbKBuEBU?si=OvL0ClJpVXBKkiQj")
# #             if b == 3:
# #                 webbrowser.open(
# #                     "https://youtu.be/K86IxKir8do?si=DOtDHWrQcaEv_N1L")
# #         elif "news" in query:
# #             latestnews()
# #         elif "shutdown system" in query:
# #             speak("Are You sure you want to shutdown")
# #             shutdown = input("Do you wish to shutdown your computer? (yes/no)")
# #             if shutdown == "yes":
# #                 os.system("shutdown /s /t 1")
# #             elif shutdown == "no":
# #                 break
# #         elif "schedule my day" in query:
# #             tasks = []  # Empty list
# #             speak("Do you want to clear old tasks (Plz speak YES or NO)")
# #             query = takeCommand().lower()
# #             if "yes" in query:
# #                 file = open("DataBase\\task.txt", "w")
# #                 file.write(f"")
# #                 file.close()
# #                 no_tasks = int(input("Enter the no. of tasks :- "))
# #                 i = 0
# #                 for i in range(no_tasks):
# #                     tasks.append(input("Enter the task :- "))
# #                     file = open("DataBase\\task.txt", "a")
# #                     file.write(f"{i}. {tasks[i]}\n")
# #                     file.close()
# #             elif "no" in query:
# #                 i = 0
# #                 no_tasks = int(input("Enter the no. of tasks :- "))
# #                 for i in range(no_tasks):
# #                     tasks.append(input("Enter the task :- "))
# #                     file = open("DataBase\\task.txt", "a")
# #                     file.write(f"{i}. {tasks[i]}\n")
# #                     file.close()

# #         elif "show my schedule" in query:
# #             file = open("DataBase\\task.txt", "r")
# #             content = file.read()
# #             file.close()
# #             mixer.init()
# #             mixer.music.load("notification.mp3")
# #             mixer.music.play()
# #             notification.notify(
# #                 title="My schedule :-",
# #                 message=content,
# #                 timeout=15)
# #         elif "open" in query:
# #             query = query.replace("open", "")
# #             query = query.replace("jarvis", "")
# #             pyautogui.press("super")
# #             pyautogui.typewrite(query)
# #             pyautogui.sleep(2)
# #             pyautogui.press("enter")

# #         elif "play a game" in query:
# #             game_play()
# #         elif "screenshot" in query:
# #             import pyautogui  # pip install pyautogui
# #             im = pyautogui.screenshot()
# #             im.save("ss.jpg")

# #         elif "click my photo" in query:
# #             pyautogui.press("super")
# #             pyautogui.typewrite("camera")
# #             pyautogui.press("enter")
# #             pyautogui.sleep(2)
# #             speak("SMILE")
# #             pyautogui.press("enter")
# #         elif "translate" in query:
# #             from Translator import translategl
# #             query = query.replace("jarvis", "")
# #             query = query.replace("translate", "")
# #             translategl(query)


# # if __name__ == "__main__":
# #     main()


# # if __name__ == "__main__":
# #     # Your main code here

# import os
# import pygame


# def playAssistantSound():
#     # Specify the path to the audio file
#     music_dir = r'DataBase\Startup2.mp3'

#     # Initialize Pygame mixer
#     pygame.mixer.init()

#     # Load the music file
#     pygame.mixer.music.load(music_dir)

#     # Play the music in the background
#     pygame.mixer.music.play()

#     # Wait for the music to finish
#     # Adjust the time or use an event loop for a dynamic solution
#     pygame.time.wait(5000)

#     # Stop the music
#     pygame.mixer.music.stop()


# # Check if the script is being run as the main program
# if __name__ == "__main__":
#     # Call the playAssistantSound function when the script is run
#     playAssistantSound()
