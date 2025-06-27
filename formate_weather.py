def format_weather(weather: tuple) -> str:
    temperature, wind_speed, weather_type, sunset, sunrise = weather
    weather_emojis = {
    "Ясно": "☀️",
    "Облачно": "☁️",
    "Дождь": "🌧️",
    "Снег": "❄️"
}
    emoji = weather_emojis.get(weather_type, "")

    return (
        f"Temperature: {temperature}°C\n"
        f"Wind Speed: {wind_speed} m/s\n"
        f"Weather: {weather_type} {emoji}\n"
        f"Sunset: {sunset.strftime('%H:%M:%S')}\n"
        f"Sunrise: {sunrise.strftime('%H:%M:%S')}"
    )