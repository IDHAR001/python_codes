import socket
from sql import conn
import datetime

# Create tcp socket
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sockfd.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# Bind addr
sockfd.bind(('0.0.0.0',80))

# Listen
sockfd.listen(5)

# Block connections which are waiting to be processed
print("Waiting for connect...")
connfd,addr = sockfd.accept()
print("Connected from", addr) 

# Get user ip & port
ip, port = addr

# send/recv msg
while True:
    data = connfd.recv(1024)

    # Get current recv time
    ct = datetime.datetime.now()

    # ct stores current time
    print("Store time:-", ct)

    # split time & date
    # date = str(ct).split(" ")[0]
    # time_stamp = str(ct).split(" ")[1]
    # print(date)
    # print(time_stamp)

    cursor = conn.cursor()
    if cursor:
        print("DB connected")
    client_msg = data.decode()
    insert_sql = "insert into chat_history(ip,msg,date_time) values('%s','%s','%s')" %(str(ip),str(client_msg),str(ct))
    print(insert_sql)
    cursor.execute(insert_sql)
    conn.commit()

    # sql_result = cursor.fetchone()
    # print(sql_result)
    print("Recieved:", data.decode())
    msg = "Server recieved your msg: " + data.decode()
    msg_bytes = msg.encode()
    n = connfd.send(msg_bytes) #Send bytes
    print("Send %d bytes"%n)
    if data == b"close\n":
    # Close socket    
        connfd.close()
        sockfd.close()
        break





