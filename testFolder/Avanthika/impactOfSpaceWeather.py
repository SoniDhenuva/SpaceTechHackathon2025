
def assess_mission_impact(k_index, solar_wind_speed):
    # Example thresholds for space mission impact
    if k_index >= 7:
        mission_status = "Critical impact - High risk of failure"
    elif k_index >= 5:
        mission_status = "Moderate impact - Possible interference"
    else:
        mission_status = "Low impact - Mission should be safe"
    
    if solar_wind_speed > 600:
        mission_status += " - High solar wind speed detected"
    
    return mission_status

def main():
    k_index = float(input("Enter the K-index (geomagnetic activity): "))
    solar_wind_speed = float(input("Enter the solar wind speed (km/s): "))
    
    mission_impact = assess_mission_impact(k_index, solar_wind_speed)
    print(f"Mission Impact Assessment: {mission_impact}")

if __name__ == "__main__":
    main()
