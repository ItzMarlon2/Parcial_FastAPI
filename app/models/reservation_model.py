from app.config.config import Base
from sqlalchemy import Column, Integer, Date, String, ForeignKey
from sqlalchemy.orm import relationship

class ReservationORM(Base):
    __tablename__= 'Reservations'
    
    id = Column(Integer, primary_key=True, index=True)
    reservation_code = Column(String, unique=True)
    date= Column(Date)
    client_id = Column(Integer, ForeignKey("Clients.id"))
    client = relationship("ClientORM", back_populates="reservations")