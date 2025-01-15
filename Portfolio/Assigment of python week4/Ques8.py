# 8. Modify the previous program so that it can process any number of values. The input
# terminates when the user just pressed "Enter" at the prompt rather than entering a
# value.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def process_temperatures_any():
    temperatures = []
    while True:
        temp_input = input("Enter a temperature (e.g., 25C) or press Enter to finish: ").strip()
        if temp_input == "":
            break
        elif temp_input[-1].upper() == 'C' and temp_input[:-1].replace('.', '', 1).isdigit():
            temperatures.append(float(temp_input[:-1]))
        else:
            print("Invalid input. Please enter a number followed by 'C'.")

    if temperatures:
        # Calculations
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        print(f"Max temperature: {max_temp:.2f}C")
        print(f"Min temperature: {min_temp:.2f}C")
        print(f"Mean temperature: {mean_temp:.2f}C")
    else:
        print("No temperatures entered.")

# Testing the program
process_temperatures_any()
