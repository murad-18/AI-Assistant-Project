import elevenlabs


audio = elevenlabs.generate(
    text="""Hello, my name is Bella. How may I assist you.
     It's very hot today... I guess, would u like some juice?""",
    voice="Bella"
)
elevenlabs.play(audio)
