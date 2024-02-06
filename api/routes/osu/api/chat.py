from fastapi import HTTPException, APIRouter, Response, status

router = APIRouter()

@router.post("/chat/ack")
def chat_ack(resp: Response):
    resp.status_code = status.HTTP_200_OK
    return {
        "silences": []
    }

@router.get("/chat/updates")
def chat_updates(resp: Response):
    resp.status_code = status.HTTP_200_OK
    return {
        "presence": [],
    }

@router.get("/chat/channels")
def chat_channels(resp: Response):
    resp.status_code = status.HTTP_200_OK
    return []