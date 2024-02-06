from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v2")

from . import me
from . import friends
from . import notifications
from . import session
from . import seasonal_backgrounds
from . import chat
from . import users

api_router.include_router(me.router)
api_router.include_router(friends.router)
api_router.include_router(notifications.router)
api_router.include_router(session.router)
api_router.include_router(seasonal_backgrounds.router)
api_router.include_router(chat.router)
api_router.include_router(users.router)