# 🌤️ Weather App – AI/ML Internship Project

## 📋 Project Overview

This Weather App enables users to:

* 🔍 Fetch real-time weather for any location (city, zip code, or landmark)
* 💾 Automatically save fetched weather to a database
* ⚡ Perform basic CRUD operations on stored weather records
* 📊 View saved records instantly on the frontend

### 🛠️ Tech Stack
- Python
- FastAPI
- SQLAlchemy (SQLite)
- OpenWeatherMap API
- Jinja2 templates

## 📥 Requirements

- Python 3.9+
- pip package manager
- OpenWeatherMap API key

### Installation

```bash
pip install -r requirements.txt
```

Configure your API key in `config.py`:
```python
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
```

> 📝 Note: SQLite database (weather.db) is automatically created on first run.

## 🚀 Running the App

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

- 🌐 Server URL: http://127.0.0.1:8000
- 📚 Swagger UI (API docs): http://127.0.0.1:8000/docs

## 🔌 API Endpoints

### 1️⃣ Home Page
- **URL**: `/`
- **Method**: GET
- **Description**: Loads the HTML page with the weather form
```bash
curl http://127.0.0.1:8000/
```

### 2️⃣ Fetch Current Weather
- **URL**: `/weather`
- **Method**: GET
- **Parameters**:
  - `location`: city name, zip code, or landmark
  - `save`: true to save the record (optional)

```bash
curl "http://127.0.0.1:8000/weather?location=Kampala&save=true"
```

#### Sample Response:
```json
{
  "weather": {
    "location": "Kampala",
    "temperature": 28.5,
    "humidity": 70,
    "description": "clear sky"
  },
  "saved": {
    "id": 1,
    "location": "Kampala",
    "date": "2025-10-27",
    "temperature": 28.5,
    "humidity": 70,
    "description": "clear sky"
  }
}
```

### 3️⃣ Save Weather Record
- **URL**: `/weather_record`
- **Method**: POST
- **Parameter**: `location`

```bash
curl -X POST "http://127.0.0.1:8000/weather_record?location=Kampala"
```

### 4️⃣ List All Stored Records
- **URL**: `/weather_records`
- **Method**: GET

```bash
curl http://127.0.0.1:8000/weather_records
```

## 💻 Database Management

### CLI Access
```bash
sqlite3 weather.db
```

### Useful Commands
```sql
.tables                 -- list all tables
.schema weather        -- show table structure
.headers on           -- display column headers
.mode column          -- pretty-print output
SELECT * FROM weather; -- show all records
.exit                 -- exit SQLite CLI
```

> ⚠️ **Important**: Always backup before using UPDATE or DELETE operations.

## 🖥️ Frontend Usage

1. Enter a location in the input field
2. Click "Get & Save Weather"
3. View weather info and automatic database save
4. Browse saved records below (refreshable)

---
*Made with ❤️ during AI/ML Internship*