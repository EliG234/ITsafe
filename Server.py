from socket import *

import threading

server = socket(AF_INET, SOCK_STREAM)
server.bind(("0.0.0.0",1234))
server.listen(5)
users=[]

def recieve(myclient,addr):
    while True:
        data = myclient.recv(2048).decode()
        print("User {0}:{1}:".format(addr[0],addr[1]), data)
        if data == "exit":
            myclient.close()
            break
        else:
            forward_message(data,myclient,addr)

def forward_message(data,sender_socket, sender_addr):
        for client, client_addr in users:
            if client != sender_socket:
                client.sendall(f"User {sender_addr[0]}:{sender_addr[1]} : {data}".encode())

        """chat = input("[+] You > ")
        myclient.sendall(chat.encode())

        if chat == "exit":
            myclient.close()
            break"""



while True:
    client,addr = server.accept()
    users.append((client,addr))
    print ("Connected from user: {0}".format(addr))
    t1=threading.Thread(target=recieve,args=(client, addr))
    t2=threading.Thread(target=forward_message)
    t1.start()



server.close()