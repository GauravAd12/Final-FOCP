# 3. Write a program that manages a list of countries and their capital cities. It should
# prompt the user to enter the name of a country. If the program already "knows"
# the name of the capital city, it should display it. Otherwise it should ask the user to
# enter it. This should carry on until the user terminates the program (how this
# happens is up to you).
def manage_countries():
    countries = {}
    while True:
        country = input("Enter the name of a country (or 'quit' to stop): ").strip().lower()
        if country == 'quit':
            break
        if country in countries:
            print(f"The capital of {country.title()} is {countries[country]}.")
        else:
            capital = input(f"Capital of {country.title()} not found. Enter the capital: ").strip()
            countries[country] = capital
            print(f"{capital} has been added as the capital of {country.title()}.")

# Example usage
manage_countries()
