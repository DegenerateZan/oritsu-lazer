from fastapi import HTTPException, APIRouter, Response, status
from db.database import db

router = APIRouter()

@router.get("/seasonal-backgrounds")
def notifications(resp: Response):
    resp.status_code = status.HTTP_200_OK
    return {}