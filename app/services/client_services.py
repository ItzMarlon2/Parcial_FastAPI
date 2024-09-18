from sqlalchemy.orm import Session
from app.repositories.client_repository import (create_client, delete_client, get_all_clients,
    get_client_by_email_repository)
from app.schemas.client_schemas import ClientRequest

def get_all_clients_service(db:Session):
    return get_all_clients(db)

def create_client_service(db:Session, client:ClientRequest):
    return create_client(client, db)

def delete_client_service(uid:int, db:Session):
    return delete_client(uid, db)

async def get_client_by_email(db: Session, email: str):
    return get_client_by_email_repository(db, email)