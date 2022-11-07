# INF360 - Programming in Python
# Hyojin Park
# FinalProject

'''
    ***** Description *****
    
    Let's play Bingo game.

    The bingo board is made by the computer's random number.
    Users need to call numbers that are advantageous for bingo.
    Bingo must be at least three lines, horizontal, vertical, and diagonal.
    You have a total of 10 opportuniti5es.
'''

import logging
import sys
logging.basicConfig(filename='myProgramLog.txt', format=' %(asctime)s -  %(levelname)s -  %(message)s')

try:
    from functions import *
    
except:
    logging.critical('Missing functions.py!')
    print('Missing functions.py! is closing')
    sys.exit()

    
import random

#Class User : get a name and answer 
class User:

    # Initializer
    def __init__(self):
        self.getname()
        self.getanswer()

    def getname(self):
        #input must be one name, can user only letters
        while True: 
            name = input('Enter your name : ')
            if not name.isalpha():
                print('\nEnter the valid name again(Only letter)')
            else:
                self.name = name.capitalize() # first letter change uppercase
                print('Hi! ' + self.name + ', nice to meet you!')
                break
            
    def getanswer(self):
        # check the answer if user want to play
        print('\nHow about playing a BINGO together?')
        while True:
            answer = input('If you are OK, type Y, or N: ')
            if answer != 'Y' and answer != 'y' and answer != 'N' and answer != 'n':
                print('\nEnter the valid answer. Type Y or N')
            else:
                self.answer=answer.upper()
                break



# BINGO GAME
print("Welcome to the BINGO GAME")

#User class
user1 = User()



# While loop if answer is yes
while user1.answer == 'Y':
    
    #chances for user
    game = 10

    # random number between 1 and 25
    u = random.sample(range(1,26),25)


    # print out the table
    print("\n** There is a your table with randomly number **\n")
    listPrint(u) # Print out the table by random number

    # The 1-25 numbers in list. It will be removed when it calls
    callList = list(range(1,26))

    # play the bingo until game is 0
    while game> 0:
        
        # user turn for calling number
        uCall = input("\nPlease enter the number you want : ")

        # check the number user called if it's valid
        while True:
            if not uCall.isnumeric():
                uCall = input("\nPlease enter the number you want : ")
            elif int(uCall) not in callList:
                print("\nIt's NOT valid number. Try again.")
                uCall = input("Please enter the number you want : ")
            else:
                break


        uCall = int(uCall)
        callList.remove(uCall)   # remove the called number in callList

        changeList(u, uCall)     # change the Table called  number to ZERO

        totalLine = 0

        # calculate the bingo lines
        totalLine = finalTotalLine(u,totalLine)


        # check if bingo is 5 or more
        if isTotalLine(totalLine):
            print(" **** YOU ARE WINNER!!!! ****\n")
            break                  # end the game



        # computer turn for calling number
        c= random.sample(callList, 1)      # make a random number from computer
        cCall = c[0]                       # store as a number type
        print("\nIt's my turn. I call the number :", cCall, "\n")
        
        changeList(u, cCall)     # Change the Table called number to ZERO
        callList.remove(cCall)   # remove the called number in callList

        # print the bingo lines after calling from computer
        printTotalLine(u,0)
        
        game -=1
        print("Your chance is ", game, "times.")
        if game ==0:
            print("Sorry.........You LOSE................\n\n\n")
            break

    break

# End while loop
print("\n*****  Thank you  ***** \n** Have a great day! **")
