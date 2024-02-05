from fastapi import FastAPI
from . import routes

def init_routes(asgi_app: FastAPI) -> None:
    """Initialize endpoints"""

    asgi_app.host(f"osu.ppy.sh", routes.osu_router)
    asgi_app.host(f"assets.ppy.sh", routes.assets_router)
    asgi_app.host(f"auth.ppy.sh", routes.auth_router)
    asgi_app.host(f"sentry.ppy.sh", routes.sentry_router)