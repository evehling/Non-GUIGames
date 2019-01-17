"""
Elisabeth Vehling
ITP 115, Fall 2018
A4
vehling@usc.edu

Description: I created a word jumble game that randomizes a series of letters and asks the user to guess what the word is. Each hint the user uses will
deduct points from their total score. Users can access multiple hints if they choose! In the decryption part I created a program that encrypts and decrypts a
message that the user inputs (without affecting their spacing or punctuation). To create both of these, I practiced converting strings to lists, using for and while
loops, and manipulating lists.

"""
#PART 1: WORD JUMBLE
import random

#here are the rules:
print("\n\t\t\t\tWORD JUMBLE!")
print("RULES:\nYou begin with 30/30 points. Each guess will deduct one point.\nHints will be available after the first guess to help you, but \neach hint you use will deduct 5 points. If you guess right on\nthe first try, no points will be deducted. Good Luck!")

#first wrote the list of words
gameList = ["enterprise", 'california', "anaconda", "trojans", "porche", "endeavor","falcon" ]
#used random choice to choose a random word
gameWord = random.choice(gameList)
#made a copy of gameword and assigned it to copyword
copyWord = gameWord[:]
#made copyword into a list and assigned it to jword
jWord= list(copyWord)
#I set the variables wordPosition to a random index position in the word, the switched two of them
#at a time, doing a total of 3 swaps

wordPosition = random.randrange(len(jWord))
wordPosition2 = random.randrange(len(jWord))
jWord[wordPosition], jWord[wordPosition2] = jWord[wordPosition2], jWord[wordPosition]
wordPosition3 = random.randrange(len(jWord))
wordPosition4 = random.randrange(len(jWord))
jWord[wordPosition3], jWord[wordPosition4] = jWord[wordPosition4], jWord[wordPosition3]
wordPosition5 = random.randrange(len(jWord))
wordPosition6 = random.randrange(len(jWord))
jWord[wordPosition5], jWord[wordPosition6] = jWord[wordPosition6], jWord[wordPosition5]

#if after this first round of jumblihng the word somehow was the same as the original, I sent it through a second round
if jWord == list(copyWord):
    wordPosition = random.randrange(len(jWord))
    wordPosition2 = random.randrange(len(jWord))
    jWord[wordPosition], jWord[wordPosition2] = jWord[wordPosition2], jWord[wordPosition]
    wordPosition3 = random.randrange(len(jWord))
    wordPosition4 = random.randrange(len(jWord))
    jWord[wordPosition3], jWord[wordPosition4] = jWord[wordPosition4], jWord[wordPosition3]
    wordPosition5 = random.randrange(len(jWord))
    wordPosition6 = random.randrange(len(jWord))
    jWord[wordPosition5], jWord[wordPosition6] = jWord[wordPosition6], jWord[wordPosition5]
else:
    pass

#then I rejoined the list of letters into a string

jWord = ''.join(jWord)
print("\nThe jumbled word is: " + jWord)

#HINTS

if copyWord == "enterprise":
    hint = "The USS ... (NCC-1701)"
elif copyWord == "california":
    hint = "Flower is the Poppy."
elif copyWord == "anaconda":
    hint = "A Constricting reptile."
elif copyWord == "trojans":
    hint = "Fight On!"
elif copyWord == "porche":
    hint = "A luxury German auto."
elif copyWord == "endeavor":
    hint = "A Space shuttle."
elif copyWord == "falcon":
    hint = "Millenium..."
else:
    pass

#I set the variable guessCount to 0 and increased it by one each time the while loop is run to count
#the number of user guesses. I did the same with hintCount
guessCount = 0
hintCount = 0
userGuess = input("Input a guess: ")
askHint = " "
print("Enter H at anytime to receive a hint.")
while userGuess != copyWord:
    guessCount = guessCount + 1
    userGuess = input("Guess again: ")
    if hintCount in range(1) and userGuess.lower() == "h":
        print("\nThe first two letters of the word are: " + copyWord[0:2])
        hintCount = hintCount + 1
    elif hintCount in range(2) and userGuess.lower() == "h":
        print("\nHint: " +hint)
        hintCount = hintCount + 1
    elif hintCount in range(3) and userGuess.lower()=="h":
        print("\nThe first four letters of the word are: " + copyWord[0:4])
        hintCount = hintCount + 1
    elif hintCount in range(4) and userGuess.lower() == "h":
        print("Luke...use the force. ")
    elif hintCount > 4 and userGuess.lower()=="h":
        print("I can't help you anymore.")
    else:
        pass
print("\n"+copyWord.upper() + " is correct!")

#hint grammar fixer:
if hintCount == 1:
    hints = str(hintCount) + " hint."
else:
    hints = str(hintCount) + " hints."
#score calculator
if guessCount == 0:
    print("\nI grant you the rank of MASTER\nYour score is: 30/30!")
else:
    totalscore = 30 - (guessCount+(hintCount*5))
    if totalscore in range(25, 30):
        print("\nI grant you the rank of JEDI")
        print("\nYour total score is: " + str(totalscore)+ "/30 points.")
        print ("It took you " + str(guessCount) + " guesses and you used " + hints)
    elif totalscore in range(21, 25):
        print("\nI grant you the rank of PADAWAN")
        print("\nYour total score is: " + str(totalscore) + "/30 points.")
        print("It took you " + str(guessCount) + " guesses and you used " + hints)
    elif totalscore in range(15,21):
        print("\nI grant you the rank of YOUNG ANAKIN")
        print("\nYour total score is: " + str(totalscore) + "/30 points.")
        print("It took you " + str(guessCount) + " guesses and you used " + hints)
    elif totalscore in range(10, 16):
        print("\nI grant you the rank of WATTO")
        print("\nYour total score is: " + str(totalscore) + "/30 points.")
        print("It took you " + str(guessCount) + " guesses and you used " + hints)
    elif totalscore in range(5,11):
        print("\nI grant you the rank of BATTLE DROID")
        print("\nYour total score is: " + str(totalscore) + "/30 points.")
        print("It took you " + str(guessCount) + " guesses and you used " + hints)
    else:
        print("\nI grant you the rank of JAR-JAR BINKS")
        print("\nYour total score is: " + str(totalscore) + "/30 points.")
        print("It took you " + str(guessCount) + " guesses and you used " + hints)
print("\nPOINTS : RANK")
print("30     : JEDI MASTER")
print("25-29  : JEDI")
print("21-24  : PADAWAN")
print("15-20  : YOUNG ANAKIN ")
print("10-15  : WATTO")
print("5-10   : BATTLE DROID")
print("0-5    : JAR-JAR BINKS")


#PART 2:ENCRYPT/DECRYPT
print("\n\nENCRYPTION/DECRYPTION")
#I prompted the user for a message then made a copy of the string, then converted
#it into a list.
bet = input("\nEnter a message to encrypt:")
bet = bet[:]
alphabet = list(bet)

#I them prompted the user for a number between 1-25 and used a while loop to keep
#prompting the user if they do not enter a number within that range
#I decided not to include 0 because I figured that would defeat the purpose
# of a cipher.
userNum = int(input("Enter a number to shift by (1-25): "))
while userNum not in range(1, 26):
    print("Number not in range.")
    userNum = int(input("Enter a number between 1 and 25: "))
print("ENCRYPTING...\n")
print("ENCRYPTED MESSAGE: ", end="")
cypherWord = []
encrypt = ""
#for each letter (string: 'letter') in the list alphabet (the list copy of the
#user's word), I converted the character into ASCII. I looked up the range of the
#ASCII alphabet and found the letters a-z are numbers 97-122.

for letter in alphabet:
    asciiLetter = ord(letter)
#I used nested if/else statements to deal with characters that were not in the lowercase range of 97-122.
#I looked up the uppercase ASCII codes for A-Z (65-90). If the ASCII code was in this range, I added the
#userNum (aka the shift value) to the ASCII number. Using another if/else statement, If the value of the
#ASCII letter was outside the range of 90 (aka not an uppercase letter) I subtracted 90 from the larger value.
#Then, I added this difference to 65 and subtracted 1.
    if asciiLetter not in range(97,123):
        if asciiLetter in range(65,91):
           cypherLetter = asciiLetter + userNum
           if cypherLetter > 90:
               fixedShift =cypherLetter - 90
               cypherLetter= (fixedShift + 65 -1)

           else:
               pass
#I used another  if else statement to exempt punctuation from encryption (aka, characters
#that are not in the range 97-122 or in the range 65-90). I then assigned the asciiLetter
#to cypherLetter to keep the ASCII code the same (this way it won't be shifted
#like the letters will by  userNum)
        else:
            cypherLetter = asciiLetter
#Then I repeated the same process for lowercase letters (97-122) using the ASCII values for a-z
#if the shifted letter was greater than 122, I subtracted 122 from the larger number, then added 97 -1
    else:
        cypherLetter = asciiLetter + userNum
        if cypherLetter > 122:
            fixedShift = cypherLetter - 122
            cypherLetter = (fixedShift + 97 - 1)
        else:
            pass
#Then I reconverted the variable called
#cypherLetter to letters, then printed each one on the same line using end=" ".
    alphLetter = chr(cypherLetter)
    cypherWord.append(cypherLetter)
    print(alphLetter, end="")
#the cypherword variable is a list I made that stores the ASCII translation of the input message
#print(cypherWord)


print("\nDECRYPTING...\n")
print("DECRYPTED MESSAGE: ", end="")

#for each number in the list cypherword (the encrypted ascii values), I took a similar approach as the encryption but
#changed a few things:

for number in cypherWord:

#i first decrypted the lowercase letters (aka the range 97-122). I subtracted the userNum from it to revert the shift
    if number in range (97,123):
        decryptLetter = number - userNum
#to account for letters that ended up falling below the 97 range after the subtraction, I subtraced decryptLetter from 97 to get the difference.
#then I subtracted this difference from 122 to start from the end of the alphabet again
        if decryptLetter < 97:
            revertShift = 97 - decryptLetter
            decryptLetter = 122 - revertShift + 1
        else:
            pass
#then I repeated the process for uppercase letters (range 65-90), except using the boundary of 65 (A) instead of 97 (a) and 90 (Z) instead of 122 (z)
    elif number in range(65,91):
        decryptLetter = number - userNum
        if decryptLetter < 65:
            revertShift = 65 - decryptLetter
            decryptLetter = 90 - revertShift + 1
        else:
            pass
#if the number was not in one of these ranges, that meant it was a character so I kept the number the same as its original in the cypherword list
    else:
        decryptLetter = number
#then I converted each new number back into characters and printed them.
    translation = chr(decryptLetter)
    print(translation, end="")

print("\nORIGINAL MESSAGE:", bet)

