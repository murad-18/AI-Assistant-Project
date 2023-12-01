import elevenlabs
audio = elevenlabs.generate(
    text="Welcome to ElevenLabs!, I am Adam, How may I assist you sir?", voice="Adam")

elevenlabs.play(audio)
