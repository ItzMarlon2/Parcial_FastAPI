from app.services.auth_services import get_current_client
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.reservations_schemas import ReservationDTO, ReservationRequest
from app.services.reservation_services import (create_reservation_service,
    delete_reservation_service, get_all_reservations_service)
from sqlalchemy.orm import Session
from typing import List
from app.config.config import get_db
from app.schemas.client_schemas import ClientDTO

router = APIRouter()

@router.get('/reservations', response_model=List[ReservationDTO])
def get_reservations(db:Session = Depends(get_db)):
    resers = get_all_reservations_service(db)
    if not resers:
        raise HTTPException(status_code=404, detail="NO HAY RESERVACIONES")
    return resers

@router.post('/reservations', response_model=ReservationDTO)
def create_reservation(reser:ReservationRequest, db:Session = Depends(get_db), current_client: ClientDTO = Depends(get_current_client)):
    create_reservation = create_reservation_service(reser, db, current_client.id)
    if not create_reservation:
        raise HTTPException(status_code=404, detail="NO SE HA PODIDO CREAR LA RESERVACIÓN")
    return create_reservation

@router.delete('reservations/{uid}', response_model=dict)
def delete_reservation(uid:int, db:Session = Depends(get_db)):
    success = delete_reservation_service(uid, db)
    if not success:
        raise HTTPException(status_code=404, detail="RESERVACIÓN NO ENCONTRADA")
    return {"detail": "Reservación Eliminada Correctamente"}