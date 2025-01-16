
import json
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np


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

# Function to display results
def display_results(grand_prix_location, fastest_driver, fastest_time, driver_metrics, driver_details, file_name):
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
    plot_lap_times(driver_metrics_sorted, driver_details, file_name, grand_prix_location)

# Function to plot lap times comparison for all drivers
def plot_lap_times(driver_metrics_sorted, driver_details, file_name, grand_prix_location):
    drivers = [d["driver"] for d in driver_metrics_sorted]
    fastest_times = [d["fastest_time"] for d in driver_metrics_sorted]
    average_times = [d["average_time"] for d in driver_metrics_sorted]
    names = [driver_details.get(d["driver"], {}).get("name", "Unknown") for d in driver_metrics_sorted]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(drivers))
    bar_width = 0.35

    if file_name == "lap_times_1.json":
        ax.bar(x - bar_width / 2, fastest_times, bar_width, label='Fastest Time', color='blue')
        ax.bar(x + bar_width / 2, average_times, bar_width, label='Average Time', color='orange')
    elif file_name == "lap_times_2.json":
        ax.bar(x - bar_width / 2, fastest_times, bar_width, label='Fastest Time', color='green')
        ax.bar(x + bar_width / 2, average_times, bar_width, label='Average Time', color='red')
    elif file_name == "lap_times_3.json":
        ax.bar(x - bar_width / 2, fastest_times, bar_width, label='Fastest Time', color='purple')
        ax.bar(x + bar_width / 2, average_times, bar_width, label='Average Time', color='yellow')

    ax.set_xlabel('Driver')
    ax.set_ylabel('Time (seconds)')
    ax.set_title(f'Fastest vs Average Lap Times, {grand_prix_location}')
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=45, ha="right")
    ax.legend()

    plt.tight_layout()
    plt.show()

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
        
        grand_prix_location = data.get("grand_prix_location", "Unknown Location")
        lap_times = data.get("lap_times", {})
        
        return grand_prix_location, lap_times
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return "Unknown Location", {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON in '{file_name}'.")
        return "Unknown Location", {}

# Function to process multiple files
def main():
    lap_times_files = ["lap_times_1.json", "lap_times_2.json", "lap_times_3.json"]
    driver_details = load_driver_details()

    for lap_times_file in lap_times_files:
        print(f"\nProcessing file: {lap_times_file}\n")
        
        grand_prix_location, lap_times = parse_lap_times(lap_times_file)
        
        if not lap_times:
            print(f"No data found in {lap_times_file}. Skipping...\n")
            continue
        
        fastest_driver, fastest_time, driver_metrics = analyze_lap_times(lap_times)
        display_results(grand_prix_location, fastest_driver, fastest_time, driver_metrics, driver_details, lap_times_file)

if __name__ == "__main__":
    main()