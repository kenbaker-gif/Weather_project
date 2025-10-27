# Main FastAPI app
# Connects API calls with CRUD and database

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from crud import create_weather_record, read_weather_records
from database import Base, engine, get_db
from utils import get_weather
from datetime import date

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(title="Weather App")

# Simple GET endpoint to fetch current weather
@app.get("/weather")
def weather_endpoint(location: str):
    return get_weather(location)

# POST endpoint to save weather record
@app.post("/weather_record")
def add_weather_record(location: str, db: Session = Depends(get_db)):
    weather = get_weather(location)
    if "error" in weather:
        return {"error": "Location not found"}
    return create_weather_record(db, location, date.today(),
                                 weather["temperature"], weather["humidity"], weather["description"])

# GET endpoint to read all records
@app.get("/weather_records")
def list_weather_records(db: Session = Depends(get_db)):
    return read_weather_records(db)

@app.get("/")
def home():
    return {"message": "Welcome to the Weather API!"}
