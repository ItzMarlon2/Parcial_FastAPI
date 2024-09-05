from app.models.models import ClientORM
from typing import List
from sqlalchemy.orm import Session
from app.schemas.client_schemas import ClientRequest
from fastapi import HTTPException


def get_all_clients(db:Session) -> List[ClientORM]:
    return db.query(ClientORM).all()

def create_client(db:Session, client:ClientRequest)->ClientORM:
    db_client = ClientORM(
        full_name=client.full_name,
        phone_number= client.phone_number,
        email= client.email,
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def delete_client(uid:int, db:Session)->bool:
    client = db.query(ClientORM).filter(ClientORM.id == uid).first()
    if not client:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    db.delete(client)
    db.commit()
    return True