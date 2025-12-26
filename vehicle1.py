# Vehicle Mileage Calculator
import sys


def calculate_average(values):
    if len(values) == 0:
        return 0
    return sum(values) / len(values)


def mileage_category(avg_mileage):
    if avg_mileage < 10:
        return "Low Mileage"
    elif 10 <= avg_mileage < 20:
        return "Average Mileage"
    else:
        return "High Mileage"


if __name__ == "__main__":

    script_name = sys.argv[0]

    if len(sys.argv) > 3:
        vehicle_name = sys.argv[1]
        fuel_type = sys.argv[2]
        mileages = list(map(float, sys.argv[3:]))

        print("User provided vehicle details:")
    else:
        vehicle_name = "Car"
        fuel_type = "Petrol"
        mileages = [12.5, 14.0, 15.5, 13.0]

        print("No input given - using default values:")

    total_trips = len(mileages)
    average_mileage = calculate_average(mileages)
    category = mileage_category(average_mileage)

    print("\n========== Vehicle Mileage Details ==========")
    print("Script Name:", script_name)
    print("Vehicle Name:", vehicle_name)
    print("Fuel Type:", fuel_type)
    print("Mileage Records:", mileages)
    print("Total Trips:", total_trips)
    print("Average Mileage:", average_mileage)
    print("Lowest Mileage:", min(mileages))
    print("Highest Mileage:", max(mileages))
    print("Mileage Category:", category)
