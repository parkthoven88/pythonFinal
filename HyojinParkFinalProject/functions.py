#functions.py

'''
This file will hold basic functions.
'''

# Function to print out 5 numbers each lines in same space
def listPrint(l):
    n = 0
    while n < len(l):
        print('%5d' %l[n],'%5d' %l[n+1],'%5d' %l[n+2],'%5d' %l[n+3],'%5d' %l[n+4])
        n += 5

        
# Function to change the called number to ZERO        
def changeList(l, x):
    for i in range(len(l)):
        if l[i] == x:
            l[i] = 0
    return listPrint(l)

# Function to check if there is horizontal bingo
def findHorizontal(l):
    line = 0
    i = 0
    while i < len(l):
        if l[i:i+5].count(0) == 5:
            line +=1
        i += 5
    if line >= 1:
        print("*-*-*-*-* ", line, " horizontal bingo *-*-*-*-*")
    return line

# Function to check if there is vertical bingo
def verticalLoop(l, number):
    count = 0
    line = False
    for i in range(number, len(l), 5):
        if l[i] ==0:
            count +=1
    if count==5:
        line = True
    return line

# Print out if there is vertical bingo    
def findVertical(l):
    i= 0
    line = 0
    while i < 5:
        if verticalLoop(l,i):
            line += 1
        i += 1
    if line >= 1:
        print("*-*-*-*-* ", line, "  vertical bingo  *-*-*-*-*")
    return line
        

# Function to check if there is right diagonal bingo    
def rightDiagonal(l):
    count = 0
    line = 0
    for i in range(0, len(l), 6):
        if l[i] == 0:
            count += 1

    if count == 5:
        print("*-*-*-*-*  \\  diagonal bingo *-*-*-*-*")
        line = 1
    return line

# Function to check if there is left diagonal bingo 
def leftDiagonal(l):
    line = 0
    count = 0
    for i in range(4, 21, 4):
        if l[i] == 0:
            count += 1

    if count == 5:
        print("*-*-*-*-*  /  diagonal bingo *-*-*-*-*")
        line = 1

    return line

# Function is True if lines equal and greater then 5
def isTotalLine(n):
    if n >= 5:
        return True

# Founction count bingo line
def finalTotalLine(l,n):
    n += findHorizontal(l) + findVertical(l) + rightDiagonal(l) + leftDiagonal(l)
    print("\n\nYour BINGO is ", n)
    return n

# Function print bingo lines
def printTotalLine(l, n):
    n += findHorizontal(l) + findVertical(l) + rightDiagonal(l) + leftDiagonal(l)
    print("\n\nYour BINGO is ", n)
