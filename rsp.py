import sys
import random
from enum import Enum


# set class for constantly used variables.
class RPS(Enum):
    ROCK = 1
    SCISSORS = 2
    PAPER = 3


print("")
playerchoice = input("Please enter \n1 for rock, \n2 for scissors or \n3 for paper\n\n")
player = int(playerchoice)

# exit when players' inputs are not in the correct range
if player > 3 or player < 1:
    sys.exit("Your must enter 1, 2 or 3")

computerchoice = random.choice("123")
computer = int(computerchoice) #Overwriting computerchoice with int

# using variables for clean code.
win = "😄You win🏆🥇"
lose = "👽Computer win🏆"
print(
    "You chose "
    + str(RPS(player)).replace("RPS.", "")
    + " and Computer chose "
    + str(RPS(computer)).replace("RPS.", "")
    + ".\n"
)


# no need to set each case of lose
if player == 1 and computer == 2:
    print(win)
elif player == 2 and computer == 3:
    print(win)
elif player == 3 and computer == 1:
    print(win)
elif player == computer:
    print("Tie game!!")
else:
    print("Computer wins")
print("")
