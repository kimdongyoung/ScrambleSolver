# Trie 
class Trie(object):
	def __init__(self):
		self.root = _Node()

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
			charNum = ord(word[i].lower()) - 97
			node.children[charNum] = _Node()
			node = node.children[charNum]
			i += 1

		node.key = word

	# Returns the word if word is in dictionary. Otherwise returns empty string ""
	def isValidWord(self, word):
		if word.isalpha() == False:
			print "Invalid word. Not looking in trie."
			return

		node = self.root
		for char in word:
			charNum = ord(char.lower()) - 97
			if node.children[charNum] == None:
				return ""
			else:
				node = node.children[charNum]
		return node.key

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
class _Node(object):
	def __init__(self):
		self.key = ""
		self.children = [None] * 26

# Input: path to dictionary file
# Output: a trie
def buildTrie(path):
	trie = Trie()
	with open(path) as dictionary:
		for word in dictionary:
			trie.insert(word.strip())
	return trie

if __name__ == '__main__':
	myTrie = buildTrie('../dictionary/testDictionary.txt')
	print myTrie.isValidWord("")
	print myTrie.size()

