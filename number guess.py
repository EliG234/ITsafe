import random

startup=input("[C]ontinue last game/[N]ew game > ").lower()
if startup=="c":
    save=open("save.db", "r")
    data=save.read()
    data=data.split("|")
    rand=int(data[0])
    tries=int(data[1])
    save.close()

else:
    rand = random.randint(1,1000)
    tries = 0

while True:
    guess=input("To save game and exit press [Q]\nGuess the number! > ").lower()
    if guess=="q":
        save=open("save.db","w")
        save.write("{0}|{1}".format(rand,tries))
        save.close()
        print("Game saved! See ya next time!")
        exit(0)
    else:
        guess=int(guess)
        tries +=1
    if guess>rand:
        print("Too high! Try again!")
        continue
    elif guess<rand:
        print("Too low! Try again!")
        continue
    else:
        continue


print("You guessed it!\n Game over!")
print("Number of tries : " + str(tries))

while True:
    endgame=input("[N]ew game\n [E]xit").lower()
    if  endgame=="e":
        exit(0)
    else:
        continue






