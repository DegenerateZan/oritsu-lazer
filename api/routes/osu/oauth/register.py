from fastapi import HTTPException, APIRouter
from db.database import db
from api.objects.User import User
from helpers.REGEX import USERNAME, EMAIL
import secrets
from datetime import datetime
import argon2

router = APIRouter()

@router.post("/register")
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