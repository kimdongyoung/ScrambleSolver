def isValidWord(d, word):
	return d.has_key(word.lower())

# Input: path to dictionary file
# Output: a dictionary
def buildDict(path):
	d = {}
	with open(path) as dictionary:
		for word in dictionary:
			d[word.strip()] = 1
	return d

if __name__ == '__main__':
	myDict = buildDict('../dictionary/dictionary.txt')