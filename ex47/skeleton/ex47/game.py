class Room(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}

	def go(self, direction):
		return self.paths.get(direction, None)

	def add_paths(self, paths):
		self.paths.update(paths)


class New_Room(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.moves = {}

	def go(self, direction):
		return self.moves.get(direction, None)

	def add_moves(self, moves):
		self.moves.update(moves)