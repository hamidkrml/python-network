import socket

print("Hangi istemci başlatılsın? (1: TCP, 2: UDP)")
secim = input("Seçiminizi girin: ")
server_address = ('localhost', 12345)

if secim == "1":
    # TCP İstemci
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    message = "Hello python from TCP client"
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print("Received message:", data.decode())
    client_socket.close()
elif secim == "2":
    # UDP İstemci
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = "Hello python from UDP client"
    client_socket.sendto(message.encode(), server_address)
    data, _ = client_socket.recvfrom(1024)
    print("Received message:", data.decode())
    client_socket.close()
else:
    print("Geçersiz seçim!")