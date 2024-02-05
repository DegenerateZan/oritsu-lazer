from fastapi import APIRouter

router = APIRouter()

# Used to show the bottom image on the main menu.
@router.get("/lazer-status.json")
def assetsroute() -> dict:
    return {
        "image": "https://assets.ppy.sh/main-menu/community-choice-2023@2x.png",
        "url": "https://osu.ppy.sh/home/news/2024-01-29-community-choice-2023-open"
    }