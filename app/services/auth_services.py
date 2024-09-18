from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.config.config import get_db
from app.services.security import ALGORITHM, SECRET_KEY
from app.repositories.client_repository import get_client_by_email_repository

async def get_current_client(token: str, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email : str = payload.get('sub')
        if email is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    
    client = get_client_by_email_repository(db, email)
    
    if client is None:
            raise HTTPException(status_code=401, detail="Client not found")
    
    return client
        