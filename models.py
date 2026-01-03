from sqlalchemy import Column, Integer, String, Float, Date
from database import Base

class WeatherRecord(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    description = Column(String, nullable=False)
