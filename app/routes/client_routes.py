from fastapi import APIRouter, HTTPException, Depends
from app.schemas.client_schemas import ClientDTO, ClientRequest
from sqlalchemy.orm import Session
from typing import List
from app.config.config import get_db
from app.services.client_services import (create_client_service, delete_client_service,
    get_all_clients_service)


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
            
