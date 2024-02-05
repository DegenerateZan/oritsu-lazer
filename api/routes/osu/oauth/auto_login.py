from fastapi import HTTPException, APIRouter
from db.database import db

router = APIRouter()

@router.post("/auto_login")
def auto_login(token:str) -> dict:
    user = db.fetch_one("SELECT user_id FROM tokens WHERE token = %s", (token,))

    if not user or user is None:
        raise HTTPException(status_code=400, detail="invalid_token")

    refresh_token_req = db.fetch_one("SELECT refresh_token FROM tokens WHERE user_id = %s", (user[0],))
    refresh_token = refresh_token_req[0] if refresh_token_req is not None else None

    if not user:
        raise HTTPException(status_code=400, detail="invalid_token")
    return {
        "access_token": token,
        "refresh_token": refresh_token,
        "token_type": "Bearer"
    }