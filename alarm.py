from word2number import w2n
import speech_recognition as sr
import re
import pyttsx3
import os
from datetime import datetime


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty("voice", voice_id)
    engine.say(text=text)
    engine.runAndWait()


def convert_text_to_digit(text):
    try:
        # Try to convert text to number using word2number library
        number = w2n.word_to_num(text)
        return str(number)
    except ValueError:
        # If conversion fails, assume it's already in digit form
        return text


def get_alarm_time():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
        return None
    query = str(query).lower()
    print("You Said :", query)
    return query


def write_alarm_time_to_file(time):
    with open("alarmtext.txt", "w") as file:
        file.write(time)


def parse_time_from_query(query):
    # Use regular expression to extract time and am/pm
    time_pattern = re.compile(r'(\d{1,2}):(\d{2})\s*([apAP][mM]?)')
    match = time_pattern.search(query)
    if match:
        hour, minute, period = match.groups()
        # print("Time period", period)
        # Convert to 24-hour format
        if (period.lower() == 'p' or period.lower() == 'pm') and int(hour) < 12:
            hour = str(int(hour) + 12)
        elif (period.lower() == 'a' or period.lower() == 'am') and int(hour) == 12:
            hour = '00'
        return f"{hour.zfill(2)}:{minute}"
    else:
        speak("Invalid time format. Please use a valid time format with AM/PM.")
        return None


def ring_alarm(alarm_time):
    # print("Alarm Time", alarm_time)
    speak(f"Alarm set for:{alarm_time}")

    while True:
        current_datetime = datetime.now().time()
        # print("Alarm Time:", alarm_time)
        # print("Current Time:", current_datetime)
        current_datetime = current_datetime.strftime("%H:%M")
        current_datetime = str(current_datetime)
        # print(current_datetime)
        if alarm_time >= current_datetime:
            if current_datetime == alarm_time:
                speak("Alarm ringing, sir")
                os.startfile("music.mp3")
                break
        elif alarm_time < current_datetime:
            speak("The alarm time is in the past. Exiting.")
            break


def callAlarm():
    # Get the alarm time from voice command
    alarm_query = get_alarm_time()
    alarm_time = parse_time_from_query(alarm_query)
    # Write the alarm time to the file
    write_alarm_time_to_file(alarm_time)
    # Ring the alarm
    ring_alarm(alarm_time)
# if __name__ == "__main__":
