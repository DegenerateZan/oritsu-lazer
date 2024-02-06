from fastapi import APIRouter, Response, WebSocket

router = APIRouter()

@router.websocket("/notify")
def handle_websocket(websocket: WebSocket):
    websocket.accept()
    while True:
        data = websocket.receive_text()
        # Process the received data here
        websocket.send_text("Message received: " + data)
