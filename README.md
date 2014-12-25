This program will produce solutions to Scramble With Friends. It will sort results by longest to shortest word (TL, DL, etc. can be implemented easily later).

Input will be a an array of 4 arrays, i.e.
[	
	['S','E','F','W'], 
	['Z','A','I','P'], 
	['T','E','S','T'], 
	['B','A','M','F']
]

Data Structure:
Trie - Using the words from dictionary.txt, we will build a trie. The trie will serve to efficiently check if a word is valid.
Linked List to store matches?

Algorithm:
Traverse the tiles. For each tile, test every single combination of words that can be generated from the tile. Test means using the trie to see if the word exists in the dictionary. If in trie, then add to linked list.

After traversing all tiles, sort pairs (index, length of word) on length of word (index is the index of the word in the linked list). 

Math:
There are x total combination of words that can be produced from each tile. We have 16 tiles so that x * 16 combinations.


Efficiency:
Finding Word Efficiency:

Trie Efficiency:

Sorting Efficiency: