import requests

def get_weather_data(location, api_key):
    try:
     
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()

       
        if response.status_code == 200:
            return data
        else:
            print(f"Error: {data.get('message', 'Unable to fetch weather data')}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather(data):
    
    city = data['name']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']

    print(f"\nWeather Information for {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Description: {description.capitalize()}")

def main():

    api_key = "998656b6d21a5f6011f377f88eadad58"

    location = input("Enter the name of a city or a zip code: ")

    weather_data = get_weather_data(location, api_key)

    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
