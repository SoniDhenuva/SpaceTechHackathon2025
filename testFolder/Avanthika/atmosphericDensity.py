import math

def calculate_density(altitude):
    # Constants for the model (in SI units)
    sea_level_density = 1.225  # kg/m^3
    scale_height = 8500  # meters, scale height of Earth's atmosphere
    
    # Exponential model for atmospheric density
    density = sea_level_density * math.exp(-altitude / scale_height)
    return density

def main():
    altitude = float(input("Enter altitude (in meters): "))
    density = calculate_density(altitude)
    
    print(f"Atmospheric density at {altitude} meters: {density:.6f} kg/m^3")

if __name__ == "__main__":
    main()
