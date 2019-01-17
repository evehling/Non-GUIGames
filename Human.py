"""
Human Class

"""
#import being class
from Being import Being

class Human(Being):
#constructor method, inherited attributes + new bloodtype
    def __init__(self, name, quarts, bloodType):
    #call parent class constructor for name and quarts
        super().__init__(name, quarts)
    #set bloodtype
        self.__bloodType = bloodType
#getters and setters
    def getBloodType(self):
        return self.__bloodType

    def setBloodType(self, bloodType):
        if bloodType != "":
            self.__bloodType = bloodType
#determines if human is alive
    def isAlive(self):
        #if more than 0 quarts, True
        if super().getQuarts() > 0:
            return True
        #if less than equal, False
        elif super().getQuarts() <= 0:
            return False
        else:
            return False
#print method
    def __str__(self):
        msg = super().getName() + " (human) has " + str(super().getQuarts()) + " quarts of " + self.__bloodType + " blood."
        return msg
