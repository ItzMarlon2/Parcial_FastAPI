from app.models.client_model import ClientORM
from app.models.reservation_model import ReservationORM
from typing import List
from sqlalchemy.orm import Session
from app.schemas.client_schemas import ClientRequest
from fastapi import HTTPException


def get_all_clients(db:Session) -> List[ClientORM]:
    return db.query(ClientORM).all()

def create_client(db:Session, client:ClientRequest)->ClientORM:
    
    existing_client=db.query(ClientORM).filter(
        (ClientORM.phone_number == client.phone_number) |
        (ClientORM.email == client.email)
    ).first()
    
    if existing_client:
        conflict_field = 'número de teléfono' if existing_client.phone_number == client.phone_number else 'correo electrónico'
        raise HTTPException(status_code=400, detail=f"Ya existe un cliente con ese {conflict_field}.")

    
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
    
    reservation = db.query(ReservationORM).filter(ReservationORM.client_id== client.id).first()
    if reservation is not None:
        raise HTTPException(status_code=400, detail=f"No se puede eliminar el cliente porque tiene reservaciones asociadas. ID de reservación: {reservation.id}")
    
    db.delete(client)
    db.commit()
    return True