import requests

asteroid_id = "2000433"  # Example asteroid ID
nasa_url = f"https://api.nasa.gov/neo/rest/v1/neo/{asteroid_id}?api_key=SZmGczOnby9lWoef9BxlmJlqhByTqGluLeFdlJjm"
response = requests.get(nasa_url)
data = response.json()

# Check if the request was successful
if response.status_code == 200:
    # Print asteroid details in an organized manner
    print("Asteroid Information:")
    print(f"Name: {data['name']}")
    print(f"NASA JPL URL: {data['nasa_jpl_url']}")
    
    # Estimated diameter check
    if 'estimated_diameter' in data and 'kilometers' in data['estimated_diameter']:
        diameter_info = data['estimated_diameter']['kilometers']
        min_diameter = diameter_info.get('min', 'Not available')
        max_diameter = diameter_info.get('max', 'Not available')
        print(f"Estimated Diameter (Min): {min_diameter} km")
        print(f"Estimated Diameter (Max): {max_diameter} km")
    else:
        print("Estimated diameter data is not available.")
    
    # Close approach data (if available)
    if 'close_approach_data' in data and len(data['close_approach_data']) > 0:
        close_approach = data['close_approach_data'][0]
        print(f"Close Approach Date: {close_approach['close_approach_date']}")
        print(f"Miss Distance (Astronomical Units): {close_approach['miss_distance']['astronomical']}")
        print(f"Relative Velocity (km/h): {close_approach['relative_velocity']['kilometers_per_hour']}")
    else:
        print("Close approach data not available.")
    
    # Additional information
    if 'is_potentially_hazardous_asteroid' in data:
        hazardous_status = "Yes" if data['is_potentially_hazardous_asteroid'] else "No"
        print(f"Potentially Hazardous: {hazardous_status}")
else:
    print(f"Error: Unable to retrieve data for asteroid {asteroid_id}. HTTP Status Code: {response.status_code}")


