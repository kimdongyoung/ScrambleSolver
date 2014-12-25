from MyDict import buildDict, isValidWord
from Tile import Tile
import os, sys

myDict = {}
tileGrid = []
numRow = [0]
numCol = [0]
validWords = []
neighbors = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

# Initializes the grid of tiles and recurses on each tile, finding valid word.
def findCombinations():
	for x in range(0, numRow[0]):
		for y in range(0, numCol[0]):
			findCombinationsHelper(x, y, "")

def findCombinationsHelper(x, y, word):
	newWord = word + tileGrid[x][y].letter
	if isValidWord(myDict, newWord):
		validWords.append(newWord)

	tileGrid[x][y].visited = True # mark as visited

	for k in range(0,8):
		newX = x + neighbors[k][0]
		newY = y + neighbors[k][1]
		if (insideGrid(newX, newY)) and (tileGrid[newX][newY].visited == False):
			findCombinationsHelper(newX, newY, newWord)

	tileGrid[x][y].visited = False # mark as unvisited

# Check valid coordinates.
def insideGrid(x, y):
	if x >= 0 and x < numRow[0] and y >= 0 and y < numCol[0]:
		return True
	else:
		return False

# Creates a 2D-array of Tile objects.
def initGrid(letterGrid):
	numRow[0] = len(letterGrid)
	numCol[0] = len(letterGrid[0])
	for row in range(0, numRow[0]):
		tileGrid.append([None] * numCol[0])
	
	for x in range(0, numRow[0]):
		for y in range(0, numCol[0]):
			t = Tile(x, y, letterGrid[x][y])
			tileGrid[x][y] = t

def printGrid(tileGrid):
	print "====Grid===="
	for x in range(0, numRow[0]):
		row = ""
		for y in range(0, numCol[0]):
			row += tileGrid[x][y].letter + " "
		print row
	print ""

def printValidWords(validWords):
	validWords = list(set(validWords))
	validWords.sort(key=len, reverse=True)
	print "====Solution===="
	for word in validWords[:50]:
		print word
	print str(len(validWords)) + " matches found."

# A function that takes in a string of 16 letters and convert to 4x4 letter grid.
def createLetterGrid(letters):
	grid = []
	i = 0;
	for row in range(0,4):
		grid.append([''] * 4)

	for row in range(0,4):
		for col in range(0,4):
			grid[row][col] = letters[i]
			i += 1
	return grid

if __name__ == '__main__':
	if len(sys.argv) != 2 or len(sys.argv[1]) != 16:
		print "Provide a string of 16 letters (the grid) as argument."
	else:
		myDict = buildDict('../dictionary/dictionary.txt')
		letterGrid = createLetterGrid(sys.argv[1])
		letterGrid2D = [["T","O"],
						["N","R"]]
		letterGrid3D = [["T","E","S"],
						["R","E","T"],
						["S","H","E"]]
		letterGrid4D = [["I","N","R","M"],
						["T","E","G","A"],
						["L","O","N","E"],
						["P","S","D","S"]]
		initGrid(letterGrid)
		findCombinations()
		printGrid(tileGrid)
		printValidWords(validWords)
