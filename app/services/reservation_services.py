from sqlalchemy.orm import Session
from app.repositories.reservations_repository import create_reservation, delete_reservation, get_all_reservations
from app.schemas.reservations_schemas import ReservationRequest

def get_all_reservations_service(db:Session):
    return get_all_reservations(db)

def create_reservation_service(db:Session, reser:ReservationRequest):
    return create_reservation(reser, db)

def delete_reservation_service(uid:int, db:Session):
    return delete_reservation(uid, db)