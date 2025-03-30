def welcome():
    name=input("What is your name? ")
    print("Welcome ", format(name)+"!")

def summary(number1, number2, number3):
    result = number1+number2+number3
    print(result)

def test_argv(*args):
    if args is not None:
        print (args)

def calculator():
    while True:
        num1= int(input("Enter first number > "))
        num2= int(input("Enter second number > "))
        result = 0
        mathaction = input("Select action: \n [A]dd  \n [S]ubtract \n [M]ultiply \n [D]ivide \n > ").lower()

        if mathaction== "a":
            result = (num1+num2)
        elif mathaction == "s":
            result =num1-num2
        elif mathaction == "m":
            result = num1*num2
        elif mathaction == "d":
            if num2 != 0:
                result = num1/num2
            else:
                return "Cannot divide by 0!"
        else:
            return "Please select A,S,M or D"

        print(f"Result = {result}")

        startover = input("Would you like to start over? ").lower()
        if startover == "n":
            print("Thank you for using me!")
            break
        else:
            continue

def get_ip():

    adapter=input("Which adapter are you using?\n(E)thernet\n(W)ifi\n> ").lower()
    if adapter=="e":
        import os
        output=os.popen("ipconfig").read()
        ip_add = None
        e_lines =output.splitlines()
        for i, line in enumerate(e_lines):

           if "Ethernet adapter Ethernet:" in line:
               #ip_line = line.splitlines()
               for j in range(i, len(e_lines)):
                    if "IPv4 Address" in e_lines[j]:
                        ip_add=e_lines[j].split(": ")[1].strip()
                        return ip_add






