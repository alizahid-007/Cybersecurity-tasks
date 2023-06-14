import whois

def perform_whois_lookup(domain):
    try:
        result = whois.whois(domain)
        print(result)
    except whois.parser.PywhoisError as e:
        print(f"An error occurred: {e}")

# Specify the domain for WHOIS lookup
domain = "example.com"

# Perform WHOIS lookup
perform_whois_lookup(domain)
