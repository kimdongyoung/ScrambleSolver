# Print out (length of word): number of words with the length of word
with open('../dictionary/testDictionary.txt') as dictionary:
	results = [0] * 30
	for word in dictionary:
		word = word.strip()
		results[len(word)] += 1
	print results