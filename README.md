# Weather App – AI/ML Internship Project
## Project Overview

This Weather App allows users to:

- Fetch real-time weather for any location (city, zip code, or landmark)

- Store weather data in a database

- Perform basic CRUD operations (Create, Read, Update, Delete) on stored weather records

Tech Stack: Python, FastAPI, SQLAlchemy (SQLite), OpenWeatherMap API

Requirements

- Python 3.9+

- pip package manager

- OpenWeatherMap API key

Install dependencies:

* pip install -r requirements.txt


* Set your API key in config.py:

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"


SQLite database (weather.db) is automatically created on first run.

Running the App

- Start the FastAPI server:

- uvicorn main:app --reload


Server URL: http://127.0.0.1:8000

Swagger UI (interactive API docs): http://127.0.0.1:8000/docs

### API Endpoints
1️⃣ Home

URL: /
Method: GET
Description: Welcome message

curl http://127.0.0.1:8000/


### Response:

{"message": "Welcome to the Weather API!"}

2️⃣ Fetch Current Weather

### URL: /weather
Method: GET
Query Parameter: location = city name, zip code, or landmark

curl "http://127.0.0.1:8000/weather?location=Kampala"


### Sample Response:

{
  "location": "Kampala",

  "temperature": 28.5,

  "humidity": 70,
  
  "description": "clear sky"
}

3️⃣ Save Weather Record

URL: /weather_record
Method: POST
Query Parameter: location = city name, zip code, or landmark

curl -X POST "http://127.0.0.1:8000/weather_record?location=Kampala"


### Sample Response:

{
  "id": 1,

  "location": "Kampala",

  "date": "2025-10-27",

  "temperature": 28.5,

  "humidity": 70,

  "description": "clear sky"
}

4️⃣ List All Stored Records

URL: /weather_records
Method: GET

curl http://127.0.0.1:8000/weather_records


### Sample Response:

[
  {
    "id": 1,

    "location": "Kampala",

    "date": "2025-10-27",

    "temperature": 28.5,

    "humidity": 70,

    "description": "clear sky"
  }
]

### Inspect Database via CLI

- Open terminal in project folder:

- sqlite3 weather.db


### Basic commands:

.tables                 -- list all tables 

.schema weather         -- show table structure

.headers on             -- display column headers 

.mode column            -- pretty-print output

SELECT * FROM weather;  -- show all records

.exit                   -- exit SQLite CLI 


Note: Make a backup before using UPDATE or DELETE.