from fastapi import APIRouter

router = APIRouter(prefix='/api/2')

@router.post("/envelope")
def updates() -> dict:
    return {}