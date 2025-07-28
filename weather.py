import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,

        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    print (response)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    else:
        return {"error": f"Unable to fetch weather. Status code: {response.status_code}"}

# Example usage
if __name__ == "__main__":
    YOUR_API_KEY = "9fde7798706edf680cb709b5eedd87b2"
    city = input("Enter city name: ")
    result = get_weather(city, YOUR_API_KEY)
    
    if "error" in result:
        print(result["error"])
    else:
        print(f"Weather in {result['city']}:")
        print(f"Temperature: {result['temperature']}°C")
        print(f"Condition: {result['description']}")
        print(f"Humidity: {result['humidity']}%")
        print(f"Wind Speed: {result['wind_speed']} m/s")

