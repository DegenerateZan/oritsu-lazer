from fastapi import APIRouter, HTTPException

sentry_route = APIRouter(prefix="/api/2")

# Return nothing for now
@sentry_route.post("/envelope")
def envelope() -> dict:
    raise HTTPException(status_code=200)