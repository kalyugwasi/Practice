import asyncio
import websockets
import json

EC2_PUBLIC_IP = "65.2.79.193"
PORT = 1111
SECRET_TOKEN = "supersecret"

async def test_connection():
    uri = f"ws://{EC2_PUBLIC_IP}:{PORT}"

    async with websockets.connect(uri) as websocket:
        print("Connected")

        # Step 1 — Authenticate
        auth_payload = {
            "type": "auth",
            "data": {"token": SECRET_TOKEN}
        }

        await websocket.send(json.dumps(auth_payload))
        response = await websocket.recv()
        print("Auth response:", response)

        # Step 2 — Send message
        message_payload = {
            "type": "message",
            "data": {"text": "Hello secure world"}
        }

        await websocket.send(json.dumps(message_payload))
        response = await websocket.recv()
        print("Message response:", response)

asyncio.run(test_connection())