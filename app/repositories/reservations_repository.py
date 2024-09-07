from app.models.client_model import ClientORM
from app.models.reservation_model import ReservationORM
from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from app.schemas.reservations_schemas import ReservationRequest
from fastapi import HTTPException



def get_all_reservations(db:Session)->List[ReservationORM]:
    return db.query(ReservationORM).all()

def create_reservation(db:Session, reser:ReservationRequest)->ReservationORM:
    existing_code = db.query(ReservationORM).filter(ReservationORM.reservation_code == reser.reservation_code).first()
    existing_cliente = db.query(ClientORM).filter(ClientORM.id == reser.client_id).first()
    active_reservations_count  = db.query(ReservationORM).filter(ReservationORM.client_id == reser.client_id).count()
    
    
    if existing_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado, no se puede crear la reserva.")
    
    if active_reservations_count  >= 5:
        raise HTTPException(status_code=400, detail="Se ha alcanzado el límite máximo de reservas por cliente (5 reservas activas).")
    
    if existing_code:
        raise HTTPException(status_code=400, detail=f"Ya existe una reservación con ese código: {existing_code.reservation_code}.")
    
    if reser.date < datetime.now().date():
        raise HTTPException(status_code=400, detail=f"La fecha de la reserva debe ser una fecha futura.")
    
    
        
    db_reser = ReservationORM(
        reservation_code= reser.reservation_code,
        date= reser.date,
        client_id= reser.client_id
    )
    db.add(db_reser)
    db.commit()
    db.refresh(db_reser)
    return db_reser

def delete_reservation(uid:int, db:Session)->bool:
    reser=db.query(ReservationORM).filter(ReservationORM.id == uid).first()
    
    if not reser:
        raise HTTPException(status_code=404, detail="Reservación no encontrada")
    db.delete(reser)
    db.commit()
    return True
    