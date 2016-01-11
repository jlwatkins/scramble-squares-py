#!/usr/bin/python3.4
class Tile:
    def __init__(self, identifier, side1, side2, side3, side4):
        self.sides = []
        self.identifier = identifier
        self.sides.append(side1)
        self.sides.append(side2)
        self.sides.append(side3)
        self.sides.append(side4)
        
    def __str__(self):
         return str("Tile: " + str(self.identifier))
        
    def getEdge(self, edge): # 0 = top, 1 = right, 2 = bottom, 3 = left
    		if edge == 0:
    			return self.sides[0]
    		elif edge == 1:
    			return self.sides[1]
    		elif edge == 2:
    			return self.sides[2]
    		elif edge == 3:
    			return self.sides[3]
    		else:
    			return null
    			
    def getEdges(self):
      return self.sides[0], self.sides[1], self.sides[2], self.sides[3]

class Placement: # rotation: 0 = not rotated, 1 = rotated 90° clockwise, 2 = 180°, 3 = 270°

    def __init__(self, baseTile, rotation):
        if rotation == 0:
            self.virtualTile = Tile(baseTile.identifier, baseTile.sides[0], baseTile.sides[1], baseTile.sides[2], baseTile.sides[3])
        elif rotation == 1:
            self.virtualTile = Tile(baseTile.identifier, baseTile.sides[3], baseTile.sides[0], baseTile.sides[1], baseTile.sides[2])
        elif rotation == 2:
            self.virtualTile = Tile(baseTile.identifier, baseTile.sides[2], baseTile.sides[3], baseTile.sides[0], baseTile.sides[1])
        elif rotation == 3:
            self.virtualTile = Tile(baseTile.identifier, baseTile.sides[1], baseTile.sides[2], baseTile.sides[3], baseTile.sides[0])
    def getEdge(self, edge):
        return self.virtualTile.getEdge(edge)
    def __str__(self):
        return str(self.virtualTile)

class Grid:
    def __init__(self):
        self.positionArray = [None] * 9
        self.maxPosition = 0
        self.totalPositions = 0
        self.almostSolutions = 0
        self.solutions = 0
        self.solGrids = []
    
    def place(self, placement, location):
        if (location % 3 != 0): # If the tile is in the middle column or right, check that its left edge matches
            if placement.getEdge(3) + self.positionArray[location - 1].getEdge(1) != 9:
                return False
        if (location > 2): # If the tile isn't in the first row, check that its top edge matches
            if placement.getEdge(0) + self.positionArray[location - 3].getEdge(2) != 9:
                return False
                
        self.positionArray[location] = placement
        return True
        
    def remove(self, location):
        self.positionArray[location] = None
    
    def __str__(self):
        s = ""
        for i in range(0, 9):
            s += "Tile " + str(i) + ":" + str(self.positionArray[i]) + "\n"
        return s
        
    def getTiles(self):
        tilelist = []
        for i in range(0, 9):
            tilelist.append(int(self.positionArray[i].virtualTile.identifier))
        return tilelist
        
        
    def addToGrid(self, positionIndex, remainingTiles):
        if positionIndex > self.maxPosition:
            # print("Found grid of " + str(positionIndex) + " tiles:\n")
            # print(str(grid) + "---")
            self.maxPosition = positionIndex
        
        if positionIndex == 8:
            self.almostSolutions += 1
            
        for i in remainingTiles:
            for j in range(4):
                if grid.place(Placement(i, j), positionIndex):
                    if (positionIndex == 8): ## if we placed it correctly and we're on the final spot, we're done
                        # print(str(grid))
                        self.solutions += 1
                        self.solGrids.append(self.getTiles())
                        # return True
                    newTiles = []
                    for k in remainingTiles:
                        if k != i:
                            newTiles.append(k)
                    validPosition = self.addToGrid(positionIndex+1, newTiles)
                    if validPosition:
                        pass
                        # return True
        self.totalPositions += 1
        return False # we were not able to add the tile


def printNames(namesDict):
    print("")
    print("1 : " + names[1])
    print("2 : " + names[2])
    print("3 : " + names[3])
    print("4 : " + names[4])
    print("5 : " + names[5])
    print("6 : " + names[6])
    print("7 : " + names[7])
    print("8 : " + names[8])
    print("")
    
def printBlankLine():
  print("\t\t\t|\t\t\t|\t\t\t")

def printHorizontalSeparator():
  print("------------------------------------------------------------------------")
  
def printSimpleBoard(numbers):
  print("")
  printBlankLine()
  print("\tTile "+ str(numbers[0]) + "\t\t|\tTile "+ str(numbers[1]) + "\t\t|\tTile "+ str(numbers[2]) + "\t\t")
  printBlankLine()
  printHorizontalSeparator()
  printBlankLine()
  print("\tTile "+ str(numbers[3]) + "\t\t|\tTile "+ str(numbers[4]) + "\t\t|\tTile "+ str(numbers[5]) + "\t\t")
  printBlankLine()
  printHorizontalSeparator()
  printBlankLine()
  print("\tTile "+ str(numbers[6]) + "\t\t|\tTile "+ str(numbers[7]) + "\t\t|\tTile "+ str(numbers[8]) + "\t\t")
  printBlankLine()
  print("")
  
# Print Intro
print("")
print("Welcome to Scramble Squares Solver!")
print("")
print("You are going to enter names for all 4 images.")
print("Each image that you give a name will than have a top or bottom")
print("After that you will enter all the edges of your squares. Please assign numbers to your squares from 1 to 9 and enter them in order.")
print("")

# Initialize tiles and names to be blank
tiles = [None] * 9
names = {}
grid = Grid()

# Get 4 names of images from user
im_name_1 = input("What would you like to call the first image? ")
im_name_2 = input("What would you like to call the second image? ")
im_name_3 = input("What would you like to call the third image? ")
im_name_4 = input("What would you like to call the last image? ")

# Build the names so they can match and be compared (automatically append top and bottoms
names = { 1: im_name_1 + " top",
          2: im_name_2 + " top",
          3: im_name_3 + " top",
          4: im_name_4 + " top",
          5: im_name_4 + " bottom",
          6: im_name_3 + " bottom",
          7: im_name_2 + " bottom",
          8: im_name_1 + " bottom" }
          
# Print the names numbers for reference when entering tiles
printNames(names)
print("Enter each tile with four numbers with spaces inbetween. Order is TOP RIGHT BOTTOM LEFT")
for tilenumber in range(1,10):
  error = True
  while error is True:
    result = input("Enter Tile #" + str(tilenumber) + ": ").split()
    if len(result) != 4:
      error = True
      print("ERROR: Please enter 4 numbers with a space inbetween")
    else:
      error = False
      tiles[tilenumber - 1] = Tile(str(tilenumber), int(result[0]), int(result[1]), int(result[2]), int(result[3]))
      
# Hardcoded Tiles - Example if you wanted to hardcode the tiles
# tiles[0] = Tile("1", 3, 8, 2, 4)
# tiles[1] = Tile("2", 3, 8, 2, 4)
# tiles[2] = Tile("3", 3, 8, 6, 4)
# tiles[3] = Tile("4", 7, 5, 3, 1)
# tiles[4] = Tile("5", 7, 5, 2, 1)
# tiles[5] = Tile("6", 5, 3, 1, 2)
# tiles[6] = Tile("7", 4, 6, 1, 7)
# tiles[7] = Tile("8", 7, 1, 4, 3)
# tiles[8] = Tile("9", 2, 1, 4, 6)
  
foundSolution = grid.addToGrid(0, tiles)

# Solution Information
print("\n")
print("Was a solution found? " + str(grid.solutions > 0))
if grid.solutions > 0:
  print("How many solutions were found: " + str(grid.solutions))

print("Total Guesses: " + str(grid.totalPositions))
print("Number of almost solutions: " + str(grid.almostSolutions - grid.solutions))
print("")
input("Hit Enter To View Solutions")
solutionNumber = 0
for g in grid.solGrids:
  solutionNumber += 1
  print("")
  print("Solution #" + str(solutionNumber))
  printSimpleBoard(g)
  print("")
