from fastapi import HTTPException, APIRouter, Response, status
from db.database import db
import websockets

router = APIRouter()

@router.get("/notifications")
def notifications(resp: Response):
    resp.status_code = status.HTTP_200_OK
    return {
        "notification_endpoint": "wss://notify.ppy.sh/notify",
        "notifications": [],
    }

@router.websocket("/ws")
async def websocket_endpoint(websocket, path):
    # Send 200 OK
    await websocket.send("HTTP/1.1 200 OK\r\n\r\n")
    while True:
        data = await websocket.recv()
        await websocket.send(f"You said: {data}")