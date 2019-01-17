"""
Elisabeth Vehling
A10
ITP 115, Fall 2018
vehling@usc.edu

Description: This program simulates an animal daycare game using a class to represent each animal. In this
assignment I practiced creating classes, attributes, methods instance variables, functions,
and reading from CSV files.



"""

#class Animal(): public class for animals
#has methods __init__, __str__, play, feed, giveMedicine, sleep
class Animal(object):

#constructor method
#inputs: 1 for each attribute
#output: none
    def __init__(self, hunger, happiness, health, energy, age, name, species):
        self.hunger = hunger
        self.happiness = happiness
        self.health = health
        self.energy = energy
        self.age = age
        self.name = name
        self.species = species

#method play: increases animal's happiness by 10 and their hunger by 5
#inpt: none
#output: none
    def play(self):
#added 5 to hunger int, if more than 100 sets to 100 (repeated this for all of these methods that involved adding/subtracting ints)
        self.hunger = self.hunger + 5
        if self.hunger > 100:
            self.hunger = 100
        self.happiness = self.happiness + 10
        if self.happiness > 100:
            self.happiness = 100
        print("You played with", self.name +"!")

#method feed: decreases animal's hunger by 10
#input: none
#ouputL none
    def feed(self):
        self.hunger = self.hunger - 10
        if self.hunger < 0:
            self.hunger = 0
        print("You fed" , self.name + "!")

#method giveMedicine: decreases animals's happiness by 20 and increase health by 20
#input: none
#output: none
    def giveMedicine(self):
        self.happiness = self.happiness - 20
        if self.happiness < 0:
            self.happiness = 0
        self.health = self.health + 20
        if self.health > 100:
            self.health = 100
        print("You gave", self.name + "medicine!")

#method sleep: increases animal's energy by 20 and increases age by 1
#input: none
#output: none
    def sleep(self):
        self.energy = self.energy + 20
        if self.energy > 100:
            self.energy = 100
        self.age = self.age + 1
        if self.age > 1000:
            self.age = 100
        print(self.name , "went to sleep!")

#method __str__: string with info about the animal
#input: none
#output: string
    def __str__(self):
        msg = ("Name: " + self.name + " the " + self.species + "\nHealth: " + str(self.health) + "\nHappiness: " + str(self.happiness) + "\nHunger: " + str(self.hunger) + "\nEnergy: " + str(self.energy) + "\nAge: "+ str(self.age) + "\n***************************")
        return msg


#function loadAnimals: opens csv, creates new animal objects, stores in list that is returned
#input: string representig name of csv
#output: list of Animal objects
def loadAnimals():
#made empty list then opened file
    animalList = []
    animalCSV = open("animals.csv", "r")
    for line in animalCSV:
#for each line in csv, stripped of whitespace and \n
        line = line.strip()
        line = line.rstrip("\n")
#split each line by ,
        line = line.split(',')
#created new animal object for each line; converted index positions 0-4 to int because they're #
#used index position on each line to set each to an attribute
        newAnimal = Animal(int(line[0]), int(line[1]), int(line[2]), int(line[3]), int(line[4]), line[5], line[6])
#appended this new animal to the list of animals
        animalList.append(newAnimal)
    animalCSV.close()
    return animalList

#function displayMenu: print out menu with all possible options to user
#input:none
#output: none
def displayMenu():
    print("\nMENU OPTIONS:")
    print("[1] Play")
    print("[2] Feed")
    print("[3] Give Medicine")
    print("[4] Sleep")
    print("[5] Print an Animal's stats")
    print("[6] View All Animals")
    print("[7] Exit")

#function selectAnimal: prints out menu with animal's name/species and returns animal of user's choice
#input: list of animals
#output: selected animal object from list
def selectAnimal(animalList):
    print("[1] Ollie the Bunny \n[2] Murdock the French Bulldog \n[3] Socks the Cat \n[4] Peewee the Turtle \n[5] Milo the Labrador")
    userChoice = input(">> ")
    while userChoice not in "12345":
        print("Sorry, that's an invalid animal.")
        userChoice = input(">> ")
#subtracted 1 from the # the user chose bc the animal index positions start at 0-4 instead of 1-5
    animalChoice = animalList[int(userChoice)-1]
    return animalChoice

#function: saveAnimalInfo: saves updated info into new csv file
#input: list of animals
#output: none
def saveAnimalInfo(animalList):
    newFile = open("animalData.csv", "w")
#set c to a comma bc I was too lazy to type out a comma inbetween each attribute
    c = ","
#for each Animal object in the list, I converted each attribute back to a string and put a , between
#printed to the new csv file
#I wasn't sure if we were allowed to use the csv module so I just did it this way in case
    for animal in animalList:
        print(str(animal.hunger) + c + str(animal.happiness) + c + str(animal.health) + c + str(animal.energy)+ c + str(animal.age) + c + animal.name + c + animal.species, file = newFile)
    print("SUCCESS!")
    newFile.close()

def main():
#created list of animals
    animalList = loadAnimals()
    print("WELCOME TO ANIMAL DAYCARE!")
    continueGame = 0
#set while loop
    while continueGame != 1:
#displayed menu
        displayMenu()
        userChoice = input(">>")
#error check
        while userChoice not in "1234567":
            print("Sorry, that's not an option.")
            userChoice = input(">")
#convert choice to int after
        userChoice = int(userChoice)
#call play method
        if userChoice == 1:
            print("\nSELECT AN ANIMAL TO PLAY WITH:")
            animalChoice = selectAnimal(animalList)
            Animal.play(animalChoice)
#call feed method
        elif userChoice ==2:
            print("\nSELECT AN ANIMAL TO FEED:")
            animalChoice = selectAnimal(animalList)
            Animal.feed(animalChoice)
#call giveMedicine method
        elif userChoice ==3:
            print("\nSELECT AN ANIMAL TO GIVE MEDICINE:")
            animalChoice = selectAnimal(animalList)
            Animal.giveMedicine(animalChoice)
#call sleep method
        elif userChoice == 4:
            print("\nSELECT AN ANIMAL TO SLEEP:")
            animalChoice = selectAnimal(animalList)
            Animal.sleep(animalChoice)
#call selectAnimal function
        elif userChoice == 5:
            print("\nSELECT AN ANIMAL TO VIEW STATS:")
            print(selectAnimal(animalList))
#for each object in list, call __str__ method
        elif userChoice == 6:
            print("\n*ALL ANIMAL STATS*\n")
            print("***********************")
            for animal in animalList:
                print(animal)
            print("")
#end while loop
        elif userChoice == 7:
#set continue to 1
            continueGame = 1
#call saveAnimalInfo function
            saveAnimalInfo(animalList)
            print("Your daycare data has been saved!")
            print("THANKS FOR PLAYING ANIMAL DAYCARE")
#this handles if the user puts in "23" or "12" and not a single number
        else:
            print("Sorry, that's not an option.")

main()