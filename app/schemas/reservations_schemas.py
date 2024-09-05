from pydantic import BaseModel, Field, EmailStr
from datetime import date


class ReservationRequest(BaseModel):
    
    reservation_code: str
    date: date
    client_id: int
    
    
class ReservationDTO(BaseModel):
    id: int
    reservation_code: str
    date: date
    client_id: int
    
    class Config:
        orm_mode = True