# Route Configuration
from fastapi import APIRouter
notify_router = APIRouter()

# Subroute Configuration
from . import notify
notify_router.include_router(notify.router)