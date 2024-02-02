from fastapi import APIRouter, HTTPException, Depends, Security
from db.database import db
from api.objects.User import User
from helpers.REGEX import USERNAME, EMAIL
import secrets

oauth_route = APIRouter(prefix="/oauth")

# I dont know the register endpoint, so I'll do without for now
@oauth_route.post("/register")
def register(username:str, password:str, email:str):
    
    # Check username & email validity
    if User.user_exists(username):
        raise HTTPException(status_code=400, detail="username_exists")
    
    if User.email_exists(email):
        raise HTTPException(status_code=400, detail="email_exists")
    
    # Regex
    if not USERNAME.match(username):
        raise HTTPException(status_code=400, detail="username_invalid")
        
    if not EMAIL.match(email):
        raise HTTPException(status_code=400, detail="email_invalid")
    
    # Generate OAUTH token
    token = secrets.token_urlsafe(128)
    refresh_token = secrets.token_urlsafe(128)

    # Raise user_registered with the tokens
    raise HTTPException(status_code=200, detail="user_registered", headers={"token": token, "refresh_token": refresh_token})


@oauth_route.post("/token")
def token(username:str, password:str, grant_type:str, scope:str, client_id:str, client_secret:str):

    if grant_type != "password":
        return {"error": "unsupported_grant_type"}
    
    # Check if user exists.
    user = db.fetch_one("SELECT * FROM users WHERE name = %s", (username,))
    if not user:
        return {"error": "invalid_user"}
    
    # Check if hashed password is correct.
    if user[2] != password:
        return {"error": "invalid_password"}

    # Generate token
    # token =
    return {"access_token": token, "token_type": "bearer", "expires_in": 3600, "scope": scope}