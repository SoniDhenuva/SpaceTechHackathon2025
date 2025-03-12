
import requests

def get_space_weather_data():
    url = "https://services.swpc.noaa.gov/json/planetary_k_index.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch space weather data. Status code: {response.status_code}")
        return None

def get_solar_wind_data():
    url = "https://services.swpc.noaa.gov/json/solar_wind.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch solar wind data. Status code: {response.status_code}")
        return None

def parse_k_index_data(data):
    if data:
        return data[0]['kp_index']  # Parse the K-index
    return None

def parse_solar_wind_data(data):
    if data:
        return data[0]['speed']  # Parse solar wind speed
    return None

def main():
    space_weather_data = get_space_weather_data()
    solar_wind_data = get_solar_wind_data()
    
    if space_weather_data and solar_wind_data:
        k_index = parse_k_index_data(space_weather_data)
        solar_wind_speed = parse_solar_wind_data(solar_wind_data)
        
        print(f"Space Weather: K-index: {k_index}, Solar Wind Speed: {solar_wind_speed} km/s")

if __name__ == "__main__":
    main()
