"""
Elisabeth Vehling
ITP 115, Fall 2018
Assignment 6
vehling@usc.edu

Description: A program that simulates a game of Rock Paper Scissors by practicing
using loops, variable declaration/assignment and using functions

"""
import random

#function displayMenu: displays the game rules to the user
#input: none
#output: none
def displayMenu():
    print("\nRULES:")
    print("Rock smashes Scissors.")
    print("Scissors cut Paper,")
    print("Paper covers Rock.")
    print("If both choices are the same, it's a tie.")
    print("Choose: [0] Rock [1] Paper [2] Scissors")

#function getComputerChoice: randomly chooses an integer for computer's move
#input: none
#output: returns a random integer between 0 and 2
def getComputerChoice():
    integerRand = random.randrange(0,3)
    return integerRand

#function getPlayerChoice: asks the user for their choice 0=rock, 1=paper, 2=scissors
#input: none
#output: integer that represents choice
#side effects: if user doesn't enter a valid choice, will prompt them again
def getPlayerChoice():
    choice = (input("Enter [0] Rock, [1] Paper, or [2] Scissors:"))
    while choice != "1" and choice != "2" and choice != "0":
        choice = (input("Enter [0] Rock, [1] Paper, or [2] Scissors:"))
    choice = int(choice)
    return choice

#function playRound: simulates game and keeps track of who the game
#inputs: two integers, getComputerChoice (0,1,2) and getPlayerChoice (0,1,2)
#outputs: returns -1 if computer won, 1 if player won, 0 if tie
def playRound(computerChoice, playerChoice):

    result = playerChoice - computerChoice
    if result == 0:
        winner = 0
    elif result == -2:
        winner = 1
    elif result == 2:
        winner = -1
    elif result == 1:
        winner = 1
    elif result == -1:
        winner= -1
    return winner

#function continueGame: asks user if they want to continue, then returns true or false bool
#input: none
#output: boolean value
#side effects: if user doesn't enter y or n, they will be prompted again
def continueGame():
    continueG = input("Do you want to continue playing? (y/n)")
    while continueG.lower() not in "yn":
        continueG = input("Do you want to continue playing? (y/n)")
    if continueG.lower() =="y":
        return True
    elif continueG.lower() == "n":
        return False
    else:
        pass

def main():
    #below are the variables for the results counters and continuePlaying
    compCounter = 0
    playCounter = 0
    tieCounter =0
    conPlay = True
    print("WELCOME TO ROCK PAPER SCISSORS!")
    while conPlay == True:
        displayMenu()
        yourMove = input("\nWhat's your move?")
    #prompts user to continue entering a valid number
        while yourMove not in "012":
            print("Sorry, that's not a choice.")
            yourMove = input("\nWhat's your move?")
    #converted input to int after to avoid program crashing
        yourMove = int(yourMove)

    #used the if/else statements below to print the user's choice
        if yourMove == 0:
            print("\nYou played Rock.")
        elif yourMove == 1:
            print("\nYou played Paper.")
        else:
            print("\nYou played Scissors.")
    #assigned the return value from playRound to the variable results
        results = (playRound(getComputerChoice(), yourMove))

    #below is an unneccesarily long series of if/elif statements to print
    #computer's choice. I did it based off of the user's choice and the results
    #of the game i.e win/loss/tie
        if yourMove == 0 and results == 1:
            print("Computer played Scissors.")
        elif yourMove == 0 and results == -1:
            print("Computer played Paper.")
        elif yourMove == 0 and results == 0 :
            print("Computer also played Rock.")
        elif yourMove == 1 and results == 1:
            print("Computer played Rock.")
        elif yourMove == 1 and results == -1:
            print("Computer played Scissors.")
        elif yourMove == 1 and results == 0:
            print("Computer also played Paper.")
        elif yourMove == 2 and results == 0:
            print("Computer also played Scissors.")
        elif yourMove == 2 and results == 1:
            print("Computer played Paper.")
        elif yourMove == 2 and results == -1:
            print("Computer played Rock.")

    #used results to print results of game and added 1 to the
    #corresponding win/tie counter
        if results == 1:
            print("You won! :-)\n")
            playCounter = playCounter + 1
        elif results == -1:
            print("Computer won! :-(\n")
            compCounter = compCounter + 1
        else:
            print("It's a tie. :-/\n")
            tieCounter = tieCounter + 1
    #assinged conPlay to the return bool from continueGame
        conPlay = continueGame()
    #printed final results
    print("---------------------")
    print("\nFINAL RESULTS")
    print("Your total wins:", playCounter)
    print("Computer's total wins:", compCounter)
    print("Total ties:", tieCounter)
    if playCounter > compCounter:
        print("\nYou were on fire!")
    elif compCounter > playCounter:
        print("\nYikes, better luck next time...")
    else:
        print("\nYou read eachother's minds!")
    print("THANKS FOR PLAYING!")


main()