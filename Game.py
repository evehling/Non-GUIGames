"""
Elisabeth Vehling
ITP 115, fall 2018
vehling@usc.edu
Description: in this assignment i practiced writing classes using inheritence to
simulate a vampire sucking blood from a human

Main:
"""
#import statements
from Being import Being
from Vampire import Vampire
from Human import Human

#prints list of humans
def printHumans(humanList):
    counter = 1
    for item in humanList:
        #use counter to increment menu number
        print(str(counter) + "." , item)
        counter = counter + 1
#performs feeding
def performFeeding(humanList, vamp):
    #use isStuffed method to check first if vampire is full
    if Vampire.isStuffed(vamp) == True:
        print("Sorry, your vampire is stuffed!")
    else:
        humanChoice = input("Enter the index number of a human:")
        #error check if not a digit
        while humanChoice.isdigit() == False:
            print("Sorry, that's not an option.")
            humanChoice = input("Enter the index number of a human:")
        #variable listRange takes the list range (0->n) and adds one to correct for 0
        listRange = len(humanList) + 1
        #checks if choice is in range of 1 to the listRange
        while int(humanChoice) not in range(1,listRange):
            print("\tSorry, that human is not a choice.")
            humanChoice = input("Enter the index number of a human:")
        #the choice is the index position -1 to correct for 1 starting point
        human = humanList[int(humanChoice) - 1]
        #chekcs if human object is alive
        check = Human.isAlive(human)
        if check == False:
            print("Sorry, that human is already dead!")
        elif Vampire.isStuffed(vamp) == True:
            print("Sorry, your vampire is already stuffed and can't suck any more blood!")
        #call suckblood method if everythign is good
        else:
            Vampire.suckBlood(vamp,human)
            print("BLOOD SUCKED! Now" , human)
            print(vamp)
#an extra function to make main cleaner
def printMenu():
    print("\nMENU OPTIONS:")
    print("[1] Print all humans")
    print("[2] Suck Blood")
    print("[3] Quit")



def main():
    nikias = Human("Max Nikias", 4, "O-")
    daniels = Human("JT Daniels", 1, "A")
    darnold = Human("Sam Darnold", 5, "AB")
    clay = Human("Clay Helton", 2, "L")
    #list of human objects
    humanList = [nikias, daniels, darnold, clay]
    #get vampire input from user
    userName = input("What is your vampire's name? ").title()
    userAnimal = input("What type of animal is your vampire? ")
    #create new vampire object set with 0 quarts of blood
    vampire = Vampire(userName, 0, userAnimal)
    userChoice = 0
    while userChoice != 3:
        #print menu choices
        printMenu()
        userChoice = input(">>")
        while userChoice.isdigit() == False:
        #error check
            print("Sorry, that's not an option.")
            userChoice = input("><")
        #convert to int
        userChoice = int(userChoice)
        if userChoice == 1:
            print("LIST OF HUMANS:")
            printHumans(humanList)
        #calls performFeeding
        elif userChoice == 2:
            print("CHOICES:")
            printHumans(humanList)
            print("")
            performFeeding(humanList, vampire)
        #quits and prints vampire message
        elif userChoice == 3:
            userChoice = 3
            print("")
            print(vampire)
            print("Thanks for playing!")
        else:
            print("Sorry, that's not an option.")

main()


