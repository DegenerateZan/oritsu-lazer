# Route Configuration
from fastapi import APIRouter
sentry_router = APIRouter()

# Subroute Configuration
from . import sentry
sentry_router.include_router(sentry.router)