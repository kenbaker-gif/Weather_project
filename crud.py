# CRUD functions for the WeatherRecord table

from models import WeatherRecord

# Create a new record
def create_weather_record(session, location, record_date, temp, humidity, desc):
    new_record = WeatherRecord(location=location, date=record_date,
                               temperature=temp, humidity=humidity, description=desc)
    session.add(new_record)
    session.commit()
    return new_record

# Read all records
def read_weather_records(session):
    return session.query(WeatherRecord).all()

# Update a record by id
def update_weather_record(session, record_id, **kwargs):
    record = session.query(WeatherRecord).filter(WeatherRecord.id == record_id).first()
    for key, value in kwargs.items():
        setattr(record, key, value)
    session.commit()
    return record

# Delete a record by id
def delete_weather_record(session, record_id):
    record = session.query(WeatherRecord).filter(WeatherRecord.id == record_id).first()
    session.delete(record)
    session.commit()
