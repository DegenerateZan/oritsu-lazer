from fastapi import APIRouter

oauth_router = APIRouter(prefix="/oauth")


from . import auto_login
from . import register
from . import token

oauth_router.include_router(auto_login.router)
oauth_router.include_router(register.router)
oauth_router.include_router(token.router)