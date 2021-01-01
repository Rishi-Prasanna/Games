# TicTacToe (With Time)
# Made By Rishi Prasanna
import sys, os, time, random

class Square:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

grid = [] # Tic Tac Toe Board.

def mainMenu():
    message = "Tic Tac Toe"
    for char in message:
        print(char, end = '')
        time.sleep(0.05)
    print("")
    while True:
        print("n - New Game")
        print("e - Exit")
        choice = input("Select an option: ")
        if choice == "e":
            return
        elif choice == "n":
            newGame()
        else:
            print("Error: Not an option!\n")

def newGame():
    defGrid()
    GIP()

def defGrid():
    global grid
    grid = []
    for x in range(1,4):
        for y in range(1,4):
            S = Square(x,y," ")
            grid.append(S)

def printGrid():
    global grid
    cell = 1
    print("")
    for S in grid:
        if cell % 3 == 1:
            print(" ", end='')
        print(S.val, end = '')
        if cell % 3 == 0:
            if cell != 9:
                print("\n-----------")
        else:
            print(" | ", end = '')
        cell = cell + 1
    print("\n")

def GIP(): # Game in Progress.
    while True:
        printGrid()

        if existsBingo() == "you":
            youWin()
            break
        elif existsBingo() == "enemy":
            youLose()
            break

        myY = 0
        myX = 0
        while True:
            myX = int(float(input("Select a row: ")))
            myY = int(float(input("Select a column: ")))
            if myX < 1 or myX > 3 or myY < 1 or myY > 3:
                print("Error: Row or column number is below 1 or greater than 3!")
                continue
            break
        S = findSquare(myX, myY)
        S.val = "X"


        engineEnemy("easy")
    return

def findSquare(x, y):
    for S in grid:
        if S.x == x and S.y == y:
            return S

def engineEnemy(mode):
    while True:
        rand = random.randint(0, 8)
        S = grid[rand]
        if S.val == " ":
            S.val = "O"
            break
    return

def existsBingo(): # Returns "you", "enemy" or "none".
    row = existsRow()
    if row != "none":
        return row
    col = existsCol()
    if col != "none":
        return col
    return existsDiag()

def existsRow():
    cell = 0
    while True:

        rowYou = 0
        rowEnemy = 0
        if cell > 8:
            break
        row = []
        row.append(grid[cell])
        row.append(grid[cell+1])
        row.append(grid[cell+2])

        for R in row:
            if R.val == " ":
                break
            elif R.val == "O":
                rowEnemy = rowEnemy + 1
            elif R.val == "X":
                rowYou = rowYou + 1

        if rowYou == 3:
            return "you"
        elif rowEnemy == 3:
            return "enemy"

        cell = cell + 3


    return "none"

def existsCol():
    cell = 0
    while True:

        colYou = 0
        colEnemy = 0
        if cell > 2:
            break
        col = []
        col.append(grid[cell])
        col.append(grid[cell+3])
        col.append(grid[cell+6])

        for C in col:
            if C.val == " ":
                break
            elif C.val == "O":
                colEnemy = colEnemy + 1
            elif C.val == "X":
                colYou = colYou + 1

        if colYou == 3:
            return "you"
        elif colEnemy == 3:
            return "enemy"

        cell = cell + 1


    return "none"

def existsDiag():
    cell = 0
    diag1 = []
    diag2 = []
    for S in grid:
        if S.x == S.y:
            diag1.append(S)
        if S.x == 2 and S.y == 2:
            diag2.append(S)
        if S.x == S.y - 2:
            diag2.append(S)
        if S.y == S.x - 2:
            diag2.append(S)

    diagYou = 0
    diagEnemy = 0
    for A in diag1:
        if A.val == " ":
            break
        if A.val == "X":
            diagYou = diagYou + 1
        elif A.val == "O":
            diagEnemy = diagEnemy + 1

    if diagYou == 3:
        return "you"
    if diagEnemy == 3:
        return "enemy"
    diagYou = 0
    diagEnemy = 0

    for B in diag2:
        if B.val == " ":
            break
        if B.val == "X":
            diagYou = diagYou + 1
        elif B.val == "O":
            diagEnemy = diagEnemy + 1

    if diagYou == 3:
        return "you"
    if diagEnemy == 3:
        return "enemy"
    return "none"

def youWin():
    print("")
    message = "You Win!"
    for char in message:
        print(char, end = '')
        time.sleep(0.25)
    print("\n\n")
    return

def youLose():
    print("")
    message = "You Lose"
    for char in message:
        print(char, end = '')
        time.sleep(0.25)
    print("\n\n")
    return


try:
    mainMenu()
except KeyboardInterrupt:
    print("\n\n\nForce quit.")
finally:
    print("Exiting...")
