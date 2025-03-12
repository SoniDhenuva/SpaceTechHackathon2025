
# Constants for solar radiation calculation
SOLAR_CONSTANT = 1361  # W/m^2, average solar constant at 1 AU

def calculate_solar_radiation(distance_from_sun):
    """
    Calculate the solar radiation at a given distance from the Sun.
    :param distance_from_sun: Distance from the Sun in AU (Astronomical Units)
    :return: Solar radiation in W/m^2
    """
    return SOLAR_CONSTANT / (distance_from_sun ** 2)

def main():
    distance = float(input("Enter the distance from the Sun in AU (e.g., 1 for Earth): "))
    solar_radiation = calculate_solar_radiation(distance)
    print(f"Solar radiation at {distance} AU: {solar_radiation:.2f} W/m^2")

if __name__ == "__main__":
    main()
