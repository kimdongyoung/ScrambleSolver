from Trie import buildTrie, Trie
from Tile import Tile

validWords = []

# Initializes the grid of tiles and recurses on each tile, finding valid word.
def findCombinations():
	grid = initGrid(gridLetters)
	for x in range(0, 4):
		for y in range(0, 4):
			findCombinationsHelper(grid, x, y, "")

def findCombinationsHelper(grid, x, y, word):
	# Check valid coordinates.
	if not (x >= 0 and x <= 3 and y >= 0 and y <= 3):
		return
	grid[x][y].visited = True
	newWord = word + grid[x][y].letter
	if isValidWord(newWord):
		validWords.append(newWord)
	findCombinationHelper(grid, x + 1, y + 1, newWord)

	# recurse on valid neighbors
	# mark as unvisited
	return 0

# Creates a 4x4 array of Tile objects.
def initGrid(letterGrid):
	tileGrid = [[None]*4, [None]*4, [None]*4, [None]*4]
	for x in range(0, 4):
		for y in range(0,4):
			tileGrid[x][y] = Tile(x,y, letterGrid[x][y])
	return tileGrid

# For debugging purposes.
def printGrid(tileGrid):
	for x in range(0, 4):
		row = ""
		for y in range(0, 4):
			row += tileGrid[x][y].letter + " "
		print row

if __name__ == '__main__':
	buildTrie('../dictionary/testDictionary.txt')
	letterGrid = [	["A","B","C","D"],
					["E","F","G","H"],
					["I","J","K","L"],
					["M","N","O","P"]]
	tileGrid = initGrid(letterGrid)
	printGrid(tileGrid)
	# findCombinations(tileGrid)