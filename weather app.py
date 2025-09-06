import urllib.request
import json

def get_weather(city):
    API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

    url = BASE_URL + "appid=" + API_KEY + "&q=" + city + "&units=metric"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

            if data.get("cod") != 200:
                print("City not found! Please enter a valid city name.")
                return

            main = data['main']
            weather = data['weather'][0]

            print(f"\nWeather in {city}:")
            print(f"Temperature: {main['temp']}°C")
            print(f"Feels Like: {main['feels_like']}°C")
            print(f"Humidity: {main['humidity']}%")
            print(f"Condition: {weather['description'].title()}")

    except Exception as e:
        print("Error fetching data:", e)

# Run the app
city = input("Enter city name: ")
get_weather(city)


