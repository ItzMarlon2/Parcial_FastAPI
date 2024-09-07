from app.config.config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class ClientORM(Base):
    __tablename__= 'Clients'
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    phone_number = Column(String, unique=True)
    email = Column(String, unique=True)
    reservations = relationship("ReservationORM", back_populates="client")
    

