from models import WeatherRecord
from sqlalchemy.orm import Session

def create_weather_record(session: Session, location, record_date, temp, humidity, desc):
    new_record = WeatherRecord(
        location=location,
        date=record_date,
        temperature=temp,
        humidity=humidity,
        description=desc
    )
    session.add(new_record)
    session.commit()             # ✅ must commit
    session.refresh(new_record)   # get ID
    return new_record

def read_weather_records(session: Session):
    return session.query(WeatherRecord).all()
