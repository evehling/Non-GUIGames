"""
Elisabeth Vehling
ITP 115, Fall 2018
Assignment 2
vehling@usc.edu

Description: Vending machine that calculates the change for
the user and choose your own adventure game using if/else/elif statements


"""

#Part 1: Harry Potter Vending Machine

#below I set up the exchange rate between coins and set sicklechange to 0 to use for later:
knutValue = 1
sickleValue = knutValue*29
galleonValue = knutValue*493
sickleChange = 0

#below I set the variables of each product with their price in knuts:
butterbeerPrice = knutValue*64
quillPrice = knutValue*90
theDailyProphetPrice = knutValue*13
bookOfSpellsPrice = knutValue*600

#I started the user prompt below:
print("\nWelcome to the Harry Potter Vending Machine!\n")
print("     ITEM                PRICE")
print(" [A] Butter Beer       : 64 knuts \n [B] Quill             : 90 knuts \n [C] The Daily Prophet : 13 knuts \n [D] Book of Spells    : 600 knuts")
userSelection = input("\nPlease select an item: ")

#I outputted the user's choice back to them, and if they didn't choose from one of
#the options I put in a while loop until they did
#I also created a new variable, userCharge that would be assigned the value of
#one of the items for use in calculations later

if userSelection.capitalize() == "A":
    print("\nYou selected a Butter Beer.")
    userCharge = butterbeerPrice
elif userSelection.capitalize() == "B":
    print("\nYou selected a Quill.")
    userCharge = quillPrice
elif userSelection.capitalize() == "C":
    print("\nYou selected The Daily Prophet.")
    userCharge = theDailyProphetPrice
elif userSelection.capitalize() == "D":
    print("\nYou selected a Book of Spells.")
    userCharge = bookOfSpellsPrice
else:
    while userSelection.capitalize() not in "ABCD":
       print("You have entered an invalid option.")
       userSelection = input("Please select an item: ")
       if userSelection.capitalize() == "A":
           print("\nYou selected a Butter Beer.")
           userCharge = butterbeerPrice
       elif userSelection.capitalize() == "B":
           print("\nYou selected a Quill.")
           userCharge = quillPrice
       elif userSelection.capitalize() == "C":
           print("\nYou selected The Daily Prophet.")
           userCharge = theDailyProphetPrice
       elif userSelection.capitalize() == "D":
           print("\nYou selected a Book of Spells.")
           userCharge = bookOfSpellsPrice

#below is the discount calculation:
#I began with the discount prompt

discount = input("\nWould you be willing to share your purchase on Instagram\nfor a 5 knut discount?(Y/N): ")

if discount.capitalize() == "Y":
    userCharge = (userCharge - 5)
    print("\nYour discounted cost is:", userCharge , "knuts.")
elif discount.capitalize() == "N":
    print("Your cost is:" , userCharge , "knuts.")
else:
    while discount.capitalize() not in "YN":
        discount = input("Please enter Y/N: ")
        if discount.capitalize() == "Y":
            userCharge = (userCharge - 5)
            print("\nYour discounted cost is:", userCharge, "knuts.")
        elif discount.capitalize() == "N":
            print("Your cost is:", userCharge, "knuts.")

#the next section I allowed the user to input their own amount of each of the coins.
#to force the user to only input numbers, I used a while loop to reprompt the user
#each time their input was not a in my string of numbers. then I converted the input
#to an integer after when I converted the galleons and sickles the user inputted back
#into knuts.
print("\n\tPAYMENT METHODS")
payGalleons= input("How many Galleons are you paying with?: ")
while payGalleons not in "0123456789":
    print("Invalid option. Please enter a number.")
    payGalleons = input("How many Galleons are you paying with?: ")

paySickles = input("How many Sickles are you paying with?: ")
while paySickles not in "0123456789":
    print("Invalid option. Please enter a number.")
    payGalleons = input("How many Sickles are you paying with?: ")

payKnuts = input("How many Knuts are you paying with?: ")
while payKnuts not in "0123456789":
    print("Invalid option. Please enter a number.")
    payKnuts = input("How many Knuts are you paying with?: ")


payGalleons = int(payGalleons) * int(galleonValue)
paySickles = int(paySickles) * int(sickleValue)
knutsChange = 0
#the userPay variable represents the total amount of knuts the user has inserted
#the knuts change variable subtracts the charge (price of item in knuts) from the user's input

userPay = payGalleons + paySickles + int(payKnuts)
#I added in this while loop in case the amount of coins the user put in is less than the cost. the
#loop will keep prompting the user until they enter more than the charge

while userPay <= userCharge:
    print("\nYou have not inserted enough for:", userCharge," knuts. Please insert more coins." )
    print("\n\tPAYMENT METHODS")
    payGalleons = input("How many Galleons are you paying with?: ")
    while payGalleons not in "0123456789":
        print("Invalid option. Please enter a number.")
        payGalleons = input("How many Galleons are you paying with?: ")

    paySickles = input("How many Sickles are you paying with?: ")
    while paySickles not in "0123456789":
        print("Invalid option. Please enter a number.")
        payGalleons = input("How many Sickles are you paying with?: ")

    payKnuts = input("How many Knuts are you paying with?: ")
    while payKnuts not in "0123456789":
        print("Invalid option. Please enter a number.")
        payKnuts = input("How many Knuts are you paying with?: ")

    payGalleons = int(payGalleons) * int(galleonValue)
    paySickles = int(paySickles) * int(sickleValue)
    userPay = payGalleons + paySickles + int(payKnuts)

knutsChange = (userPay - userCharge)

#using the if statement below to determine whether we need to give any galleon change first. then, if
#the remainder of the first division was greater than 29 (a sickle), i did the same process for sickles.
#if not i jsut returned the user the remainder of the change in knuts. There is also an option in case
#the user inputs exact change or if the payment in knuts is greater than 29 but less than 493. if the
#the change is less than 29, the user just gets the change in knuts.

if knutsChange >= 493:
    galleonChange = knutsChange // 493
    knutsChange2 = knutsChange % 493
    if knutsChange >= 29:
        sickleChange = knutsChange2 // 29
        knutsChange2 = knutsChange % 29
        print("\nYour change is", galleonChange, "galleons,",sickleChange, "sickles, and", knutsChange2, "knuts. (Total change in knuts: " + str(knutsChange) + ")")
    else:
        print("\nYour change is", galleonChange, "galleons and", knutsChange2, "knuts. (Total change in knuts: " + str(knutsChange) + ")")

elif knutsChange >= 29:
    sickleChange = knutsChange // 29
    knutsChange2 = knutsChange % 29
    print("\nYour change is", sickleChange, "sickles and", knutsChange2, "knuts. (Total change in knuts: " + str(knutsChange) + ")")
elif knutsChange == 0:
    print("You have no change")
else:
    print("Your change is " +str(knutsChange)+ " knuts.")

#Part 2: Choose Your Own Adventure:
#I used while loops to make sure the user chooses from one of the options they're supposed to


print("\n\tCHOOSE YOUR OWN ADVENTURE: \'LOST IN THE WOODS\'")
print("\nIt was a dark and stormy night...You are lost in a thick, dark, forest.\nUp ahead in the distance, you see a faint yellow flickering light. ")
travelChoice = input("Will you go towards it? (Y/N): ")

while travelChoice.capitalize() not in "YN":
    print('You only have two options.')
    travelChoice = input("Will you go towards it? (Y/N): ")
if travelChoice.capitalize() == "Y":
    print("\nYou stumble through the rain towards the light. It takes about 15 minutes, but\neventually you reach a dilapidated cabin with a single flickering porch light.")
    cabinChoice = input("\nDo you enter the cabin and get out of the rain storm? (Y/N): ")
    while cabinChoice.capitalize() not in "YN":
        print('You only have two options.')
        cabinChoice = input("Do you enter the cabin and get out of the rain storm? (Y/N): ")
    if cabinChoice.capitalize() == "Y":
        print("\nYou push open the creaky front door. In front of you are three doorways:\n[1]The first leads into a kitchen.\n[2]The second leads to a dark flight of stairs\n[3]The third leads to a bedroom.")
        doorChoice = input("Which door will you choose? (1/2/3): ")
        while doorChoice not in "123":
            doorChoice= input("There's no turning back now. Which door will you choose? (1/2/3):")
        if doorChoice == "1":
           print("\nYou head into the kitchen and see a pantry in the corner. Your stomach grumbles.")
           pantryOption = input("You're not sure when the rain will let up. Do you look for some food in the pantry? (Y/N): ")
           while pantryOption.capitalize() not in "YN":
               pantryOption = input("You're not sure when the rain will let up. Do you look for some food? (Y/N): ")
           if pantryOption.capitalize() == "Y":
               print("\nYou yank open the door to the pantry. Instantly, you see them: a glorious box of Oreos.\nYou snatch the box and begin shoving them into your mouth. Suddenly, you feel a hand grab your shoulder.\n'What are you doing eating my OREOS?!' a deep voice shouts. Something hits you over the head. and you fall to the ground.")
               print("\nThe next day, reports of a murderer hiding out in an abandoned cabin begin flooding in: \n'A person was found dead on the floor of an abandoned cabin, covered in Oreo crumbs. The suspected murderer has not been caught.\'")
           else:
               print("\nThe food is probably all expired anyway. You head back out of the kitchen and into the bedroom.\n")
               print("A nap sounds really nice right now. You lay down on the bed and close your eyes for a second.\nYou wake up with a flashlight in your face. It's your pal, Park Ranger Dave!\n'Good thing we got to you first. An escaped murderer has been camped out in the kitchen here for a few days. We just caught him.\nHopefully you've learned your lesson about exploring sketchy cabins.\'")
        elif doorChoice == "2":
           print("\nYou start heading up the creaky stairs. Suddenly a shadow darts out in front of you! Its a man with a scraggly beard! He shoves you down the stairs.\nYou wake up with a flashlight shining in your face. It's your pal, Park Ranger Dave!\n'Good thing we got to you. An escaped murderer has been camped out in here for a few days. We just caught him.\nHopefully you've learned your lesson about camping in sketchy cabins.\'")
        else:
           print("\nYou head into the bedroom. A nap sounds really nice right now. You lay down on the bed and close your eyes for a second.\nYou wake up with a flashlight in your face. It's your pal, Park Ranger Dave!\n'Good thing we got to you first. An escaped murderer has been camped out in the kitchen here for a few days. We just caught him.\nHopefully you've learned your lesson about exploring sketchy cabins.\' ")
    else:
        print("\nYour spider senses are probably right. That cabin was hecka sketchy. \nYou head back into the woods and run into Park Ranger Dave who gives you a lift back to town. \nOn the car radio you hear a news report about an escaped murderer hiding out in an abandoned cabin in the woods.\nSpooky.")
else:
    print("\nYou turn the other way. Following sketchy lights into the forest is probably a bad idea.\n20 minutes later you run into your pal Park Ranger Dave. He gives you a lift back to town.\nIn the car, you hear a news report on the radio about an escaped murderer hiding out in an abandoned cabin.\nSpooky.")
