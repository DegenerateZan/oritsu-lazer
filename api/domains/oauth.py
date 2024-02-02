from fastapi import APIRouter, HTTPException, Depends, Security
from db.database import db
from api.objects.User import User
from helpers.REGEX import USERNAME, EMAIL
import secrets
from datetime import datetime
import argon2

oauth_route = APIRouter(prefix="/oauth")

# I dont know the register endpoint, so I'll do without for now
@oauth_route.post("/register")
def register(username:str, password:str, email:str) -> dict:
    
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
    token = secrets.token_urlsafe(100)
    refresh_token = secrets.token_urlsafe(100)

    # Hash password with argon2
    hasher = argon2.PasswordHasher(time_cost=2, memory_cost=50000, parallelism=2, hash_len=64, salt_len=16, encoding="utf-8")
    pw_argon2 = hasher.hash(password)

    # Insert user into the database
    db.execute("INSERT INTO users (name, safe_name, email, country, argon2_pw) VALUES (%s, %s, %s, %s, %s)", (username, username.lower(), email, "XX", pw_argon2))

    # Get the user_id
    user_id_query_result = db.fetch_one("SELECT user_id FROM users WHERE safe_name = %s", (username.lower(),))

    if user_id_query_result is None:
        # Handle the case when no user_id is found for the given username
        raise HTTPException(status_code=400, detail="user_not_found")

    user_id = user_id_query_result[0]

    # Insert token into the database
    db.execute("INSERT INTO tokens (token, refresh_token, created_at, user_id) VALUES (%s, %s, %s, %s)", (token, refresh_token, datetime.now(), user_id))

    # Raise user_registered with the tokens
    raise HTTPException(status_code=200, detail="user_registered", headers={"token": token, "refresh_token": refresh_token})

@oauth_route.post("/auto_login")
def auto_login(token:str) -> dict:
    user = db.fetch_one("SELECT user_id FROM tokens WHERE token = %s", (token,))

    if not user or user is None:
        raise HTTPException(status_code=400, detail="invalid_token")

    refresh_token_req = db.fetch_one("SELECT refresh_token FROM tokens WHERE user_id = %s", (user[0],))
    refresh_token = refresh_token_req[0] if refresh_token_req is not None else None

    if not user:
        raise HTTPException(status_code=400, detail="invalid_token")
    return {
        "access_token": token,
        "refresh_token": refresh_token,
        "token_type": "Bearer"
    }

@oauth_route.post("/token")
def token(username:str, password:str) -> dict:

    # Check if the user exists
    if not User.user_exists(username):
        raise HTTPException(status_code=400, detail="invalid_credentials")

    # Get the argon2 hash from the database
    argon2_pw_result = db.fetch_one("SELECT argon2_pw FROM users WHERE safe_name = %s", (username.lower(),))

    # Check if the user has a password
    if argon2_pw_result is None:
        raise HTTPException(status_code=400, detail="no_password_set")

    argon2_pw = argon2_pw_result[0]

    # Ensure that argon2_pw is of type str
    if not isinstance(argon2_pw, str):
        raise HTTPException(status_code=500, detail="invalid_hash_format")

    # Compare the password with the hash
    try:
        argon2.PasswordHasher().verify(argon2_pw, password)
    except Exception as e:
        raise HTTPException(status_code=400, detail="invalid_credentials")
    
    access_token = db.fetch_one("SELECT token FROM tokens WHERE user_id = (SELECT user_id FROM users WHERE safe_name = %s)", (username.lower(),))
    refresh_token = db.fetch_one("SELECT refresh_token FROM tokens WHERE user_id = (SELECT user_id FROM users WHERE safe_name = %s)", (username.lower(),))

    if access_token is None or refresh_token is None:
        raise HTTPException(status_code=400, detail="no_token")
    
    return {
        "access_token": access_token[0],
        "refresh_token": refresh_token[0],
        "token_type": "Bearer"
    }