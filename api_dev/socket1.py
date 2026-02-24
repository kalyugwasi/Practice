import asyncio
import websockets
import json

MAX_MESSAGE_SIZE = 1024 * 32  # 32KB
ALLOWED_TYPES = {"auth", "message", "ping"}
SECRET_TOKEN = "supersecret"

def validate_schema(payload):
    # Must be dictionary
    if not isinstance(payload, dict):
        return False, "Payload must be JSON object"

    # Required keys
    if "type" not in payload or "data" not in payload:
        return False, "Missing required keys"

    # Type validation
    if payload["type"] not in ALLOWED_TYPES:
        return False, "Invalid message type"

    # Data must be dict
    if not isinstance(payload["data"], dict):
        return False, "Data must be object"

    return True, None


async def register_client(websocket):
    print("Client connected")
    authenticated = False

    try:
        async for message in websocket:

            # Size check
            if len(message) > MAX_MESSAGE_SIZE:
                await websocket.close(code=1009)
                return

            # JSON validation
            try:
                payload = json.loads(message)
            except json.JSONDecodeError:
                await websocket.close(code=1003)
                return

            # Schema validation
            valid, error = validate_schema(payload)
            if not valid:
                await websocket.send(json.dumps({"error": error}))
                continue

            # AUTH HANDSHAKE (Phase 2 will extend this)
            if payload["type"] == "auth":
                token = payload["data"].get("token")
                if token == SECRET_TOKEN:
                    authenticated = True
                    await websocket.send(json.dumps({"status": "authenticated"}))
                else:
                    await websocket.close(code=1008)
                    return

            elif not authenticated:
                await websocket.send(json.dumps({"error": "Not authenticated"}))

            elif payload["type"] == "message":
                text = payload["data"].get("text", "")
                await websocket.send(json.dumps({"echo": text}))

            elif payload["type"] == "ping":
                await websocket.send(json.dumps({"type": "pong"}))

    except Exception:
        print("Client disconnected")


async def main():
    async with websockets.serve(
        register_client,
        "0.0.0.0",
        1111,
        max_size=MAX_MESSAGE_SIZE
    ):
        print("Secure server running...")
        await asyncio.Future()

asyncio.run(main())