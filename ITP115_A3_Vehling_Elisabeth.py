"""
Vehling Elisabeth

ITP 115, Fall 2018

A3

vehling@usc.edu

Description: I created a program that translates a single word at a time from english
to Pig Elvish followed by a program that finds the largest integer out of the integers
the user inputs (without using a list). In both of these I used lots of while and for loops and
practiced manipulating strings.





"""

#PART 1: PIG ELVISH TRANSLAGOR

#imported the random mod to use later
import random
#first I started off the while loop by setting continueTranslator to "y"
print("Welcome to the Pig Elvish Translator!")
continueTranslator = "y"
while continueTranslator == "y":
    englishWord = input("\nPlease enter a word you'd like translated into Pig Elvish: ")

#I then made an index copy of the user's input using slicing
    translation = englishWord[:]

#Then I printed the translation from the first position to the last position
#(the total length of the word) and added the first letter

    translation = translation[1:len(translation)] + translation[0:1]

#For the next part I used an if else statement : if the length of the user's unput is greater
#than 4 I created a variable with a string of the vowels, then radomized it with random
#choice. I then added it to the end of the translation.


    if len(translation) >= 4:
        vowels = "aeiou"
        randomVowel = random.choice(vowels)
        translation = translation + randomVowel
    else:
        translation = translation + "en"
#I created a variable k  to hold my "k" string. if there is a "k" in the word,
#i used the  .replace() function to switch it with a c

    k = "k"
    for k in translation:
        translation = translation.replace("k","c")

#I used an if else statement to do the next part:
# if there is an "e" in the last position of the word,
#I cut the letter out of the original word and added the umlaut e instead

    if translation[-1] == "e":
        translation = translation[:len(translation)-1] + "ë"
    else:
        pass
#I used the .lower() to make everything lower case
    translation= translation.lower()

#then i used .capitalize() to capitalize the first letter of the new word
    translation = translation.capitalize()
    print("\'"+ englishWord.capitalize()+ "\'", "in Pig Elvish is:" , translation +".")
#if the user puts y (lower or capital, the program continues. if not it ends)
    continueTranslator = input("\nWould you like to answer another word?(Y/N): ")
    continueTranslator = continueTranslator.lower()

print("\nThanks for using the Pig Elvish Translator!")


#if you have time attempt the extra credit portion

#PART 2-LARGEST NUMBER

print("\nWelcome to the Largest Integer Finder")

#first I assigned the anotherIndex variable as Y to start off the first while loop
anotherIndex = "Y"
while anotherIndex.capitalize() == "Y":
    print("\nPlease input an integer greater than or equal to 0. Enter -1 to quit.")
#then i assigned the two variables i used in the next while loop to 0, i (for integer) and largestInt (for my
#greatest integer value.
    i = 0
    largestInt = 0
#in this loop, as long as i is greater than 0, the loop will continue (aka until the user puts in a negative #
    while i >= 0:
        integer = int(input("> "))
#i assigned i to the value that the user put into the 'integer' prompt
        i = integer
#then with the next loop, as long as i is greater than the largestInt value (0 to begin with), the largest
#int value will be reassgned to the integer value the user entered.
        while i > largestInt:
            largestInt = integer

    print("The largest integer is:", largestInt)
#I asked this prompt after to complete the first while loop. if the user says y, the loop will begin again
    anotherIndex= input("Would you like to find another largest number? (Y/N): ")
print("Thanks!")
