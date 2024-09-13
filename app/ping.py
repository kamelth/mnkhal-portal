import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import sr1, IP, ICMP
import socket

def get_mosquitto_ip():
    try:
        mosquitto_ip = socket.gethostbyname('mosquitto')
        print(f"Mosquitto Broker IP Address: {mosquitto_ip}")
        return mosquitto_ip
    except socket.error as err:
        print(f"Error getting IP: {err}")
        return None

def ping_host(host):
    try:
        # Create the packet with IP and ICMP layers
        packet = IP(dst=host)/ICMP()
        # Send the packet and wait for the response
        response = sr1(packet, timeout=2, verbose=False)

        if response:
            print(f"{host} is reachable (Ping successful)")
        else:
            print(f"{host} is unreachable (Ping failed)")
    except Exception as e:
        print(f"Error pinging {host}: {e}")

def check_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(2)  # Set timeout for the connection attempt
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} on {host} is open")
            else:
                print(f"Port {port} on {host} is closed or unreachable")
    except Exception as e:
        print(f"Error checking port {port} on {host}: {e}")

mosquitto_ip = get_mosquitto_ip()
if mosquitto_ip:
    ping_host(mosquitto_ip)
    check_port(mosquitto_ip, 1883)  # Check the Mosquitto MQTT port (1883)
