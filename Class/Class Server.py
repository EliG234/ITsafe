import threading
import time
from socket import *


class Server(object):
    def __init__(self):
        self.users = []
        self.socket = socket(AF_INET, SOCK_STREAM)

    def startup(self):
        self.socket.bind(("0.0.0.0",1234))
        self.socket.listen(5)
        print("Server started, waiting for connections...")
        threading.Thread(target=self.server_chat).start()
        while True:
            client, addr = self.socket.accept()
            self.users.append((client, addr))
            print("user {0} has connected".format(addr))
            threading.Thread(target=self.recieve, args=(client, addr)).start()


    def recieve(self, myclient, addr):
        while True:
            data = myclient.recv(2048).decode()
            print("User {0}:{1}:".format(addr[0], addr[1]), data)
            if data == "exit":
                myclient.close()
                break
            else:
                self.forward_message(data, myclient, addr)

    def forward_message(self, data, sender_socket, sender_addr):
        for client, client_addr in self.users:
            if client != sender_socket:
                client.sendall(f"User {sender_addr[0]}:{sender_addr[1]} : {data}".encode())

    def server_chat(self):
        while True:
            if not self.users:
                print("No users connected.")
                time.sleep(5)
                continue

            chat = input("Server: ")
            for client, addr in self.users:
                client.sendall(chat.encode())

Server().startup()