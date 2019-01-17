"""
Being Class (Parent Class)

"""
class Being(object):
#constructor, name = str, quarts = int
    def __init__(self, name, quarts):
        self.__name = name
        self.__quarts = quarts
#getters and setters
    def getName(self):
        return self.__name
    def getQuarts(self):
        return self.__quarts
    def setName(self, name):
        self.__name = name
    def setQuarts(self, quarts):
        self.__quarts = quarts
#increases being's quarts by 1
    def increaseQuarts(self):
        self.__quarts = self.__quarts + 1
#decreases being's quarts by 1
    def decreaseQuarts(self):
        self.__quarts = self.__quarts - 1
