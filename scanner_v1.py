import socket

IP_addrs = input(
    "Enter the IP address of the target(s) (you can choose multiple hosts, e.g., 192.168.0.1,192.168.0.2): ")
ports = input(
    "Enter the port(s) of the chosen target (you can choose multiple ports, e.g., 22,23): ")

list_of_IP = [IP_addr.strip() for IP_addr in IP_addrs.split(",")]
list_of_ports = [int(port.strip()) for port in ports.split(",")]

for ip_addr in list_of_IP:
    for port in list_of_ports:
        try:
            s = socket.socket()
            s.connect((ip_addr, port))
            print(f"Found port: {port} on host: {ip_addr}")

            answer = s.recv(1024)
            print(answer)

            s.close()

        except ConnectionRefusedError as e:
            print(
                f"Connection refused as port {port} on host {ip_addr} isn't online:", e)
            continue

        except Exception as e:
            print("An error occurred:", e)
            continue
