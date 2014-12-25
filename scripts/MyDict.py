# Returns the word if word is in dictionary. Otherwise returns empty string ""
def isValidWord(self, word):
	node = self.root
	for char in word:
		charNum = ord(char.lower()) - 97
		if node.children[charNum] == None:
			return self.root
		else:
			node = node.children[charNum]
	return node


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
	#myDict = buildDict('../dictionary/dictionary.txt')
	word = "aardvark"
	for x in range(0, 100000000):
		len(word)
	#for x in range(0, 10000000):
	#	isValidWord(myDict,"aardvar")

	#	myTrie.isValidWord("aardvar")
	#n = myTrie.isValidWord("aardvar")
	#print n.key
	#print myTrie.size()