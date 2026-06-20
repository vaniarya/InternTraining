import streamlit as st
import asyncio
import websockets
import json
import tempfile

from streamlit_mic_recorder import mic_recorder

from ai.stt import transcribe_audio
from ai.tts import text_to_speech


async def send_message(message):

    async with websockets.connect(
        "ws://localhost:8000/ws/chat"
    ) as ws:

        await ws.send(message)

        response = await ws.recv()

        return json.loads(response)


st.set_page_config(
    page_title="Sales Training NPC",
    layout="wide"
)

st.title("Sales Training NPC")

if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])


st.subheader("Voice Input")

audio = mic_recorder(
    start_prompt="🎤 Start Recording",
    stop_prompt="⏹ Stop Recording",
    key="mic"
)

user_message = None


if audio:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    ) as temp_audio:

        temp_audio.write(audio["bytes"])
        audio_path = temp_audio.name

    with st.spinner("Transcribing..."):

        user_message = transcribe_audio(
            audio_path
        )

    st.success(
        f"You said: {user_message}"
    )


typed_message = st.chat_input(
    "Talk to the shopkeeper"
)

if typed_message:
    user_message = typed_message


if user_message:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    with st.chat_message("user"):
        st.write(user_message)

    with st.spinner("NPC is thinking..."):

        data = asyncio.run(
            send_message(user_message)
        )

    npc_reply = data["npc_reply"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": npc_reply
        }
    )

    with st.chat_message("assistant"):
        st.write(npc_reply)

    audio_file = "npc_response.mp3"

    asyncio.run(
        text_to_speech(
            npc_reply,
            audio_file
        )
    )

    import base64

    with open(audio_file, "rb") as f:
        audio_bytes = f.read()

    audio_base64 = base64.b64encode(audio_bytes).decode()

    st.markdown(
        f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Scores")
    st.json(data["scores"])

