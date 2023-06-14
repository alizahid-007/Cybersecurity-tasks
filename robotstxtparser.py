import requests

def parse_robots_txt(url):
    try:
        robots_url = url + "/robots.txt"
        response = requests.get(robots_url)

        # Extract and print the contents of robots.txt
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Specify the base URL to parse the robots.txt file
url = "https://facebook.com"

# Parse the robots.txt file
parse_robots_txt(url)
