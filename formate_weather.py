def format_weather(weather: tuple) -> str:
    temperature, wind_speed, weather_type, sunset, sunrise = weather
    emoji = []
    return (
        f"Temperature: {temperature}°C\n"
        f"Wind Speed: {wind_speed} m/s\n"
        f"Weather: {weather_type}\n"
        f"Sunset: {sunset.strftime('%H:%M:%S')}\n"
        f"Sunrise: {sunrise.strftime('%H:%M:%S')}"
    )