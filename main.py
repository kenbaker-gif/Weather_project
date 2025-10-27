from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from crud import create_weather_record, read_weather_records
from database import Base, engine, get_db
from utils import get_weather
from datetime import date

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Weather App")

# Serve static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve templates
templates = Jinja2Templates(directory="templates")

# HTML home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API: Get weather (optionally save)
@app.get("/weather")
def weather_endpoint(location: str, save: bool = False, db: Session = Depends(get_db)):
    """
    Fetch current weather.
    If save=True, store it in the database.
    """
    weather = get_weather(location)
    if "error" in weather:
        return {"error": "Location not found"}

    if save:
        record = create_weather_record(
            db, location, date.today(),
            weather["temperature"], weather["humidity"], weather["description"]
        )
        return {"weather": weather, "saved": record}

    return weather

# API: Save record (optional, still works)
@app.post("/weather_record")
def add_weather_record(location: str, db: Session = Depends(get_db)):
    weather = get_weather(location)
    if "error" in weather:
        return {"error": "Location not found"}
    return create_weather_record(
        db, location, date.today(),
        weather["temperature"], weather["humidity"], weather["description"]
    )

# API: List records
@app.get("/weather_records")
def list_weather_records(db: Session = Depends(get_db)):
    return read_weather_records(db)
