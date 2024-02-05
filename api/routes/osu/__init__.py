from fastapi import APIRouter
from .oauth import oauth_router
from .api import api_router

# Create the route
osu_router = APIRouter(tags=["osu.ppy.sh route"])
osu_router.include_router(oauth_router)
osu_router.include_router(api_router)
