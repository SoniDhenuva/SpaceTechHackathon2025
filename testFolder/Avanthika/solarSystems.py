
import math

# Function to calculate the distance from Earth to a given planet in the solar system
def calculate_distance(planet_name):
    # Sample data: distance from Earth (in millions of kilometers)
    planet_distances = {
        'Mercury': 91.7,
        'Venus': 41.4,
        'Mars': 78.3,
        'Jupiter': 628.7,
        'Saturn': 1275.0,
        'Uranus': 2724.0,
        'Neptune': 4351.0
    }
    
    if planet_name in planet_distances:
        return planet_distances[planet_name]
    else:
        return None

def main():
    planet = input("Enter the planet name: ").capitalize()
    distance = calculate_distance(planet)
    
    if distance:
        print(f"Distance from Earth to {planet}: {distance} million kilometers.")
    else:
        print("Planet not found. Please check the name and try again.")

if __name__ == "__main__":
    main()
