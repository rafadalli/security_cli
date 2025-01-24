import socket
from datetime import datetime


class PortScanner:
    def scan(self, hostname: str) -> None:
        """Scans ports based on the hostname"""
        # Defining a target
        target = socket.gethostbyname(hostname)

        print("-" * 50)
        print("Scanning Target: " + target)
        print("Scanning started at:" + str(datetime.now()))
        print("-" * 50)

        # Scan ports between 1 to 65,535
        for port in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # Returns an error indicator
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
            s.close()
