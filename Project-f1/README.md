# Formula 1 Lap Times Analyzer

Welcome to the **Formula 1 Lap Times Analyzer**! This project is designed to analyze lap times of F1 drivers during a Grand Prix and provide insights into their performance. The program processes lap time data, identifies the fastest driver, and generates comprehensive reports and visualizations.

---

## **Features**

### **1. Lap Time Analysis**
- Reads lap time data from JSON files.
- Identifies the fastest driver and their best lap time.
- Computes average lap times for each driver.

### **2. Driver Details Integration**
- Fetches driver details (name, team) from an external JSON file.
- Displays enriched data about each driver, including their fastest and average lap times.

### **3. Results Visualization**
- Plots lap time trends for all drivers in a Grand Prix.
- Clear and intuitive line chart to compare performance.

### **4. Comprehensive Reports**
- Saves detailed analysis results in a JSON log file.
- Outputs a formatted table of results in the console.

---

## **How It Works**

### **1. Data Loading**
- **Driver Details**: Loaded from `f1_drivers.json`, which contains driver codes, names, and team information.
- **Lap Times**: Parsed from a JSON file containing lap times and the Grand Prix location.

### **2. Lap Time Analysis**
- Computes the fastest and average lap times for each driver.
- Identifies the overall fastest driver of the session.

### **3. Reporting**
- Displays results in a formatted table with driver details, fastest lap times, and average lap times.
- Saves a detailed JSON report to a file.

### **4. Visualization**
- Generates a line plot for lap times, showing performance trends for each driver during the session.

---

## **Getting Started**

### **Prerequisites**
- Python 3.x
- Required libraries: `matplotlib`, `tabulate`

Install the dependencies using:
```bash
pip install matplotlib tabulate
```

### **Setup Instructions**
1. Clone or download this repository.
2. Ensure the following JSON files are present:
   - `f1_drivers.json`: Contains driver codes, names, and team information.
   - Lap times JSON file (e.g., `lap_times.json`): Contains lap times and Grand Prix location.

### **Running the Program**
1. Execute the main script in your terminal:
   ```bash
   python lap_time_analyzer.py
   ```
2. Follow the console outputs to view results and locate saved reports.

---

## **File Structure**
- **lap_time_analyzer.py**: Main script for analyzing lap times.
- **f1_drivers.json**: JSON file containing driver details.
- **lap_times.json**: Example lap times data file.
- **results_log.json**: Generated JSON file containing analysis results (created after execution).

---

## **Example JSON Files**

### `f1_drivers.json`
```json
{
    "HAM": {"name": "Lewis Hamilton", "team": "Mercedes"},
    "VER": {"name": "Max Verstappen", "team": "Red Bull Racing"},
    "LEC": {"name": "Charles Leclerc", "team": "Ferrari"}
}
```

### `lap_times.json`
```json
{
    "grand_prix_location": "Monza",
    "lap_times": {
        "HAM": [77.321, 77.654, 77.452],
        "VER": [76.987, 77.125, 76.945],
        "LEC": [78.102, 77.998, 78.231]
    }
}
```

---

## **Demo**

### Console Output
Displays results in a neat table format:
```
+------+-----------------+----------------+--------------+---------------+
| Code | Name            | Team           | Fastest Time | Average Time  |
+------+-----------------+----------------+--------------+---------------+
| VER  | Max Verstappen  | Red Bull Racing| 76.945       | 77.019        |
| HAM  | Lewis Hamilton  | Mercedes       | 77.321       | 77.476        |
| LEC  | Charles Leclerc | Ferrari        | 77.998       | 78.110        |
+------+-----------------+----------------+--------------+---------------+
```
Main output visual form
![image](https://github.com/user-attachments/assets/b7557401-c49a-4a60-80db-388e345f360b)
Fast Time vs Average time
![image](https://github.com/user-attachments/assets/96c5eee9-3d06-465c-8ec7-c86834edaa6d)
lap-times2 visual
![alt text](image.png)


### Plot
Generates a line chart showing lap time trends for all drivers.

---

## **Contributing**
We welcome contributions! To add features or fix issues:
1. Fork this repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes and push them:
   ```bash
   git commit -m "Added YourFeatureName"
   git push origin feature/YourFeatureName
   ```
4. Submit a pull request.

---

## **License**
This project is licensed under the MIT License. You are free to use, modify, and distribute it.

---

## **Contact**
For questions or feedback, reach out to [Your Contact Information].

---

🏎️

Auther Gaurav Adhikari
Email adhikarygaurav99@gmail.com
