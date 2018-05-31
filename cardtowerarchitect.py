import math as m
import sys

def MainMenu(key):
    if key == True:
        print()
        input("Press any key to continue.")
    print()
    print("What would you like to do? ")
    return input("A. Calculate Potential Card Tower \nB. Measure Card Tower \nC. Build Card Tower \nD. Exit\n").lower()

def CalculationsMenu():
    print()
    input("Press any key to continue.")
    print()
    print("What calculations would you like to make?")
    return input("A. Collection Stats \nB. Card Towers \nC. Main Menu\n").lower()

print()
print("Welcome to Card Tower Architect!")
print()
print("A program by rockafansky")
answer = MainMenu(True)
while answer == "a" or answer == "b" or answer == "c":
    if answer == "a":
        print()
        decknum = int(input("How many full decks of cards do you have? "))
        extracard = int(input("How many loose extra cards do you have? "))
        cardnum = (decknum * 52) + extracard
        print()
        if cardnum < 2:
            print("You do not have enough cards to make a tower. You fool.")
        stats = CalculationsMenu()
        while stats == "a" or stats == "b":
            if stats == "a":
                print("You have a total of " + str(decknum) + " decks of cards.")
                print("You have a total of " + str(cardnum) + " single playing cards.")
                stats = CalculationsMenu()
            if stats == "b":
                print()
                levels = int(input("How many levels would you like your card tower to have? "))
                offlevels = levels
                onetowercardnum = 0
                while levels > 0:
                    onetowercardnum += ((levels * 2) + (levels - 1))
                    levels -= 1
                if onetowercardnum > cardnum:
                    print()
                    print("You don't have enough cards to build that tower!")
                    print()
                elif onetowercardnum <= cardnum:
                    towers = cardnum // onetowercardnum
                    towerscardnum = towers * onetowercardnum
                    mod = cardnum - towerscardnum
                    print()
                    print("You can build " + str(towers) + " " + str(offlevels) + "-level card towers.")
                    print("Each tower will be made up of " + str(onetowercardnum) + " playing cards.")
                    print("You will have " + str(mod) + " cards left over.")
                    stats = CalculationsMenu()
        answer = MainMenu(False)
    elif answer == "b":
        print()
        decknum = int(input("How many full decks of cards will you use? "))
        extracard = int(input("How many loose extra cards will you use? "))
        cardnum = (decknum * 52) + extracard
        if cardnum < 2:
            print()
            print("You do not have enough cards to make a tower. You fool.")
        else:
            towercardnum = cardnum
            tower = 0
            levels = 1
            while towercardnum >= ((2 * levels) + (levels-1)):
                towercardnum -= ((2 * levels) + (levels-1))
                tower += ((2 * levels) + (levels-1))
                levels += 1
            cardlen = 88.9 #mm
            onelevelheight = (m.sqrt(3)/2)*cardlen
            height = (onelevelheight * levels)//10 #cm
            print()
            print("You card tower will be " + str(height) + " cm tall, " + str(levels-1) + " levels high.")
            print("It will be made up of " + str(tower) + " playing cards.")
            print("You will have " + str(towercardnum) + " cards left over.")
        answer = MainMenu(True)
    elif answer == "c":
        print()
        decknum = int(input("How many full decks of cards will you use? "))
        extracard = int(input("How many loose extra cards will you use? "))
        cardnum = (decknum * 52) + extracard
        if cardnum < 2:
            print()
            print("You do not have enough cards to make a tower. You fool.")
        else:
            towercardnum = cardnum
            tower = 0
            levels = 1
            while towercardnum >= ((2 * levels) + (levels-1)):
                towercardnum -= ((2 * levels) + (levels-1))
                tower += ((2 * levels) + (levels-1))
                levels += 1
            print()
            smolrow = 1
            var = levels -1
            for i in range(levels -1):
                print((" " * var) + ("/\\" * smolrow))
                smolrow = smolrow + 1
                var = var - 1
        answer = MainMenu(True)
print()
print("Thank you for using Card Tower Architect! Now please get a life.")
sys.exit()
