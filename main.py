from os import system, name
from math import trunc # for truncating when adding the starting area
from numpy import array
import scipy.ndimage as ndimage

# globals
SIZE = 11
grid = []

# create grid
for y in range(SIZE):
    grid.append([])
    for x in range(SIZE):
        grid[y].append("-")

# add starting area
middleX = trunc(SIZE / 2)
middleY = trunc(SIZE / 2)
# creates a 4 tall line
for i in range(-2, 2):
    grid[middleY + i][middleX] = "|"

currentPlayer = "X"
gameOver = False
reason = ""

# clears the screen
def clear():
    if name == 'nt':
        system('cls')
  
    else:
        system('clear')

# swaps the currentPlayer between X and O
def changePlayer():
    global currentPlayer

    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# prints the grid
def printGrid():
    # print the x axis at the top
    for i in range(SIZE + 1):
        print(str(i)[-1], end = " ")
    
    # create new line
    print()

    yGuide = 1
    for line in grid:
        print(str(yGuide)[-1], end = " ")
        for location in line:
            print(location, end = " ")
        yGuide += 1

        # create new line
        print()

printGrid()

# main game loop
while not gameOver:
    # get action type
    while True:
        print("Player " + currentPlayer)
        action = input("Choose your action:\n1. Place a symbol\n2. Create 4 new connecting tiles\n3. Block any two unfilled tiles\n")
        if action.isdigit():
            action = int(action)
            if action in [1, 2, 3]:
                break
            else:
                print("Please enter 1, 2 or 3")
        else:
            print("Please enter 1, 2 or 3")
    
    # if place a symbol is chosen
    # get x and y
    # both must be within the bounds and the selected square must be a | meaning it is empty
    if action == 1:
        while True:
            # check if there are any empty tiles
            possibleLocationCheck = False
            for line in grid:
                if "|" in line:
                    possibleLocationCheck = True

            if not possibleLocationCheck:
                break

            # get x
            while True:
                coordinate = input("Enter x coordinate: ")
                if coordinate.isdigit():
                    if 0 < int(coordinate) <= SIZE:
                        coordinate = int(coordinate) - 1
                        x = coordinate
                        break
                    else:
                        print("Please enter a number between 1 and " + str(SIZE))
                else:
                    print("Please enter a number")
            
            # get y
            while True:
                coordinate = input("Enter y coordinate: ")
                if coordinate.isdigit():
                    if 0 < int(coordinate) <= SIZE:
                        coordinate = int(coordinate) - 1
                        y = coordinate
                        break
                    else:
                        print("Please enter a number between 1 and " + str(SIZE))
                else:
                    print("Please enter a number")
            
            if grid[y][x] != "|":
                print("The selected tile isn't an empty square (|)")
            else:
                grid[y][x] = currentPlayer
                break
        
        # 3 in a row check
        # horizontal check
        for y in range(SIZE):
            for x in range(SIZE - 2):
                if (grid[y][x] == currentPlayer) and (grid[y][x+1] == currentPlayer) and (grid[y][x+2] == currentPlayer):
                    gameOver = True
        # vertical check
        for y in range(SIZE - 2):
            for x in range(SIZE):
                if (grid[y][x] == currentPlayer) and (grid[y+1][x] == currentPlayer) and (grid[y+2][x] == currentPlayer):
                    gameOver = True
        # top left to bottom right check
        for y in range(SIZE - 2):
            for x in range(SIZE - 2):
                if (grid[y][x] == currentPlayer) and (grid[y+1][x+1] == currentPlayer) and (grid[y+2][x] == currentPlayer):
                    gameOver = True
        # bottom left to top right check
        for y in range(2, SIZE):
            for x in range(SIZE - 2):
                if (grid[y][x] == currentPlayer) and (grid[y-1][x+1] == currentPlayer) and (grid[y-2][x] == currentPlayer):
                    gameOver = True
        if gameOver:
            reason = currentPlayer + " won!"
    # first tile must neighbour a | X O #
    # al the rest must neigherbour a T
    elif action == 2:
        isFirst = True
        # loop this four times as we want to add 4 squares
        for i in range(4):
            # check if the grid is full
            possibleLocationCheck = False
            for line in grid:
                if "-" in line:
                    possibleLocationCheck = True

            if not possibleLocationCheck:
                break

            while True:
                # get x
                while True:
                    coordinate = input("Enter x coordinate: ")
                    if coordinate.isdigit():
                        if 0 < int(coordinate) <= SIZE:
                            coordinate = int(coordinate) - 1
                            x = coordinate
                            break
                        else:
                            print("Please enter a number between 1 and " + str(SIZE))
                    else:
                        print("Please enter a number")
                
                # get y
                while True:
                    coordinate = input("Enter y coordinate: ")
                    if coordinate.isdigit():
                        if 0 < int(coordinate) <= SIZE:
                            coordinate = int(coordinate) - 1
                            y = coordinate
                            break
                        else:
                            print("Please enter a number between 1 and " + str(SIZE))
                    else:
                        print("Please enter a number")
                
                # check neighbours
                # isFirst does same check but looks for | X O rather than T
                if isFirst:
                    validTiles = ["|", "X", "O", "#"]
                else:
                    validTiles.append("T")

                valid = False
                if grid[y][x] == "-":
                    if (grid[y+1][x] in validTiles) and (y+1 <= SIZE):
                        valid = True
                    elif (grid[y-1][x] in validTiles) and (y-1 >= 0):
                        valid = True
                    elif (grid[y][x+1] in validTiles) and (x+1 <= SIZE):
                        valid = True
                    elif (grid[y][x-1] in validTiles) and (x-1 >= 0):
                        valid = True
                    elif (grid[y+1][x+1] in validTiles) and (y+1 <= SIZE) and (x+1 <= SIZE):
                        valid = True
                    elif (grid[y-1][x+1] in validTiles) and (y-1 >= 0) and(x+1 <= SIZE):
                        valid = True
                    elif (grid[y+1][x-1] in validTiles) and (y+1 <= SIZE) and(x-1 >= 0):
                        valid = True
                    elif (grid[y-1][x-1] in validTiles) and (y-1 >= 0) and (x-1 >= 0):
                        valid = True
                    
                    if valid:
                        grid[y][x] = "T"
                        if isFirst:
                            isFirst = False
                        break
                    else:
                        if isFirst:
                            print("The selected tile doesn't neighbour an existing tile (| O X #)")
                        else:
                            print("The selected tile doesn't neighbour a newly created tile (T)")
                else:
                    print("The selected tile already exists")
            # after placing the T, reprint the grid so the user can see where to go next
            print()
            printGrid()
        
        # once all 4 are selected, change all Ts to |
        for y in range(SIZE):
            for x in range(SIZE):
                if grid[y][x] == "T":
                    grid[y][x] = "|"
        
        # fill in gaps
        temp = grid
        for y in range(SIZE):
            for x in range(SIZE):
                if temp[y][x] == "-":
                    temp[y][x] = 0
                else:
                    temp[y][x] = 1
        data = array(temp)
        out = ndimage.binary_fill_holes(data)
        for y in range(SIZE):
            for x in range(SIZE):
                if out[y][x] == True:
                    grid[y][x] = "|"
                elif out[y][x] == False:
                    grid[y][x] = "-"

    # replace - with #
    elif action == 3:
        # repeat twice
        for i in range(2):
            # check if there are any empty tiles
            possibleLocationCheck = False
            for line in grid:
                if "|" in line:
                    possibleLocationCheck = True

            if not possibleLocationCheck:
                break

            while True:
                # get x
                while True:
                    coordinate = input("Enter x coordinate: ")
                    if coordinate.isdigit():
                        if 0 < int(coordinate) <= SIZE:
                            coordinate = int(coordinate) - 1
                            x = coordinate
                            break
                        else:
                            print("Please enter a number between 1 and " + str(SIZE))
                    else:
                        print("Please enter a number")
                
                # get y
                while True:
                    coordinate = input("Enter y coordinate: ")
                    if coordinate.isdigit():
                        if 0 < int(coordinate) <= SIZE:
                            coordinate = int(coordinate) - 1
                            y = coordinate
                            break
                        else:
                            print("Please enter a number between 1 and " + str(SIZE))
                    else:
                        print("Please enter a number")
                
                if grid[y][x] != "|":
                    print("The selected tile isn't an empty square (|)")
                else:
                    grid[y][x] = "#"
                    break
            # after placing the #, reprint the grid so the user can see where to go next
            print()
            printGrid()

    # check if grid is full
    actionPossible = False
    for line in grid:
        if ("|" in line) or ("-" in line):
            actionPossible = True
    if not actionPossible:
        gameOver = True
        reason = "No possible moves, DRAW!"
        break

    # reprint the grid
    clear()
    printGrid()

    changePlayer()

print()
print(reason)