import os
import pygame
from pydub.playback import play
from pydub import AudioSegment
import requests
import io

enGirl = 'en-US-AnaNeural'
enWoman = 'en-US-JennyNeural'
urMan = 'ur-IN-GulNeural'
urWoman = 'ur-PK-UzmaNeural'
enWoman2 = 'en-US-AriaNeural'


def speak(text):
    command = f'edge-tts --voice "{enWoman2}" --text "{text}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


def speak2(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech/nPOpJH7NLSSmWNpboIMr"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "68f959ba9e9822d9c6ad5f92b584bec4"
    }
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "use_speaker_boost": False,
            "style": 0.5
        }
    }
    response = requests.post(url, json=data, headers=headers)
    audio = AudioSegment.from_file(io.BytesIO(response.content), format="mp3")
    play(audio)


speak2("My name is Emma, how are you?")
