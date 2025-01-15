# 4. Write a program that takes a URL as a command-line argument and reports
# whether or not there is a working website at that address
import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
else:
    url = sys.argv[1]
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("The website is working!")
        else:
            print(f"Website returned status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
