import socket

def port_scanner(target_ip, start_port, end_port):
    print(f"Scanning {target_ip} for open ports...\n")
    for port in range(start_port, end_port + 1):
        try:
            # Create a socket and attempt to connect
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is open.")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    # Get user input
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    port_scanner(target_ip, start_port, end_port)
