from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v2")


from . import me

api_router.include_router(me.router)