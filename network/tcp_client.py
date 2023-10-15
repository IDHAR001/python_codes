from socket import *

# Create tcp socket
sockfd = socket()

# Connect server

server_addr = ('127.0.0.1',80)
sockfd.connect(server_addr)

# Send msg


while True:
    data = input("Msg>>")

    sockfd.send(data.encode())
    if data == "close":
        # Close socket    
        sockfd.close()
        break
    data = sockfd.recv(1024)

    print("Recieved from server:", data.decode())

