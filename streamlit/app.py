import streamlit as st
from datetime import date
import sys
from pathlib import Path

# --- Path Management ---
# This ensures that crud, database, and utils are findable by the Cloud environment
file_path = Path(__file__).resolve()
project_root = file_path.parent.parent 
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

# --- Imports ---
import models
from crud import create_weather_record, read_weather_records
from database import SessionLocal, engine
from utils.utils import get_weather

# --- Initialization ---
# This line creates the tables in Supabase if they don't exist yet
models.Base.metadata.create_all(bind=engine)

# Fetch API Key from Streamlit Secrets
API_KEY = st.secrets["API_KEY"]

st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️")
st.title("🌤️ Weather Dashboard")

# --- Input Section ---
location = st.text_input("Enter city:", placeholder="e.g. London, Nairobi, New York")

# --- Get Weather Logic ---
if st.button("Get Weather"):
    if location:
        # We pass the API_KEY directly into the utility function
        weather = get_weather(location, API_KEY)
        
        if "error" in weather:
            # Displays the actual error (e.g., "city not found" or "invalid api key")
            st.error(f"Error: {weather.get('message', 'Location not found')}")
        else:
            # Store in session state to persist across button clicks
            st.session_state["weather"] = weather
            st.session_state["current_location"] = location
            
            st.metric("Temperature", f"{weather['temperature']}°C")
            st.write(f"**Humidity:** {weather['humidity']}%")
            st.write(f"**Condition:** {weather['description'].capitalize()}")
    else:
        st.warning("Please enter a city name first.")

# --- Save to Database Section ---
if "weather" in st.session_state:
    st.divider()
    if st.button("Save this Result to Supabase"):
        weather = st.session_state["weather"]
        loc_name = st.session_state["current_location"]
        
        db = SessionLocal()
        try:
            record = create_weather_record(
                db,
                loc_name,
                date.today(),
                weather["temperature"],
                weather["humidity"],
                weather["description"]
            )
            st.success(f"✅ Saved to Supabase (ID: {record.id})")
        except Exception as e:
            st.error(f"Failed to save: {e}")
        finally:
            db.close()

# --- Historical Data Section ---
st.divider()
if st.checkbox("Show Search History from Database"):
    db = SessionLocal()
    try:
        records = read_weather_records(db)
        if records:
            # Convert SQLAlchemy objects to a list of dicts for a clean table
            data = [
                {
                    "ID": r.id, 
                    "Location": r.location, 
                    "Date": r.date, 
                    "Temp": r.temperature, 
                    "Humidity": r.humidity, 
                    "Desc": r.description
                } for r in records
            ]
            st.dataframe(data, use_container_width=True)
        else:
            st.info("No records found in the database yet.")
    except Exception as e:
        st.error(f"Could not fetch records: {e}")
    finally:
        db.close()