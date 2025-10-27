# Database models (tables) using SQLAlchemy

from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class WeatherRecord(Base):
    __tablename__ = "weather"
    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    date = Column(Date)
    temperature = Column(Float)
    humidity = Column(Float)
    description = Column(String)
