class Tile(object):
	def __init__(self, x, y, letter):
		self.x = x
		self.y = y
		self.letter = letter
		self.visited = False