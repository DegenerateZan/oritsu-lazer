from api.objects.User import User
from fastapi import HTTPException, APIRouter, Form
from db.database import db
import argon2

router = APIRouter()

@router.post("/token")
def token(username: str = Form(...), 
          password: str = Form(...), 
          grant_type: str = Form(...), 
          client_id: int = Form(...), 
          client_secret: str = Form(...), 
          scope: str = Form(...)) -> dict:

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