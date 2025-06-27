import requests
import json


KEY = '39c6fd155ddf3b385d7faac9d3594946'

# Function to get weather data from OpenWeatherMap API
def get_weather(latitude: float, longitude: float) -> dict:
    URL = f'http://api.openweathermap.org/data/2.5//weather?appid={KEY}&lat={latitude}&lon={longitude}&units=metric&lang=ru'
    request = requests.get(URL)

    if request.status_code == 200:
        return json.loads(request.text)
    
    else:
        print(f'Error: {request.status_code}')
        return None