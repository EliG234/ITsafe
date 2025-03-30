import random

class RockPaperScissors(object):
    def __init__(self):
        print("Rock, Paper, Scissors! Best of 5 - Good Luck!")
        self.player = 0
        self.computer = 0
        self.rounds = 0

    def play_round(self):
        self.rounds += 1
        print("Round {0}!".format(self.rounds))
        while True:
            player = input("[R]ock [P]aper [S]cissors > ").lower()
            if player in ["r", "p", "s"]:
                break
            print("Invalid input! Please choose R, P, or S")
        computer = random.choice(["r", "p", "s"])
        print("Computer chose: {0}".format(computer))
        Win_Rules = {
            "r": "s",
            "p": "r",
            "s": "p"
        }
        if player == computer:
             print("Tie!")
        elif Win_Rules[player] == computer:
             print("You win!")
             self.player += 1
        else:
             print("You lose!")
             self.computer +=1
        print("The score is:\nYou - {0}\nComputer - {1}".format(self.player, self.computer))

    def check_winner(self):
        if self.player == 3:
            print("Game Over! You win!")
            return True
        elif self.computer == 3:
            print("Game Over! You lost!")
            return True
        elif self.rounds == 5:
            print("Game Over! The final score is:\nYou - {0}\nComputer - {1}".format(self.player, self.computer))
            return True
        return False

    def __str__(self):
        if self.player == 3:
            return "You win the game! Final score: You - {0}, Computer - {1}".format(self.player, self.computer)
        elif self.computer == 3:
            return "You lose the game! Final score: You - {0}, Computer - {1}".format(self.player, self.computer)
        elif self.rounds == 5:
            return "Game is a draw! Final score: You - {0}, Computer - {1}".format(self.player, self.computer)
        else:
            return "Current score: You - {0}, Computer - {1}, Rounds: {2}".format(self.player, self.computer,
                                                                                  self.rounds)


game = RockPaperScissors()
while True:
    game.play_round()
    if game.check_winner():
        break
    print(game)




