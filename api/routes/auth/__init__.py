# Route Configuration
from fastapi import APIRouter
auth_router = APIRouter()

# Subroute Configuration
from . import updates
auth_router.include_router(updates.router)