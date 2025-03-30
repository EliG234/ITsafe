import random
from random import randint


class NumberGuess(object):
    def __init__(self):
        self.number = random.randint(1,1000)
        self.tries = 0

    def get_guess(self):
        guess = int(input("Your guess > "))
        return guess

    def check_guess(self, guess):
        self.tries += 1

        if guess == self.number:
            print("Yes! you got it in {0} tries!".format(self.tries))
            return True
        elif guess > self.number:
            print("whoops, too high! try again!")

        else:
            print(" ooh, too low! Try again!")
        return False
    def play(self):
        print("I'm thinking of a number between 1-1000! can you guess it?")
        while True:
            guess = self.get_guess()
            if self.check_guess(guess):
                    break


if __name__ == "__main__":
    game = NumberGuess()
    game.play()