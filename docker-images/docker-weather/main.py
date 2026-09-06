from flask import Flask, jsonify, make_response
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

def get_coordinates(city_name):
    geocode_url = "https://nominatim.openstreetmap.org/search"
    params = {"q": city_name, "format": "json", "limit": 1}
    headers = {"User-Agent": "WeatherAppDocker/1.0"}
    res = requests.get(geocode_url, params=params, headers=headers, timeout=5)
    res.raise_for_status()
    data = res.json()
    if not data:
        return None
    return {"lat": data[0]["lat"], "lon": data[0]["lon"]}

@app.route("/")
def health():
    return "The service is running", 200

@app.errorhandler(Exception)
def handle_error(error):
    return make_response(jsonify({"message": "Internal server error", "error": str(error)}), 500)

@app.route('/<city>')
def get_weather(city):
    try:
        coords = get_coordinates(city)
        if not coords:
            return make_response(jsonify({"message": f"City '{city}' not found."}), 404)
    except requests.exceptions.RequestException as e:
        return make_response(jsonify({"message": "Geocoding error", "error": str(e)}), 502)

    weather_url = "https://open-weather13.p.rapidapi.com/fivedaysforcast"
    querystring = {
        "latitude": coords["lat"],
        "longitude": coords["lon"],
        "lang": "EN"
    }
    headers = {
        'Content-Type': "application/json",
        'x-rapidapi-host': "open-weather13.p.rapidapi.com",
        'x-rapidapi-key': os.getenv("APIKEY")
    }

    try:
        response = requests.get(weather_url, headers=headers, params=querystring, timeout=10)
        response.raise_for_status()
        raw = response.json()

        # Extract current data from the first forecast entry
        current_entry = raw.get("list", [{}])[0]
        main = current_entry.get("main", {})
        weather = current_entry.get("weather", [{}])[0]
        wind = current_entry.get("wind", {})

        # Convert Kelvin to Celsius and m/s to km/h
        temp_k = main.get("temp", 273.15)
        temp_c = round(temp_k - 273.15, 1)
        wind_speed_ms = wind.get("speed", 0)
        wind_kph = round(wind_speed_ms * 3.6, 1)

        icon_code = weather.get("icon", "01d")
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"

        # Match the exact schema the browser's JavaScript needs
        formatted_response = {
            "location": {
                "name": raw.get("city", {}).get("name", city.capitalize()),
                "country": raw.get("city", {}).get("country", "")
            },
            "current": {
                "temp_c": temp_c,
                "temp_f": round((temp_c * 9/5) + 32, 1),
                "humidity": main.get("humidity", 0),
                "wind_kph": wind_kph,
                "condition": {
                    "text": weather.get("description", "Clear").capitalize(),
                    "icon": icon_url
                }
            }
        }

        return jsonify(formatted_response)

    except requests.exceptions.RequestException as e:
        return make_response(jsonify({"message": "Weather API error", "error": str(e)}), 500)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)