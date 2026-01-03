from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from crud import create_weather_record, read_weather_records
from utils import get_weather
from datetime import date

# Create tables if not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Weather App")

# Static files + templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/weather")
def weather_endpoint(location: str, save: bool = False, db: Session = Depends(get_db)):
    weather = get_weather(location)
    if "error" in weather:
        return {"error": "Location not found"}
    if save:
        record = create_weather_record(
            db, location, date.today(),
            weather["temperature"], weather["humidity"], weather["description"]
        )
        return {"weather": weather, "saved": {"id": record.id}}
    return weather

@app.get("/weather_records")
def list_weather_records(db: Session = Depends(get_db)):
    records = read_weather_records(db)
    return [{"id": r.id, "location": r.location, "date": str(r.date),
             "temp": r.temperature, "humidity": r.humidity,
             "desc": r.description} for r in records]
