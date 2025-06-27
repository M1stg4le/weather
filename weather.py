from coordinates import get_coordinate
from api_request import get_weather
from formate_weather import format_weather
from structure_data import structure_data

def main() -> None:
    coordinate = get_coordinate()
    weather = get_weather(latitude=coordinate.Latitude, longitude=coordinate.longitude)
    structured_data = structure_data(weather=weather)
    print(format_weather(weather=structured_data))

if __name__ == '__main__':
    main()