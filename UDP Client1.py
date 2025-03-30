from socket import *

client = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("Client: ")

    client.sendto(data.encode(), ("192.168.1.14", 3333))
    data, server = client.recvfrom(2048)
    print(data.decode())