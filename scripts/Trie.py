# Trie 
class Trie(object):
	def __init__(self):
		self.root = Node()

	def insert(self, word):
		if word.isalpha() == False:
			print "Invalid word. Not inserting into trie."
			return
		
		node = self.root
		i = 0
		n = len(word)

		while i < n:
			charNum = ord(word[i].lower()) - 97
			if node.children[charNum] != None:
				node = node.children[charNum]
				i += 1
			else:
				break
		while i < n:
			node.isLeaf = False
			charNum = ord(word[i].lower()) - 97
			node.children[charNum] = Node()
			node = node.children[charNum]
			node.isLeaf = True
			i += 1

		node.key = word

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

	# For debugging purposes. Count number of nodes using DFS
	def size(self):
		return self.sizeHelper(self.root)
	
	def sizeHelper(self, node):
		count = 0
		if node == None:
			return count
		else:
			for child in node.children:
				count += self.sizeHelper(child)
			return 1 + count		


# Node needs key and an array of nodes.
class Node(object):
	def __init__(self):
		self.key = ""
		self.children = [None] * 26
		self.isLeaf = False

# Input: path to dictionary file
# Output: a trie
def buildTrie(path):
	trie = Trie()
	with open(path) as dictionary:
		for word in dictionary:
			trie.insert(word.strip())
	return trie

if __name__ == '__main__':
	myTrie = buildTrie('../dictionary/dictionary.txt')
	for x in range(0, 1000000):
		myTrie.isValidWord("aardvar")
	#n = myTrie.isValidWord("aardvar")
	#print n.key
	#print myTrie.size()

