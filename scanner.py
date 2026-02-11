import socket
from datetime import datetime


def scan_port(target: str, port: int) -> None:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[+] Port {port} is open")
    except socket.gaierror:
        print("[-] Hostname could not be resolved.")
    except socket.error:
        print("[-] Could not connect to server.")


def main():
    target = input("Enter target IP or hostname: ")
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

    print(f"\nScanning target {target}")
    print(f"Time started: {datetime.now()}\n")

    for port in range(start_port, end_port + 1):
        scan_port(target, port)

    print(f"\nScan finished at: {datetime.now()}")


if __name__ == "__main__":
    main()
