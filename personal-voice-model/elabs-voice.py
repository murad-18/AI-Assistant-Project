import elevenlabs
audio = elevenlabs.generate(
    text="Welcome to ElevenLabs!, I am Adam", voice="Adam")

elevenlabs.play(audio)
