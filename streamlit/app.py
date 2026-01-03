import streamlit as st
from datetime import datetime
import pytz
import sys
from pathlib import Path

# --- Path Management ---
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
models.Base.metadata.create_all(bind=engine)

# Configure Timezone for Uganda
local_tz = pytz.timezone("Africa/Kampala")

# Fetch API Key from Streamlit Secrets
API_KEY = st.secrets["API_KEY"]

st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️")
st.title("🌤️ Weather Dashboard")

# --- Input Section ---
location = st.text_input("Enter city:", placeholder="e.g. London, Nairobi, Kampala")

# --- Get Weather Logic ---
if st.button("Get Weather"):
    if location:
        weather = get_weather(location, API_KEY)
        
        if "error" in weather:
            st.error(f"Error: {weather.get('message', 'Location not found')}")
        else:
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
        
        # Capture current time in Uganda (EAT)
        now_uganda = datetime.now(local_tz)
        
        db = SessionLocal()
        try:
            record = create_weather_record(
                db,
                loc_name,
                now_uganda, 
                weather["temperature"],
                weather["humidity"],
                weather["description"]
            )
            st.success(f"✅ Saved to Supabase at {now_uganda.strftime('%I:%M %p')} EAT")
        except Exception as e:
            st.error(f"Failed to save: {e}")
        finally:
            db.close()

# --- Historical Data Section (Cleaned & Single Version) ---
st.divider()
if st.checkbox("Show Search History from Database"):
    db = SessionLocal()
    try:
        records = read_weather_records(db)
        if records:
            data = []
            utc_tz = pytz.utc
            uganda_tz = pytz.timezone("Africa/Kampala")

            for r in records:
                # 1. Localize the database time as UTC
                if r.date.tzinfo is None:
                    utc_dt = utc_tz.localize(r.date)
                else:
                    utc_dt = r.date

                # 2. Convert to Kampala time (EAT)
                uganda_dt = utc_dt.astimezone(uganda_tz)
                
                # 3. Format for display
                formatted_time = uganda_dt.strftime("%d %b, %Y | %I:%M %p")
                
                data.append({
                    "Location": r.location, 
                    "Time (EAT)": formatted_time, 
                    "Temp (°C)": r.temperature, 
                    "Humidity (%)": r.humidity, 
                    "Description": r.description.capitalize()
                })
            
            # Newest records at the top
            data.reverse() 
            st.dataframe(data, use_container_width=True)
        else:
            st.info("No records found in the database yet.")
    except Exception as e:
        st.error(f"Could not fetch records: {e}")
    finally:
        db.close()