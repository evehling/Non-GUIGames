
#name(string), type (string), attack (int), health(int)
class Superhero(object):
#initialize attributes
    def __init__(self, name, type, attack):
        self.__name = name
        self.__type = type
        self.__attack = attack
        self.__health = 100

#below are all of the get methods for each attribute
    def getName(self):
        return self.__name

    def getAttack(self):
        return self.__attack

    def getHealth(self):
        return self.__health

    def getType(self):
        return self.__type
#subtracts a player's attack value from the other player's total health then converts to int
    def loseHealth(self, attack):
        self.__health = int(self.__health - attack)

#checks if health is below zero and return True if it is
    def isDead(self):
        if self.__health <= 0:
            return True
        else:
            return False
#string of player summary
    def __str__(self):
        msg = ("+ "+ self.__name.title() + " (" + self.__type + ") has " + str(self.__attack) + " attack \n  points and " + str(self.__health) + " health points." )
        return msg

#a fun extra little method I wrote to make the game more interesting
#that visually displays each player's HP
    def healthMeter(self):
        print("\t\t   " + self.__name.upper() + "'S HP")
#divides health by 10 then prints health bars accordingly
        bar = (self.__health) // 10
        print("0-------------------------------100HP")
        print("|"+ "||"*bar*2)
        print("-------------------------------------")
