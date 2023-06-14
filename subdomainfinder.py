import requests

def find_subdomains(domain):
    subdomains = set()

    try:
        # Craft the URL for the certificate search API
        url = f"https://crt.sh/?q=%25.{domain}&output=json"

        # Send a GET request to the API
        response = requests.get(url)

        # Extract subdomains from the API response
        data = response.json()
        for item in data:
            subdomains.add(item['name_value'])
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return subdomains

domain_name = "wickr.com"
subdomains = find_subdomains(domain_name)
print(subdomains)
