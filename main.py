
import json
from fastapi import FastAPI, WebSocket
from fastapi import WebSocketDisconnect
from ai.llm import generate_npc_response
from ai.scorer import score_conversion

app = FastAPI()

@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:

            user_input = await websocket.receive_text()

            npc_reply = generate_npc_response(user_input)

            scores = score_conversion(user_input, npc_reply) 

            await websocket.send_text(
                json.dumps({
                    "npc_reply": npc_reply,
                    "scores": scores
                })
            )
    except WebSocketDisconnect:
        print("Client disconnected")