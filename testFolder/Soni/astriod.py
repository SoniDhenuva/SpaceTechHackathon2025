import requests
import json

# Define the start and end date for the query
start_date = "2025-03-01"
end_date = "2025-03-02"
api_key = "SZmGczOnby9lWoef9BxlmJlqhByTqGluLeFdlJjm"  # Replace with your actual API key if needed

# Define the NeoWs API endpoint
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}"

# Send a GET request to the API
response = requests.get(url)

# Check if the response is successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Print out the data (this will print all data returned in the API response)
    print(json.dumps(data, indent=4))
else:
    print(f"Error fetching data: {response.status_code}")
