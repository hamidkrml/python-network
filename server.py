import socket

print("Hangi sunucu başlatılsın? (1: TCP, 2: UDP)")
secim = input("Seçiminizi girin: ")

if secim == "1":
    # TCP Sunucu
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(1)
    print("TCP server started")
    while True:
        print("Waiting for a TCP connection...")
        conn, client_address = server_socket.accept()
        print("TCP connection from", client_address)
        data = conn.recv(1024)
        print("Received message:", data.decode())
        message = "Hello from TCP server"
        conn.sendall(message.encode())
        conn.close()
        break
elif secim == "2":
    # UDP Sunucu
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    print("UDP server started")
    while True:
        print("Waiting for a UDP message...")
        data, client_address = server_socket.recvfrom(1024)
        print("Received message:", data.decode())
        message = "Hello from UDP server"
        server_socket.sendto(message.encode(), client_address)
        break
else:
    print("Geçersiz seçim!")