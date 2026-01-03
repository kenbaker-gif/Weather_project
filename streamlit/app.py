import streamlit as st
from datetime import date
import os
import sys
from pathlib import Path

# This finds the absolute path to the 'Weather_project' root
file_path = Path(__file__).resolve()
project_root = file_path.parent.parent  # Goes up to the folder containing crud.py
sys.path.append(str(project_root))

# Now your original import will work
from crud import create_weather_record, read_weather_records
from database import SessionLocal  # use direct session instead of get_db()
from utils.utils import get_weather
import streamlit as st
API_KEY = st.secrets["API_KEY"]

st.title("Weather Dashboard")

# --- Input ---
location = st.text_input("Enter city:")

# --- Get Weather ---
if st.button("Get Weather"):
    weather = get_weather(location)
    if "error" in weather:
        st.error("Location not found")
    else:
        # store in session state to persist across reruns
        st.session_state["weather"] = weather
        st.write(f"Temperature: {weather['temperature']}°C")
        st.write(f"Humidity: {weather['humidity']}%")
        st.write(f"Description: {weather['description']}")

# --- Save to Database ---
if "weather" in st.session_state:
    if st.button("Save to Database"):
        weather = st.session_state["weather"]
        db = SessionLocal()  # direct session
        record = create_weather_record(
            db,
            location,
            date.today(),
            weather["temperature"],
            weather["humidity"],
            weather["description"]
        )
        db.close()
        st.success(f"Weather saved with ID {record.id}")

# --- Show all records ---
if st.checkbox("Show all records"):
    db = SessionLocal()
    records = read_weather_records(db)
    db.close()
    st.write(records)
