from fastapi import HTTPException, APIRouter, Response, status, Form
from db.database import db

router = APIRouter()

@router.post("/session/verify")
def session_verify(verification_key:str = Form(...)):
    raise HTTPException(status_code=204)

