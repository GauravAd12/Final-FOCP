# 5. Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in fahrenheit, and another that does the reverse
# conversion. Test both functions. (Google will find you the formulae).
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Testing the functions
print(f"25°C = {celsius_to_fahrenheit(25):.2f}°F")  # 77.00°F
print(f"77°F = {fahrenheit_to_celsius(77):.2f}°C")  # 25.00°C
