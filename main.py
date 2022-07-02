from ast import Break
import random
from tokenize import Number

# import ipdb
# ipdb.set_trace()

print("Welcome to this CLI Rock-Paper-Scissors Game. Enjoy!!!")

options = ['Rock', 'Paper', 'Scissors']

name = input("Let's know you. Enter your namee: ")

ComputerScore = 0
PlayerScore = 0
NumberOfRounds = 0

gameOn = True

print(f"Welcome {name.title()}")


while NumberOfRounds < 5:
    ComputerOption = random.choice(options)
    PlayerOption = input("Choose one. Rock or Paper or Scissors : ").title()

    print("So what do we have here. Let's see.")
    print(f"Computer's option: {ComputerOption}")
    print(f"{name.title()}'s option: {PlayerOption}")

    if ComputerOption == PlayerOption:
        print("Shoot. Seems it's a tie.")
        NumberOfRounds += 1

    elif (ComputerOption == 'Rock' and PlayerOption == 'Scissors') or (ComputerOption == 'Scissors' and PlayerOption == 'Paper') or (ComputerOption == 'Paper' and PlayerOption == 'Rock'):
        print("Aiit. The Computer wins this round.")
        ComputerScore += 1
        NumberOfRounds += 1

    elif (PlayerOption == 'Rock' and ComputerOption == 'Scissors') or (PlayerOption == 'Scissors' and ComputerOption == 'Paper') or (PlayerOption == 'Paper' and ComputerOption == 'Rock'):
        print(f"Nice. {name.title()} wins this time.")
        PlayerScore += 1
        NumberOfRounds += 1

    else:
        print("Eish! Seems that doesn't work./nMake a valid choice.")
        NumberOfRounds += 0
        ComputerScore += 0
        PlayerScore += 0

    print("-------------------------")
    print("")
    print(f"Round No: {NumberOfRounds}")
    print("------ Score Board ------")
    print(f"{name.title()}: {PlayerScore}  |  Computer: {ComputerScore}")
    print("==============================")
    print("")

    if NumberOfRounds == 5:
        gameOn = False
        break


if PlayerScore == ComputerScore:
    print("A tie!!")
elif PlayerScore > ComputerScore:
    print(f"WooHoo!! Nice one {name.title()}, You won the game.")
else:
    print(
        f"Oops Computer won the game!! Better luck next time {name.title()}!")
