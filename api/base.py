from fastapi import FastAPI
from api.domains.osu.oauth import oauth_route
from api.domains.sentry import sentry_route
from api.domains.assets import assets_route

app = FastAPI()

app.include_router(oauth_route)
app.include_router(sentry_route)
app.include_router(assets_route)