from fastapi import APIRouter, Response

router = APIRouter(prefix='/api/2')

@router.post("/envelope/")
def updates(req: Response) -> dict:
    # Unsure
    req.status_code = 200
    return {}