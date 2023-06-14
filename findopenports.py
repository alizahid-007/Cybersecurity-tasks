import socket

def check_open_ports(domain, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Adjust the timeout value as needed

        result = sock.connect_ex((domain, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    return open_ports

# Specify the domain and the ports to check
domain = "example.com"
ports_to_check = [80,21, 443, 22, 8080]  # Add or remove ports as needed

# Call the function to check open ports
open_ports = check_open_ports(domain, ports_to_check)

# Print the open ports
if open_ports:
    print(f"The following ports are open on {domain}:")
    for port in open_ports:
        print(f"Port {port} is open")
else:
    print(f"No open ports found on {domain}")
