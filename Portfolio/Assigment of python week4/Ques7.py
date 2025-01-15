# 7. Write a program that reads 6 temperatures (in the same format as before), and
# displays the maximum, minimum, and mean of the values.
# Hint: You should know there are built-in functions for max and min. If you hunt, you
# might also find one for the mean.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def process_temperatures():
    temperatures = []
    for i in range(6):
        temp_input = input(f"Enter temperature {i + 1} (e.g., 25C): ").strip()
        if temp_input[-1].upper() == 'C' and temp_input[:-1].isdigit():
            temperatures.append(float(temp_input[:-1]))
        else:
            print("Invalid input. Try again.")
            return
    
    # Calculations
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)
    print(f"Max temperature: {max_temp:.2f}C")
    print(f"Min temperature: {min_temp:.2f}C")
    print(f"Mean temperature: {mean_temp:.2f}C")

# Testing the program
process_temperatures()
