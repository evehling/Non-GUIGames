"""
Vampire class

"""
#import classes
from Being import Being
from Human import Human

#class attributes:
MAX_BLOOD = 5
HUNGER_LEVELS = ["starving", "hangry", "hungry", "content", "full", "stuffed"]


class Vampire(Being):
#constructor
    def __init__(self,name, quarts, animalForm):
    #call parent class for name and quarts
        super().__init__(name, quarts)
    #set new attribute
        self.__animalForm = animalForm
#getters and setters
    def getAnimalForm(self):
        return self.__animalForm
    def setAnimalForm(self, animalForm):
        if animalForm != "":
            self.__animalForm = self.__animalForm
#returns string of vampire's hunger status
    def getHunger(self):
        #calls parent class getter and converts to int
        hunger = int(super().getQuarts())
        #uses int as index for hunger_levels
        string = HUNGER_LEVELS[hunger]
        return string
#checks if vampire is full
    def isStuffed(self):
        #calls parent method getQuarts to get vampire blood amount
        #checks if this is equal to max
        if int(super().getQuarts()) == MAX_BLOOD:
            return True
        else:
            return False
#sucks blood
    def suckBlood(self,human):
        #increase quarts of self (vampire)
        Being.increaseQuarts(self)
        #decreae quarts of human object chosen
        Being.decreaseQuarts(human)
#print method
    def __str__(self):
        #call parent function to get name
        msg = super().getName() + " (a "+ self.getAnimalForm() + ") is " + self.getHunger() + "."
        return msg


