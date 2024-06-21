import requests
import json

def fetch_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def process_weather(weather_data):
    if weather_data is None:
        return None
    
    # Extract relevant information from weather_data
    processed_data = {
        "temperature": weather_data["main"]["temp"],
        "description": weather_data["weather"][0]["description"],
        "humidity": weather_data["main"]["humidity"],
        "wind_speed": weather_data["wind"]["speed"]
        # Add more fields as needed
    }
    
    return processed_data

def main():
    # Replace with your OpenWeatherMap API key
    api_key = "1a561f503128a35f9d5b9336db1a71af"
    city = "Delhi,IN"  # Replace with the city you want weather data for
    
    # Fetch weather data
    weather_data = fetch_weather(api_key, city)
    
    if weather_data:
        # Process and clean the data
        processed_data = process_weather(weather_data)
        
        # Display or further process the cleaned data
        if processed_data:
            print("Weather in {}: {}, Temperature: {}°C, Humidity: {}%, Wind Speed: {} m/s"
                  .format(city, processed_data["description"].capitalize(),
                          processed_data["temperature"], processed_data["humidity"], processed_data["wind_speed"]))
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()
