import requests
import xml.etree.ElementTree as ET

SSC_API_URL = "https://sscweb.gsfc.nasa.gov/WS/sscr/2/observatories"

def get_satellite_data(satellite_name):
    """Fetch satellite data from the SSC API and parse XML response."""
    response = requests.get(SSC_API_URL)

    if response.status_code == 200:
        root = ET.fromstring(response.text)

        # Define XML namespace
        ns = {"ssc": "http://sscweb.gsfc.nasa.gov/schema"}

        # Iterate over observatories
        for obs in root.findall("ssc:Observatory", ns):
            sat_id = obs.find("ssc:Id", ns).text if obs.find("ssc:Id", ns) is not None else "Unknown"
            sat_name = obs.find("ssc:Name", ns).text if obs.find("ssc:Name", ns) is not None else "Unknown"
            start_time = obs.find("ssc:StartTime", ns).text if obs.find("ssc:StartTime", ns) is not None else "N/A"
            end_time = obs.find("ssc:EndTime", ns).text if obs.find("ssc:EndTime", ns) is not None else "N/A"

            # Check if the requested satellite matches
            if satellite_name.lower() == sat_id.lower():
                print("\n**Satellite Information**")
                print(f"Satellite ID  : {sat_id}")
                print(f"Name         : {sat_name}")
                print(f"Launch Time   : {start_time}")
                print(f"Shutdown Time     : {end_time}\n")
                return

        print(f"⚠️ Satellite '{satellite_name}' not found in SSC response.")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Test the function
if __name__ == "__main__":
    satellite_name = input("Enter a Satellite Name: ") #"ace"  # Example satellite ID
    get_satellite_data(satellite_name)
