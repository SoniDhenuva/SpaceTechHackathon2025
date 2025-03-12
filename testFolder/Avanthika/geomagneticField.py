import math

# Function to calculate geomagnetic field strength (based on latitude)
def calculate_geomagnetic_field_strength(latitude):
    # Constants (simplified model)
    equator_strength = 30  # nT (nanoteslas) at the equator
    pole_strength = 60    # nT at the poles
    
    # Estimate strength (simplified linear model)
    geomagnetic_strength = equator_strength + (pole_strength - equator_strength) * abs(math.sin(math.radians(latitude)))
    return geomagnetic_strength

def main():
    latitude = float(input("Enter the latitude: "))
    field_strength = calculate_geomagnetic_field_strength(latitude)
    print(f"Geomagnetic field strength at latitude {latitude}°: {field_strength:.2f} nT")

if __name__ == "__main__":
    main()
