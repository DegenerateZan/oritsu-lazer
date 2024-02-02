from fastapi import FastAPI
from api.domains.oauth import oauth_route

app = FastAPI()

app.include_router(oauth_route)