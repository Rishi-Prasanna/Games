# TicTacToe (With Time)
# Made By Rishi Prasanna
# time and random are very important.
import sys, os, time, random

# The square class has an init method to declare an object of type Square.
# x contains the x coordinate on the TTT grid, y contains the y coordinate on the TTT grid,
# and val contains "X", "O", or " ".
class Square:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

grid = [] # Initializing the Tic Tac Toe Board.

def mainMenu():
    # A cool little typing effect for the title card, because why not?
    message = "Tic Tac Toe"
    for char in message:
        print(char, end = '')
        time.sleep(0.05)
    print("") # A new line so that "n - New Game" does not print right next to the last "e".
    
    # Needed a loop to print new game.
    while True:
        print("n - New Game")
        print("e - Exit")
        choice = input("Select an option: ")
        # Exit if "e".
        if choice == "e":
            return
        # New game if "n".
        elif choice == "n":
            newGame()
        # Otherwise, invalid option.
        else:
            print("Error: Not an option!\n")

def newGame():
    defGrid() # Defines 9 objects of type Square and places them in grid.
    GIP() # Game In Progress.

def defGrid():
    global grid
    grid = [] # Reset grid. I could also have done grid.clear().
    for x in range(1,4): # from 1 to 3 for x
        for y in range(1,4): # from 1 to 3 for y
            S = Square(x,y," ") # Create empty square in that spot.
            grid.append(S) # Append the square object to grid.

def printGrid():
    global grid
    cell = 1 # An accumulator to print the grid.
    print("")
    
    # Enter for loop over each square in grid.
    for S in grid:
        if cell % 3 == 1: # If cell = start of row (aka 1, 4 or 7), print " ".
            print(" ", end='')
        print(S.val, end = '') # Print the value of each square object.
        if cell % 3 == 0: # If cell = end of row (aka 3, 6, 9)...
            if cell != 9: # If cell = 3 or 6, print a divider below that row and go to next row.
                print("\n-----------")
        else: # If cell = 1, 2, 4, 5, 7 or 8, print a divider between each "cell".
            print(" | ", end = '')
        cell = cell + 1 # Increment cell.
    print("\n") # Print two new lines.

def GIP(): # Game in Progress.
    while True:
        printGrid() # Call the printGrid function to print the grid every time it's your turn.

        if existsBingo() == "you": # If there is a "bingo" of X's for you, you win!
            youWin()
            break
        elif existsBingo() == "enemy": # If there is a "bingo" of O's for the enemy, you lose!
            youLose()
            break

        myX = 0
        myY = 0
    
        # When I initialize variables from user input, input("Something") gives me a string.
        # So I need to convert this string to float, and then int, to get us row and column numbers.
        while True:
            myX = int(float(input("Select a row: "))) # Row number.
            myY = int(float(input("Select a column: "))) # Column number.
            if myX < 1 or myX > 3 or myY < 1 or myY > 3: # Both vars must be 1 to 3, or else error message.
                print("Error: Row or column number is below 1 or greater than 3!")
                continue
            break # Otherwise, break from loop.
            
        S = findSquare(myX, myY) # Calls the findSquare function to find the Square in Grid that has those x and y coordinates.
        S.val = "X" # Sets that square's value to "X".


        engineEnemy("easy") # The opponent, an engine, plays back the reply.
    return

def findSquare(x, y):
    # Finds the Square object with specific x and y.
    for S in grid:
        if S.x == x and S.y == y:
            return S

def engineEnemy(mode):
    # Currently only easy mode, aka random cell.
    while True:
        rand = random.randint(0, 8) # Generates integer from index 1 to index 9.
        S = grid[rand] # Get Square at rand's index in the grid.
        if S.val == " ": # Only if the value of that Square is empty, the engine is allowed to put an "O" in that Square.
            S.val = "O" # Set that Square's value to "O".
            break
    return

def existsBingo(): # Returns "you", "enemy" or "none".
    row = existsRow() # Checks if there is a bingo on the row.
    if row != "none":
        return row
    col = existsCol() # Checks if there is a bingo on the column.
    if col != "none":
        return col
    return existsDiag() # Checks if there is a bingo in the diagonal.

def existsRow():
    cell = 0 # Index value for the grid.
    while True:

        rowYou = 0 # Accumulator for you.
        rowEnemy = 0 # Accumulator for engine.
        
        # If all cells are checked, no bingo on row. 
        if cell > 8:
            break
            
        # Define row array to be the first, second and third cells in row.
        row = []
        row.append(grid[cell])
        row.append(grid[cell+1])
        row.append(grid[cell+2])

        # For each cell in the current row...
        for R in row:
            # If the cell's value is a space, neither player gets the row! Break.
            if R.val == " ":
                break
            # If the cell's value is "O", increment enemy counter.
            elif R.val == "O":
                rowEnemy = rowEnemy + 1
            # Else, increment your counter.
            elif R.val == "X":
                rowYou = rowYou + 1

        # If all three cells are X's or all are O's, return "you" or "enemy" respectively.
        if rowYou == 3:
            return "you"
        elif rowEnemy == 3:
            return "enemy"

        # Increment cell index by 3 to go to the next row.
        cell = cell + 3

    # After the whole fiasco, return none.
    return "none"

def existsCol():
    cell = 0 # Index value for the grid.
    while True:

        colYou = 0 # Accumulator for you.
        colEnemy = 0 # Accumulator for enemy.
        
        # If you've gone past the last column, no bingo on column. Return "none".
        if cell > 2:
            break
            
        # Define the column array to be the cellth cell in the first row, cellth cell in second row, and cellth cell for third row.
        col = []
        col.append(grid[cell])
        col.append(grid[cell+3])
        col.append(grid[cell+6])

        # For every cell in the column array...
        for C in col:
            if C.val == " ": # Again, if the cell is empty, neither player gets the bingo for that column!
                break
            elif C.val == "O": # If "O", then enemy counter incremented by 1.
                colEnemy = colEnemy + 1
            elif C.val == "X": # If "X", then your counter incremented by 1.
                colYou = colYou + 1

        # Whosever counter is 3 is whoever is returned.
        if colYou == 3:
            return "you"
        elif colEnemy == 3:
            return "enemy"

        # Increment cell by 1 to go to the next column.
        cell = cell + 1


    # After the whole fiasco, return "none".
    return "none"

def existsDiag():
    cell = 0
    diag1 = [] # The northwest to southeast diagonal.
    diag2 = [] # The southwest to northeast diagonal.
    for S in grid:
        if S.x == S.y: # If you have something like (1,1),(2,2),(3,3), that's diagonal 1.
            diag1.append(S)
        if S.x == 2 and S.y == 2: # If you have (2,2), that's also diagonal 2.
            diag2.append(S)
        if S.x == S.y - 2: # (1,3) case -> diagonal 2.
            diag2.append(S)
        if S.y == S.x - 2: # (3,1) case -> diagonal 2.
            diag2.append(S)

    diagYou = 0 # Accumulator for you.
    diagEnemy = 0 # Accumulator for enemy.
    
    # For every cell in the diag1 array...
    for A in diag1:
        if A.val == " ": # If the A's val is " ", neither player gets the bingo!
            break
        if A.val == "X": # If the A's val is "X", increment your counter.
            diagYou = diagYou + 1
        elif A.val == "O": # If the A's val is "O", increment enemy's counter.
            diagEnemy = diagEnemy + 1

    # Whosever's counter is 3 is returned.
    if diagYou == 3:
        return "you"
    if diagEnemy == 3:
        return "enemy"
    
    # Reset the counters to check diag2.
    diagYou = 0
    diagEnemy = 0

    # For every cell in diag2 array...
    for B in diag2:
        if B.val == " ": # If " ", break.
            break
        if B.val == "X": # If "X", increment your counter.
            diagYou = diagYou + 1
        elif B.val == "O": # If "O", increment enemy's counter.
            diagEnemy = diagEnemy + 1

    # Whosever's counter is 3 is returned.
    if diagYou == 3:
        return "you"
    if diagEnemy == 3:
        return "enemy"
    
    # After the whole fiasco, return "none".
    return "none"

def youWin(): # You win! Typing text effect.
    print("")
    message = "You Win!"
    for char in message:
        print(char, end = '')
        time.sleep(0.25)
    print("\n\n")
    return

def youLose(): # You lose! Typing text effect.
    print("")
    message = "You Lose"
    for char in message:
        print(char, end = '')
        time.sleep(0.25)
    print("\n\n")
    return


# This calls the mainMenu() to start the game, and has an error condition for KeyboardInterrupt.
try:
    mainMenu()
except KeyboardInterrupt:
    print("\n\n\nForce quit.")
finally:
    print("Exiting...")
