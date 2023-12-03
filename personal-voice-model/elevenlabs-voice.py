# import elevenlabs


# audio = elevenlabs.generate(
#     text="""Hello, my name is Bella. How may I assist you.
#      It's very hot today... I guess, would u like some juice?""",
#     voice="Bella"
# )
# elevenlabs.play(audio)
# 68f959ba9e9822d9c6ad5f92b584bec4
from pydub.playback import play
from pydub import AudioSegment
import requests
import io

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": "68f959ba9e9822d9c6ad5f92b584bec4"
}

data = {
    "text": """ Born and raised in the charming south,
  I can add a touch of sweet southern hospitality
  to your audiobooks and podcasts """,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.75
    }
}
response = requests.post(url, json=data, headers=headers)
audio = AudioSegment.from_file(io.BytesIO(response.content), format="mp3")
play(audio)
