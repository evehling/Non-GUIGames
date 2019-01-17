"""
Elisabeth Vehling
A7
ITP 115, Fall 2018
vehling@usc.edu
Description: I created a program that simulates a two player tic tac toe game using loops, lists and functions.

"""
import TicTacToeHelper
import random

#function isValidMove: looks a spot on the board and returns T if spot is open
#and F is spot is taken/out of range
#input: list representing the board, int corresponding to index position
#output: boolean
def isValidMove(boardList, spot):
    if 0<=spot<=8:
        space = boardList[spot]
        if space.lower() == "x":
            return False
        elif space.lower() == "o":
            return False
        else:
            return True
    else:
        return False

#function updateBoard: takes current board list and places player's letter in specified spot
#input: list representing board, int corresponding to index position, string representing ("x" or "o")
#output: none
def updateBoard(boardList, spot, playerLetter):
    boardList[spot] = playerLetter

#function printPrettyBoard(): prints a ~pretty~ version of uglyboard
#input: list of board
#output:none
def printPrettyBoard(board_list):
    print()
    counter = 0
    for i in range(3):
        for j in range(3):
            if counter != 2 and counter !=5 and counter != 8:
                print(board_list[counter],  end=" | ")
#^^if the counter was at not a 2,5,or 8 (aka the last number of the row) I printed a vertical boundary
            elif counter == 2:
                print(board_list[counter])
                print("- - - - -", end="")
#^^if the counter was at 2 or 5 (aka the end of a row) I printed the horizontal boundary
            elif counter == 5:
                print(board_list[counter])
                print("- - - - -", end="")
            else:
                print(board_list[counter])

            counter += 1

        print()


#function: computerMove(): generates random number for computer's move
#input:none
#output: none

def computerMove():
    move = random.randrange(0,9)
    return move

#function playGame: has list of board, keeps track of moves, lets player take turns til game is over
#alternate between player x and o, asks player for position, etc.
#inputs:none
#output: none
def playGame():
    list = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    counter = 0
#counter: for keeping track of moves
    checker =""
#checker: for evaluating whether game is over
    move = 0
#move: for alternating x's and o's

    gamePlay = input("Do you want to play against a computer? (y/n)")
    while gamePlay.lower() not in "yn":
        print("Sorry, that's not a choice.")
        gamePlay = input("Do you want to play against a computer? (y/n)")
    if gamePlay.lower() == "n":
        starter = input("Which player wants to start? (x/o)?")
        while starter.lower() not in"xo":
            print("Sorry, that's not an option.")
            starter = input("Which player wants to start? (x/o)?")
        if starter.lower() == "x":
            move = 0
#^^assigned move to 0 or 1 depending on the choice, bc below I have 0 and 1 alternating the moves depending on if the move is even or odd
        else:
            move =1
        printPrettyBoard(list)
        while checker != "x" and checker != "o" and checker != "s":
            if move % 2 == 0:
#^^if the move is even, it's x's turn and if its odd it's o's
                print("Player X's move:")
                letter = "x"
            else:
                print("Player O's move:")
                letter = "o"
            indexPosition = (input("Which spot will you choose?"))
            while indexPosition not in "0123456789":
                print("Sorry, that's not a valid spot.")
                indexPosition = (input("Which spot will you choose?"))
            indexPosition = int(indexPosition)
            while isValidMove(list, indexPosition) == False:
                print("Sorry that's not a valid spot")
                indexPosition = (int(input("Which spot will you choose?")))

            updateBoard(list, indexPosition, letter)
            printPrettyBoard(list)
            counter = counter + 1
            move = move + 1
            checker = TicTacToeHelper.checkForWinner(list, counter)
            if checker == "x":
                print("Player X WINS! :-)")
            elif checker == "o":
                print("Player O WINS! :-)")
            elif checker == "s":
                print("STALEMATE :-/")
    else:
        printPrettyBoard(list)
        while checker != "x" and checker != "o" and checker != "s":
            if move % 2 == 0:
                print("Your move:")
                letter = "x"
                indexPosition = (input("Which spot will you choose?"))
                while indexPosition not in "0123456789":
                    print("Sorry, that's not a valid spot.")
                    indexPosition = (input("Which spot will you choose?"))
                indexPosition = int(indexPosition)
                while isValidMove(list, indexPosition) == False:
                    print("Sorry that's not a valid spot")
                    indexPosition = (int(input("Which spot will you choose?")))

                updateBoard(list, indexPosition, letter)
                printPrettyBoard(list)
                counter = counter + 1
                move = move + 1
                checker = TicTacToeHelper.checkForWinner(list, counter)
                if checker == "x":
                    print("YOU WIN! :-)")
                elif checker == "o":
                    print("COMPUTER WINS! :-(")
                elif checker == "s":
                    print("STALEMATE :-/")
            else:
                print("Computer's move:")
                letter = "o"
                indexPosition = computerMove()
                while isValidMove(list, indexPosition) == False:
                    indexPosition = computerMove()
                updateBoard(list, indexPosition, letter)
                printPrettyBoard(list)
                print("Computer placed an o at", indexPosition)
                counter = counter + 1
                move = move + 1
                checker = TicTacToeHelper.checkForWinner(list, counter)
                if checker == "x":
                    print("YOU WIN! :-)")
                elif checker == "o":
                    print("COMPUTER WINS! :-(")
                elif checker == "s":
                    print("STALEMATE :-/")


#while loop continueGame is true
def main():
    print("LET'S PLAY TIC TAC TOE!\n")
    continueGame = True
    while continueGame != False:
        playGame()
        endGame = input("Do you want to play again? (y/n)")
        if endGame.lower() == "y":
            continueGame = True
        else:
            continueGame = False
    print("Thanks for playing!")


main()
