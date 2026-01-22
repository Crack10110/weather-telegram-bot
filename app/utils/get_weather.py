import requests
from config import WEATHER_API_KEY

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric",
        "lang": "en"
    }

    r = requests.get(url, params=params).json()

    if r.get("cod") != 200:
        return "I couldn't find a city with that name."

    return {
        "desc": r["weather"][0]["description"],
        "temp": r["main"]["temp"],
        "feels": r["main"]["feels_like"]
    }


