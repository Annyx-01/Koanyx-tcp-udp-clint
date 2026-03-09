import socket

# ANSI color code for mahogany brown
MAHOGANY = '\033[38;2;192;64;0m'
RESET = '\033[0m'

# Mahogany colored banner
BANNER = f"""
{MAHOGANY}
██╗  ██╗ ██████╗  █████╗ ███╗   ██╗██╗   ██╗██╗  ██╗
██║ ██╔╝██╔═══██╗██╔══██╗████╗  ██║╚██╗ ██╔╝╚██╗██╔╝
█████╔╝ ██║   ██║███████║██╔██╗ ██║ ╚████╔╝  ╚███╔╝ 
██╔═██╗ ██║   ██║██╔══██║██║╚██╗██║  ╚██╔╝   ██╔██╗ 
██║  ██╗╚██████╔╝██║  ██║██║ ╚████║   ██║   ██╔╝ ██╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝
                    UDP CLIENT{RESET}
=====================================================
"""

def udp_client(host, port, message, wait=True, timeout=3):
    """UDP client - works with any host/website"""
    try:
        # Create UDP socket
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        if wait:
            client.settimeout(timeout)
        
        print(f"[*] Sending to {host}:{port} -> {message}")
        client.sendto(message.encode(), (host, port))
        
        if wait:
            try:
                data, addr = client.recvfrom(4096)
                print(f"[*] Response from {addr[0]}:{addr[1]}: {data.decode()}")
            except socket.timeout:
                print("[-] No response (timeout)")
        
        client.close()
        
    except Exception as e:
        print(f"[-] Error: {e}")

# Print mahogany banner
print(BANNER)

if __name__ == "__main__":
    print("=== UDP Client - Works with any website ===\n")
    
    # Get host - can be website or IP
    host = input("Enter host/website (e.g., google.com, example.com): ").strip()
    while not host:
        host = input("Host cannot be empty. Enter host: ").strip()
    
    # Get port
    try:
        port = int(input("Enter port (e.g., 53 for DNS, 123 for NTP): ").strip())
    except:
        port = 53
        print(f"Using default port {port}")
    
    # Get message
    message = input("Enter message to send: ").strip() or "Hello UDP"
    
    # Ask about waiting
    wait = input("Wait for response? (y/n): ").lower().strip() == 'y'
    
    if wait:
        try:
            timeout = float(input("Timeout seconds (default 3): ").strip() or "3")
        except:
            timeout = 3
    else:
        timeout = 3
    
    print("\n" + "="*50)
    udp_client(host, port, message, wait, timeout)