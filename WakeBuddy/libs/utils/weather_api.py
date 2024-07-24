import requests

def get_weather():
    # Example API call (replace with a real weather API)
    try:
        response = requests.get("https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=London")
        weather = response.json()
        return f"{weather['current']['temp_c']}°C, {weather['current']['condition']['text']}"
    except:
        return "Weather data unavailable"
