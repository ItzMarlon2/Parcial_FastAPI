from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.client_schemas import ClientDTO, ClientRequest
from sqlalchemy.orm import Session
from typing import List
from app.config.config import get_db
from app.services.client_services import (create_client_service, delete_client_service,
    get_all_clients_service, get_client_by_email)
from app.services.auth_services import get_current_client
from app.services.security import create_access_token, verify_password

router = APIRouter()

@router.get('/clients', response_model=List[ClientDTO])
def get_clients(db:Session = Depends(get_db)):
    clients=get_all_clients_service(db)
    if not clients:
        raise HTTPException(status_code=404, detail="NO HAY CLIENTES")
    return clients

@router.post('/clients', response_model=ClientDTO)
def create_client(client:ClientRequest, db:Session = Depends(get_db)):
    create_client = create_client_service(client, db)
    if not create_client:
        raise HTTPException(status_code=404, detail="NO SE HA PODIDO CREAR EL CLIENTE")
    return create_client

@router.delete('clients/{uid}', response_model=dict)
def delete_client(uid:int, db:Session = Depends(get_db)):
    success = delete_client_service(uid, db)
    print(success)
    if not success:
        raise HTTPException(status_code=404, detail="CLIENTE NO ENCONTRADO")
    return {"detail": "Cliente Eliminado Correctamente"}

@router.get("/me", response_model=ClientDTO)
async def read_client_me(current_client : ClientDTO = Depends(get_current_client)):
    return current_client

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db:Session=Depends(get_db)):
    client= await get_client_by_email(db, form_data.username)
    if not client or not verify_password(form_data.password, client.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": client.email})
    return {"access_token": access_token, "token_type": "bearer"}