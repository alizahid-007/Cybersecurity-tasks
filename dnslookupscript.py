import dns.resolver

def perform_dns_lookup(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for answer in answers:
            print(answer)
    except dns.resolver.NXDOMAIN as e:
        print(f"Domain not found: {e}")

# Specify the domain for DNS lookup
domain = "example.com"

# Perform DNS lookup
perform_dns_lookup(domain)
