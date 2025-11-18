import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)

print("server calling started")

while True:
    print("Waiting for a message...")
    data, client_address = server_socket.recvfrom(1024)
    print("Received message:", data.decode())

    message = "Hello from server"
    server_socket.sendto(message.encode(), client_address)
    # Sunucu sürekli çalışsın istiyorsanız break'i kaldırabilirsiniz
    break