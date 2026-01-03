from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class WeatherRecord(Base):
    __tablename__ = "weather_records"
    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    # Change Date to DateTime
    date = Column(DateTime, default=datetime.utcnow) 
    temperature = Column(Float)
    humidity = Column(Integer)
    description = Column(String)