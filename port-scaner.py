import socket

target = "scanme.nmap.org"

def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is OPEN")
    s.close()

for p in [80, 443]:
    port_scan(p)