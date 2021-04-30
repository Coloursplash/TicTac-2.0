from os import system, name
import math # for truncating when adding the starting area

# globals
SIZE = 11
grid = []

# create grid
for i in range(SIZE):
    grid.append([])
    for j in range(SIZE):
        grid[i].append("-")

# add starting area
middleX = math.trunc(SIZE / 2)
middleY = math.trunc(SIZE / 2)
# creates a 4 tall line
for i in range(-2, 2):
    grid[middleY + i][middleX] = "|"

currentPlayer = "X"
gameNotOver = True

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
        print(i[-1], end = " ")
    
    # create new line
    print()

    yGuide = 1
    for line in grid:
        print(yGuide[-1], end = " ")
        for location in line:
            print(location, end = " ")
        yGuide += 1

        # create new line
        print()

# print starting info
print("RULES WILL GO HERE")
printGrid()

# main game loop
while gameNotOver:    
    # get action type
    while True:
        action = input("Choose your action:\n1. Place a symbol\n2. Create 4 new connecting squares\n3. Delete any two unfilled squares\n")
        if action.isdigit():
            if action not in [1, 2, 3]:
                print("Please enter 1, 2 or 3")
                break
        else:
            print("Please enter 1, 2 or 3")
    
    # if place a symbol is chosen
    # get x and y
    # both must be within the bounds and the selected square must be a | meaning it is empty
    if action == "1":
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
                print("The selected tile isn't an empty square")
            else:
                grid[y][x] = currentPlayer
                break
    
    # reprint the grid
    clear()
    printGrid()

    changePlayer()