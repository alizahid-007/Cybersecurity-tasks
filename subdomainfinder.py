# import requests
# import re
# def find_subdomains(domain):
#     subdomains = []

#     # Craft the URL for the request
#     url = f"http://www.{domain}"

#     try:
#         # Send a GET request to the domain
#         response = requests.get(url)

#         # Extract subdomains using regular expressions
#         subdomains = re.findall(r'(?<=http://)[\w.-]+', response.text)
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")

#     return subdomains
# domain_name = "wickr.com"
# subdomains = find_subdomains(domain_name)
# print(subdomains)
# import requests

# def find_subdomains(domain):
#     subdomains = []

#     try:
#         # Craft the URL for the certificate search API
#         url = f"https://crt.sh/?q=%25.{domain}&output=json"

#         # Send a GET request to the API
#         response = requests.get(url)

#         # Extract subdomains from the API response
#         data = response.json()
#         for item in data:
#             subdomains.append(item['name_value'])
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")

#     return subdomains

# domain_name = "wickr.com"
# subdomains = find_subdomains(domain_name)
# print(subdomains)

# import requests
# import csv

# def find_subdomains(domain):
#     subdomains = set()

#     try:
#         # Craft the URL for the certificate search API
#         url = f"https://crt.sh/?q=%25.{domain}&output=json"

#         # Send a GET request to the API
#         response = requests.get(url)

#         # Extract subdomains from the API response
#         data = response.json()
#         for item in data:
#             subdomains.add(item['name_value'])
#     except requests.exceptions.RequestException as e:
#         print(f"An error occurred: {e}")

#     return subdomains

# def save_subdomains_to_csv(subdomains, filename):
#     with open(filename, 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerow(['Subdomain'])
#         for subdomain in subdomains:
#             writer.writerow([subdomain])

# domain_name = "wickr.com"
# subdomains = find_subdomains(domain_name)

# # Specify the filename to save the subdomains
# csv_filename = "subdomains.csv"

# # Save subdomains to CSV
# save_subdomains_to_csv(subdomains, csv_filename)

# print(f"Subdomains saved to {csv_filename}.")

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
