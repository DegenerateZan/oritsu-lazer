from fastapi import HTTPException, APIRouter, Response, status, WebSocket
from db.database import db

router = APIRouter()

@router.post("/metadata/negotiate")
def metadata_negotiate():
    return {
        "availableTransports": [
            {
                "transferFormats": [
                    "Text",
                    "Binary"
                ],
                "transport": "WebSockets"
            },
            {
                "transferFormats": [
                    "Text"
                ],
                "transport": "ServerSentEvents"
            },
            {
                "transferFormats": [
                    "Text",
                    "Binary"
                ],
                "transport": "LongPolling"
            }
        ],
        "connectionId": "XTzWrNjBGBjaFG-s5OdGfQ",
        "connectionToken": "HApG1mtYX1f2Pkt6a4aRAQ",
        "negotiateVersion": 1
    }

@router.get("/metadata")
@router.post("/metadata")
def metadata(resp: Response):
    resp.status_code = status.HTTP_204_NO_CONTENT
    return

@router.delete("/metadata")
def metadata_del(resp: Response):
    resp.status_code = status.HTTP_202_ACCEPTED
    return

@router.websocket("/metadata")
async def metadata_ws(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_bytes()
        # Process the binary data here as needed
        print(data)
        # Return empty bytes to acknowledge receipt
        await websocket.send_bytes(b"")


@router.post("/spectator/negotiate")
def spectator_negotiate():
    return {
        "availableTransports": [
            {
                "transferFormats": [
                    "Text",
                    "Binary"
                ],
                "transport": "WebSockets"
            },
            {
                "transferFormats": [
                    "Text"
                ],
                "transport": "ServerSentEvents"
            },
            {
                "transferFormats": [
                    "Text",
                    "Binary"
                ],
                "transport": "LongPolling"
            }
        ],
        "connectionId": "XTzWrNaFG-s5OdGfQ",
        "connectionToken": "HApG1mtYt6a4aRAQ",
        "negotiateVersion": 1
    }

@router.get("/spectator")
@router.post("/spectator")
def spectator(resp: Response):
    resp.status_code = status.HTTP_204_NO_CONTENT
    return

@router.delete("/spectator")
def spectator_del(resp: Response):
    resp.status_code = status.HTTP_202_ACCEPTED
    return

@router.websocket("/spectator")
async def spectator_ws(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_bytes()
        # Process the binary data here as needed
        print(data)
        await websocket.send_bytes(b"")

@router.post("/multiplayer/negotiate")
def multiplayer_negotiate():
    return {
        "availableTransports": [
            {
                "transferFormats": [
                    "Text",
                    "Binary"
                ],
                "transport": "WebSockets"
            },
            {
                "transferFormats": [
                    "Text"
                ],
                "transport": "ServerSentEvents"
            },
            {
                "transferFormats": [
                    "Text",
                    "Binary"
                ],
                "transport": "LongPolling"
            }
        ],
        "connectionId": "XTNjBGBjaFG-s5OdGfQ",
        "connectionToken": "H1mtYX1f2Pkt6a4aRAQ",
        "negotiateVersion": 1
    }

@router.get("/multiplayer")
@router.post("/multiplayer")
def multiplayer(resp: Response):
    resp.status_code = status.HTTP_204_NO_CONTENT
    return

@router.delete("/multiplayer")
def multiplayer_del(resp: Response):
    resp.status_code = status.HTTP_202_ACCEPTED
    return

@router.websocket("/multiplayer")
async def multiplayer_ws(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_bytes()
        # Process the binary data here as needed
        print(data)
        await websocket.send_bytes(b"")