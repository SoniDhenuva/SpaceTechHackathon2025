import requests

import datetime
from datetime import datetime


# Define the start and end date for the query

# start_date = "2025-03-01"
start_date = input("Enter Start Date (yyyy-mm-dd): ")
# end_date = "2025-03-02"
end_date = datetime.today().strftime('%Y-%m-%d')

api_key = "SZmGczOnby9lWoef9BxlmJlqhByTqGluLeFdlJjm"  # Replace with your actual API key if needed

# Define the NeoWs API endpoint
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"

# Send a GET request to the API
response = requests.get(url)

# Check if the response is successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract NEOs data
    neos = data["near_earth_objects"]
    
    asteroid_data = []
    hazardous_asteroids = []

    # Loop through each date's NEO list
    for date, asteroids in neos.items():
        for asteroid in asteroids:
            name = asteroid["name"]
            close_approach_data = asteroid["close_approach_data"]

            for approach in close_approach_data:
                miss_distance_km = float(approach["miss_distance"]["kilometers"])

                # Append the asteroid data with miss distance and relevant info
                asteroid_info = {
                    "name": name,
                    "miss_distance_km": miss_distance_km,
                    "approach_date": approach["close_approach_date_full"],
                    "velocity_km_per_s": approach["relative_velocity"]["kilometers_per_second"],
                    "hazardous": asteroid["is_potentially_hazardous_asteroid"]
                }

                asteroid_data.append(asteroid_info)

                # If the asteroid is hazardous, add it to the hazardous_asteroids list
                if asteroid_info["hazardous"]:
                    hazardous_asteroids.append(asteroid_info)

    # Sort the list by miss distance (ascending order) to get the nearest asteroids
    asteroid_data_sorted = sorted(asteroid_data, key=lambda x: x["miss_distance_km"])

    # Get the nearest 3 asteroids
    nearest_asteroids = asteroid_data_sorted[:3]

    # Print out the nearest 3 asteroids
    if nearest_asteroids:
        print()
        print("Nearest 3 Asteroids to Earth (in kilometers):")
        print()
        for asteroid in nearest_asteroids:
            print(f"Name: {asteroid['name']}")
            print(f"Miss Distance (km): {asteroid['miss_distance_km']}")
            print(f"Approach Date: {asteroid['approach_date']}")
            print(f"Velocity (km/s): {asteroid['velocity_km_per_s']}")
            print(f"Hazardous: {asteroid['hazardous']}")
            print()

        # Print out the hazardous asteroids below the nearest 3
        if hazardous_asteroids:
            print("________________________________________________________")
            print()
            print("Hazardous Asteroids (in kilometers):")
            for asteroid in hazardous_asteroids:
                print(f"Name: {asteroid['name']}")
                print(f"Miss Distance (km): {asteroid['miss_distance_km']}")
                print(f"Approach Date: {asteroid['approach_date']}")
                print(f"Velocity (km/s): {asteroid['velocity_km_per_s']}")
                print(f"Hazardous: {asteroid['hazardous']}")
                print()

    else:
        print("No asteroids found in the given date range.")
else:
    print(f"Error fetching data: {response.status_code}")
