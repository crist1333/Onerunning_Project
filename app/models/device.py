from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    provider = Column(String, nullable=False)
    user_id = Column(String, nullable=False)
