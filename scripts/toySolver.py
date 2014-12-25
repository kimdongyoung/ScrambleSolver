from Trie import buildTrie, Trie
from Tile import Tile

validWords = []
neighbors = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

# Initializes the grid of tiles and recurses on each tile, finding valid word.
def findCombinations(tileGrid):
	numRow = len(tileGrid)
	numCol = len(tileGrid[0])
	for x in range(0, numRow):
		for y in range(0, numCol):
			findCombinationsHelper(tileGrid, x, y, "")

def findCombinationsHelper(tileGrid, x, y, word):
	numRow = len(tileGrid)
	numCol = len(tileGrid[0])
	if (not insideGrid(x, y, numRow, numCol)) or (tileGrid[x][y].visited == True):
		return

	tileGrid[x][y].visited = True # mark as visited
	newWord = word + tileGrid[x][y].letter
	'''
	if isValidWord(newWord):
		validWords.append(newWord)
	'''
	if len(newWord) > 1:
		validWords.append(newWord)
	
	for k in range(0,8):
		findCombinationsHelper(tileGrid, x + neighbors[k][0], y + neighbors[k][1], newWord)

	tileGrid[x][y].visited = False # mark as unvisited

# Check valid coordinates.
def insideGrid(x, y, xBound, yBound):
	if x >= 0 and x < xBound and y >= 0 and y < yBound:
		return True
	else:
		return False

# Creates a 2D-array of Tile objects.
def initGrid(letterGrid):
	numRow = len(letterGrid)
	numCol = len(letterGrid[0])
	tileGrid = []
	for row in range(0, numRow):
		tileGrid.append([None] * numCol)
	
	for x in range(0, numRow):
		for y in range(0, numCol):
			t = Tile(x, y, letterGrid[x][y])
			tileGrid[x][y] = t
	return tileGrid

# For debugging purposes.
def printGrid(tileGrid):
	numRow = len(tileGrid)
	numCol = len(tileGrid[0])
	for x in range(0, numRow):
		row = ""
		for y in range(0, numCol):
			row += tileGrid[x][y].letter + " "
		print row

if __name__ == '__main__':
	buildTrie('../dictionary/testDictionary.txt')
	letterGrid2D = [["A","B"],
					["C","D"]]
	letterGrid3D = [["A","B","C"],
					["D","E","F"],
					["G","H","I"]]
	tileGrid = initGrid(letterGrid2D)
	printGrid(tileGrid)
	findCombinations(tileGrid)
	validWords.sort(key=len, reverse=True)
	print validWords
	print len(validWords)

