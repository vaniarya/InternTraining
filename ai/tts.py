import edge_tts

async def text_to_speech(
    text,
    output_file
):
    communicate = edge_tts.Communicate(
        text=text,
        voice="en-US-JennyNeural"
    )

    await communicate.save(
        output_file
    )