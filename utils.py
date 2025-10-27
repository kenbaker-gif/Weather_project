# Utility functions (API calls, input validation)

import requests
from config import API_KEY

# Fetch weather from OpenWeatherMap API
def get_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "location": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
    else:
        return {"error": "Location not found"}
