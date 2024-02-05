from fastapi import APIRouter

router = APIRouter(prefix='/updates')

# Used to show the bottom image on the main menu.
@router.post("/get")
def updates() -> dict:
    return {
        "url": None
    }