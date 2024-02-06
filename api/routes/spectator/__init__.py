# Route Configuration
from fastapi import APIRouter
spectator_router = APIRouter()

# Subroute Configuration
from . import negotiate
spectator_router.include_router(negotiate.router)