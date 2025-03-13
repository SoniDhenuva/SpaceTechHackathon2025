from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "SZmGczOnby9lWoef9BxlmJlqhByTqGluLeFdlJjm"

@app.route("/", methods=["GET", "POST"])
def index():
    asteroid_data = []
    hazardous_asteroids = []

    if request.method == "POST":
        start_date = request.form["start_date"]
        present = datetime.today().strftime('%Y-%m-%d')

        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={present}&api_key={API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            neos = data["near_earth_objects"]

            for date, asteroids in neos.items():
                for asteroid in asteroids:
                    name = asteroid["name"]
                    close_approach_data = asteroid["close_approach_data"]

                    for approach in close_approach_data:
                        asteroid_info = {
                            "name": name,
                            "miss_distance_km": float(approach["miss_distance"]["kilometers"]),
                            "approach_date": approach["close_approach_date_full"],
                            "velocity_km_per_s": approach["relative_velocity"]["kilometers_per_second"],
                            "hazardous": asteroid["is_potentially_hazardous_asteroid"]
                        }
                        asteroid_data.append(asteroid_info)

                        if asteroid_info["hazardous"]:
                            hazardous_asteroids.append(asteroid_info)

            # Sort by miss distance
            asteroid_data_sorted = sorted(asteroid_data, key=lambda x: x["miss_distance_km"])
            nearest_asteroids = asteroid_data_sorted[:3]
        else:
            return f"Error fetching data: {response.status_code}"

        return render_template("index.html", nearest_asteroids=nearest_asteroids, hazardous_asteroids=hazardous_asteroids)

    return render_template("index.html", nearest_asteroids=None, hazardous_asteroids=None)

if __name__ == "__main__":
    app.run(debug=True)
