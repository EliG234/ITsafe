import os

command_list =[]

while True:
    command = input("Give me a Command (exit to stop) > ")
    if command == "exit":
        print("Exiting...")
        break

    command_list.append(command)

    #command_string = " ".join(command_list)

for command in command_list:
    print(f"Executing Command: {command}")
    try:
        output = os.popen(command).read()
        print(output)
    except Exception as e:
        print(f"Error executing '{command}': {e}")






