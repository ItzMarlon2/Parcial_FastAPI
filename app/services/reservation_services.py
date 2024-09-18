from sqlalchemy.orm import Session
from app.repositories.reservations_repository import create_reservation, delete_reservation, get_all_reservations, get_reservation_by_client
from app.schemas.reservations_schemas import ReservationRequest

def get_all_reservations_service(db:Session):
    return get_all_reservations(db)

def get_reservation_by_client_service(db:Session, client_id:int):
    return get_reservation_by_client(db, client_id)

def create_reservation_service(db:Session, reser:ReservationRequest, client_id: int):
    return create_reservation(reser, db, client_id)

def delete_reservation_service(uid:int, db:Session):
    return delete_reservation(uid, db)