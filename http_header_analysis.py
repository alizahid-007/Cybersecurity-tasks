import requests

def analyze_http_headers(url):
    try:
        response = requests.head(url)
        headers = response.headers

        # Extract and print the HTTP headers
        for header, value in headers.items():
            print(f"{header}: {value}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Specify the URL to analyze the HTTP headers
url = "https://example.com"

# Analyze the HTTP headers
analyze_http_headers(url)
