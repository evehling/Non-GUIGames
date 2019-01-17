"""
Elisabeth Vehling
A11
ITP 115, fall 2018
vehling@usc.edi

Description: this code simulates a battle game using a class and various methods.
In this program I practiced creating new class objects as well as
importing and using classes from another file.


"""
#import from my other file
from Superhero import Superhero

def main():
    print('\n=====WELCOME TO BATTLEZONE!=====')
#if endfight changes, stops while loop running program
    endFight = 0
    while endFight == 0:
        print("\nFIGHTER 1")
        name1 = input("Enter name of Fighter 1: ")
        type1 = input("Is Fighter 1 a Hero or Villain? (H/V)")
#error check for hero and villain
        while type1.lower() not in "hv":
            print("Sorry, that's not an option.")
            type1 = input("Is Fighter 1 a Hero or Villain? (H/V)")
#assigns hero or villain depending on input
        if type1.lower() == "h":
            type1 = "hero"
        else:
            type1 = "villain"
        attack1 = input("Enter Fighter 1's attack points: ")
#checks if input is a digit or not
        while attack1.isdigit() == False:
            print("Sorry, that's not a valid option.")
            attack1 = input("Enter a number for Fighter 1's attack points: ")
#then converts input into int
        attack1 =int(attack1)

        print("\nFIGHTER 2")
        name2 = input("Enter name of Fighter 2: ")
        type2 = input("Is Fighter 2 a Hero or Villain? (H/V)")
        while type2.lower() not in "hv":
            print("Sorry, that's not an option.")
            type2 = input("Is Fighter 2 a Hero or Villain? (H/V)")
        if type2.lower() == "h":
            type2 = "hero"
        else:
            type2 = "villain"
        attack2 = input("Enter Fighter 2's attack points: ")
        while attack2.isdigit() == False:
            print("Sorry, that's not a valid option.")
            attack2 = input("Enter a number for Fighter 2's attack points: ")
        attack2 = int(attack2)
#create two new Superhero class objects using user input
        player1 = Superhero(name1, type1, attack1)
        player2 = Superhero(name2, type2, attack2)

        print("\n-------HERE'S YOUR FIGHTERS!-------")
#call __str__ method
        print(player1)
        print(player2)
        print("")
        print("------------BEGIN BATTLE!------------")

#deadplayer will stop this whle loop if it becomes true
        deadPlayer = False
        roundCounter = 1

        while deadPlayer == False:
            print("")
            print("============== ROUND", roundCounter,"==============")
#call getAttack method
            attack1 = Superhero.getAttack(player1)
            attack2 = Superhero.getAttack(player2)
#call loseHealth method
            Superhero.loseHealth(player1, attack2)
            Superhero.loseHealth(player2, attack1)

#called healthMeter method (just for kicks)
            Superhero.healthMeter(player1)
            Superhero.healthMeter(player2)
# call __str__ method to print player info
            print(player1)
            print("")
            print(player2)

#call isDead method and assign return value to aretheydead variable
            aretheydead1 = Superhero.isDead(player1)
            aretheydead2 = Superhero.isDead(player2)

#if both variables are true it's a tie
            if aretheydead1 == True and aretheydead2 == True:
                print("-------------------------------------")
                print("IT'S A TIE!")
                print("-------------------------------------")
#set deadPlayer to True to stop the while loop running a single game
                deadPlayer = True
                continueGame = input("\nDo you want to begin another battle? (Y/N)")
#error check
                while continueGame.lower() != "y" and continueGame.lower() != "n":
                    print("Sorry, that's not an option.")
                    continueGame = input("Do you want to begin another battle? (Y/N)")
#if response is n, sets endFight to 1 which ends the while loop running the
#entire program
                if continueGame.lower() == "n":
                    endFight = 1
                else:
                    pass
#repeats process like above, but these deal with if one player is dead and the other is not, returning a winner
            elif aretheydead1 == True and aretheydead2 == False:
                print("-------------------------------------")
                print("\t"+ Superhero.getName(player2).upper(), "WON THE BATTLE!")
                print("-------------------------------------")
                deadPlayer = True
                continueGame = input("\nDo you want to begin another battle? (Y/N)")
                while continueGame.lower() != "y" and continueGame.lower() != "n":
                    print("Sorry, that's not an option.")
                    continueGame = input("Do you want to begin another battle? (Y/N)")
                if continueGame.lower() == "n":
                    endFight = 1
                else:
                    pass

            elif aretheydead1 == False and aretheydead2 == True:
                print("-------------------------------------")
                print("\t" + Superhero.getName(player1).upper(), "WON THE BATTLE!!")
                print("-------------------------------------")
                deadPlayer = True
                continueGame = input("\nDo you want to begin another battle? (Y/N)")
                while continueGame.lower() != "y" and continueGame.lower() != "n":
                    print("Sorry, that's not an option.")
                    continueGame = input("Do you want to begin another battle? (Y/N)")
                if continueGame.lower() == "n":
                    endFight = 1
                else:
                    pass
##if none of these are true, deadPlayer remains False and program loops agaon
            else:
                deadPlayer = False
#adds num to round counter
            roundCounter = roundCounter + 1





main()

