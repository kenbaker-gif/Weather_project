import requests

# We removed 'from config import API_KEY' 
# and added 'api_key' as a parameter to the function
def get_weather(location, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    try:
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
            # We return the actual error message from OpenWeather (e.g., "city not found")
            error_msg = response.json().get("message", "Location not found")
            return {"error": error_msg}
    except Exception as e:
        return {"error": str(e)}