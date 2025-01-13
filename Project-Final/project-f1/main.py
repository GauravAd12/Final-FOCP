import json
import matplotlib.pyplot as plt
from tabulate import tabulate

# Function to load driver details from f1_drivers.json
def load_driver_details(file_name="f1_drivers.json"):
    try:
        with open(file_name, 'r') as file:
            drivers = json.load(file)
        return drivers
    except FileNotFoundError:
        print(f"Error: '{file_name}' not found. Driver details will not be displayed.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in '{file_name}'.")
        return {}

# Function to parse lap times from a JSON file
def parse_lap_times(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        
        # Extract Grand Prix location and lap times
        grand_prix_location = data.get("grand_prix_location", "Unknown Location")
        lap_times = data.get("lap_times", {})
        
        return grand_prix_location, lap_times
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return "Unknown Location", {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in '{file_name}'.")
        return "Unknown Location", {}

# Function to analyze lap times
def analyze_lap_times(lap_times):
    fastest_time_overall = float('inf')
    fastest_driver_overall = None
    driver_metrics = []

    for driver, times in lap_times.items():
        fastest_time = min(times)
        average_time = sum(times) / len(times)

        driver_metrics.append({
            "driver": driver,
            "fastest_time": fastest_time,
            "average_time": average_time
        })

        if fastest_time < fastest_time_overall:
            fastest_time_overall = fastest_time
            fastest_driver_overall = driver

    return fastest_driver_overall, fastest_time_overall, driver_metrics

# Function to save results to a JSON log
def save_to_json_log(grand_prix_location, fastest_driver, fastest_time, driver_metrics, driver_details, log_file):
    log_data = {
        "grand_prix_location": grand_prix_location,
        "fastest_driver": fastest_driver,
        "fastest_time": fastest_time,
        "driver_details": []
    }

    for d in driver_metrics:
        details = driver_details.get(d["driver"], {"name": "Unknown", "team": "Unknown"})
        log_data["driver_details"].append({
            "code": d["driver"],
            "name": details["name"],
            "team": details["team"],
            "fastest_time": d["fastest_time"],
            "average_time": d["average_time"]
        })

    with open(log_file, "w") as log_file:
        json.dump(log_data, log_file, indent=4)

    print(f"Results have been saved to '{log_file.name}'.")

# Function to display results
def display_results(grand_prix_location, fastest_driver, fastest_time, driver_metrics, driver_details):
    print(f"Grand Prix Location: {grand_prix_location}\n")
    print(f"Fastest Driver Overall: {fastest_driver} with a time of {fastest_time:.3f} seconds\n")

    driver_metrics_sorted = sorted(driver_metrics, key=lambda x: x["fastest_time"])
    table = []

    for d in driver_metrics_sorted:
        details = driver_details.get(d["driver"], {"name": "Unknown", "team": "Unknown"})
        table.append([
            d["driver"],
            details["name"],
            details["team"],
            f"{d['fastest_time']:.3f}",
            f"{d['average_time']:.3f}"
        ])

    print(tabulate(table, headers=["Code", "Name", "Team", "Fastest Time", "Average Time"], tablefmt="grid"))

# Function to plot lap times
def plot_lap_times(lap_times, grand_prix_location):
    plt.figure(figsize=(12, 6))
    for driver, times in lap_times.items():
        plt.plot(times, marker='o', label=driver)

    plt.title(f'Lap Times at {grand_prix_location}')
    plt.xlabel('Lap Number')
    plt.ylabel('Lap Time (seconds)')
    plt.legend()