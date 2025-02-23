import requests

try:
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    data = response.json()

    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    timestamp = data['timestamp']

    print(f"ISS Location (Real-time):")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")
    print(f"Timestamp (UTC): {timestamp}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching ISS data: {e}")