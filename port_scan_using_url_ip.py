import socket

def get_ip_address(url):
    ip_address = None
    try:
        ip_address = socket.gethostbyname(url)
    except socket.error:
        print("Error occurred during DNS lookup")
    return ip_address

def port_scan(ip_address, ports):
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")
            sock.close()
        except socket.error:
            print("Error occurred during port scanning")

print(r"""
            ___         _          ______
           / _ \       | |        |_    _|
          / /_\ \      | |          |  |
         / /_ _  \     | |          |  |
        / /    \  \    | |_____    _|  |_
        \/      \__\   |_______|  |______|
        
        Created by @ Zahid Ali
        """)
print('---------------------------------------------------')

# Get the input from user (URL or IP address)
input_str = input("Enter the URL or IP address: ")

# Get the ports to scan as a comma-separated list
ports_str = input("Enter the ports to scan (comma-separated): ")
ports = [int(p.strip()) for p in ports_str.split(',')]

# Check if input is an IP address or URL
try:
    socket.inet_aton(input_str)
    ip_address = input_str
    url = None
except socket.error:
    url = input_str
    ip_address = get_ip_address(url)
    print(f"IP address for {url}: {ip_address}")

if ip_address:
    print("Performing port scan...")
    port_scan(ip_address, ports)
else:
    print("Failed to obtain IP address for the specified URL.")
