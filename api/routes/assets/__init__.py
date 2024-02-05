# Route Configuration
from fastapi import APIRouter
assets_router = APIRouter()

# Subroute Configuration
from . import lazer_status
assets_router.include_router(lazer_status.router)