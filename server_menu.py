
def menu():
    print("""SERVER MANAGER
    ----------------------------
    1) show all clients
    2) execute command on client
    3) shutdown client
    4) close server
    """)

def get_all_clients(clients):
    counter = 0
    print("Clients:")
    for client in clients:
        counter+=1
        client_socket = client[0]  # Get the socket object
        print("{0} = Socket ID: {1}".format(counter, client_socket.fileno()))
    print("END")

def command(clients):
    get_all_clients(clients)
    client_id = int(input("[+] Select client > ")) - 1

    client_socket = clients[client_id][0]
    command_to_execute = input("[+] Command to execute > ")
    client_socket.sendall(command_to_execute.encode())
    result = client_socket.recv(2048).decode()
    print(result)

def shutdown_client(clients):
    get_all_clients(clients)
    client_id = int(input("[+] Select client > ")) - 1
    client_socket = clients[client_id][0]
    verify =input("This will terminate Client connection, continue? Y/N > ")
    if verify=="y":
        client_socket.sendall("exit".encode())
        client_socket.close()
        print("Client {0} disconnected".format(client_id+1))
        clients.pop(client_id)



