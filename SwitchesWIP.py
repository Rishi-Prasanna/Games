# Switches
# Made By Rishi Prasanna
import sys, os, time, random

class Switch:
    def __init__(self, x, y, val, rev):
        self.x = x
        self.y = y
        self.val = val
        self.rev = rev

grid = [] # Same grid system as the Tic-Tac-Toe game.
coins = 0
scoins = 0
points = 0
numDSwitches = 0
revives = 0 # To be incorporated later.
# Shop will be incorporated later.

def mainMenu():
    message = "Switches"
    for char in message:
        print(char, end = '')
        time.sleep(0.05)
    print("")

    while True:
        print("Coins: " + str(coins) + " | Star coins: " + str(scoins))
        print("n - New Game")
        print("s - Shop")
        print("e - Exit")
        choice = input("Pick an option: ")
        if choice == "n":
            newGame()
        elif choice == "e":
            break
        else:
            print("\nError: Not a valid option!")
    return

def newGame():
    global points
    points = 0
    print("\nNew Game")
    print("Loading...")
    defGrid()
    rand = random.randint(10000, 20001)
    shuffleGrid(rand) # Some random number.
    printGridRevealed()
    input("Press Enter to continue")
    GIP()
    return

def defGrid(): # Define grid.
    y = 0
    for x in range(1, 8):
        for y in range(1, 9):
            if x == 7 and y == 7:
                break
            rand = random.randint(1, 100)
            S = Switch(x,y,str(rand),False)
            grid.append(S)
        if x == 7 and y == 7:
            break

    # Now define the C, B and D switches!
    D1 = Switch(7,7,"D",False)
    D2 = Switch(7,8,"D",False)
    D3 = Switch(8,1,"D",False)
    D4 = Switch(8,2,"D",False)
    grid.append(D1)
    grid.append(D2)
    grid.append(D3)
    grid.append(D4)

    for a in range(3, 7):
        C = Switch(8,a,"C",False)
        grid.append(C)

    S = Switch(8,7,"S", False)
    B = Switch(8,8,"B", False)
    grid.append(S)
    grid.append(B)
    return

def shuffleGrid(num): # Shuffles the panels using Fisher-Yates.
    for times in range(0, num):
        for x in range(0, len(grid)):
            rand = random.randint(0, 63)
            x1 = grid[x].x
            y1 = grid[x].y
            x2 = grid[rand].x
            y2 = grid[rand].y
            grid[x], grid[rand] = grid[rand], grid[x]
            grid[x].x = x1
            grid[x].y = y1
            grid[rand].x = x2
            grid[rand].y = y2
    return

def printGridRevealed(): # Prints the grid with all tiles revealed.
    x = 1
    print("")
    for S in grid:
        print(S.val, end = '')
        if x % 8 == 0:
            print("")
            x = x + 1
            continue
        print("\t", end = '')
        x = x + 1
    print("")
    return

def printGrid(): # Prints all the squares, and whether they are revealed or not.
    x = 1
    print("")
    for S in grid:
        if S.rev:
            print(S.val, end='')
        else:
            print("?", end='')
        if x % 8 == 0:
            print("")
            x = x + 1
            continue
        print("\t", end='')
        x = x + 1
    print("")
    return

def GIP(): # Game In Progress.
    global points
    global coins
    global scoins
    global numDSwitches
    while True:
        printGrid()
        x = 0
        y = 0
        while True:
            try:
                x = int(float(input("Enter a value for the row: ")))
            except ValueError:
                print("\nError: Not a number!")
                continue
            if x < 1 or x > 8:
                print("\nError: Must be between 1 and 8!")
                continue
            else:
                break
        while True:
            try:
                y = int(float(input("Enter a value for the column: ")))
            except ValueError:
                print("\nError: Not a number!")
                continue
            if y < 1 or y > 8:
                print("\nError: Must be between 1 and 8!")
                continue
            else:
                break
        S = findSwitch(x, y)
        S.rev = True
        process(S)

        if numDSwitches >= 2:
            print("Second D switch.")
            gameOver("lose")
            break
        elif allSwitchesActivated():
            print("Hooray! You flipped all of the correct switches!")
            gameOver("win")
            break
        input("Press Enter to continue")
    return

def allSwitchesActivated():
    for S in grid:
        if S.val == "D":
            continue
        if not S.rev:
            return False
    return True

def findSwitch(x, y): # Finding switch with row and column.
    for S in grid:
        if S.x == x and S.y == y:
            return S

def gameOver(outcome):
    message = ""
    if outcome == "lose":
        message = "Game Over"
    else:
        message = "You Win!"
    for char in message:
        print(char, end = '')
        time.sleep(0.25)
    time.sleep(1)
    print("\n")

def process(S): # The process for each switch.
    global points
    global coins
    global scoins
    global numDSwitches
    if S.val == "S":
        print("You found an S switch!\n+1 Star Coin!")
        scoins = scoins + 1
    elif S.val == "C":
        print("You found a C switch!\n+100 coins!")
        coins = coins + 100
    elif S.val == "B":
        print("You found a B switch!")
        print("Congratulations! You get a mystery box!")
    elif S.val == "D":
        print("Oh, no, you found a D switch!")
        numDSwitches = numDSwitches + 1
    else:
        print("You found a number switch!")
        print("+" + str(S.val) + " points!")
    return

try:
    mainMenu()
except KeyboardInterrupt:
    print("\n\n\nForce quit.")
finally:
    print("Exiting...")
