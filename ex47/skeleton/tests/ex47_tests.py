from nose.tools import *
from ex47.game import Room, New_Room

def test_room():
	gold = Room("GoldRoom",
		"""This room has gold in it you can grab. There's a door to the north.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})

def test_room_paths():
	center = Room("Center", "Test room in the center.")
	north = Room("North", "Test room in the north.")
	south = Room("South", "Test room in the south.")

	center.add_paths({'north': north, 'south': south})
	assert_equal(center.go('north'), north)
	assert_equal(center.go('south'), south)

def test_map():
	start = Room("Start", "You can go west and down a hole.")
	west = Room("Trees", "There are trees here, you can go east.")
	down = Room("Dungeon", "It's dark down here, you can go up.")

	start.add_paths({'west':west, 'down':down})
	west.add_paths({'east':start})
	down.add_paths({'up':start})

	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)

def test_new_room():
	main = New_Room("MainRoom", "You wake up in a room with only one way out, to the north.")
	assert_equal(main.name, "MainRoom")
	assert_equal(main.moves, {})

def test_room_moves():
	center = New_Room("Center", "Test room in the center.")
	north = New_Room("North", "Test room in the north.")
	south = New_Room("South", "Test room in the south.")

	center.add_moves({"north": north, "south": south})
	assert_equal(center.go("north"), north)
	assert_equal(center.go("south"), south)

def test_new_map():
	start = New_Room("Start", "You can go north or west.")
	north = New_Room("Bunnies", "There are bunnies here, you can go north.")
	west = New_Room("Trees", "You can see some trees in here. You can go south.")

	start.add_moves({"north": north, "west": west})
	assert_equal(start.go("north"), north)
	assert_equal(start.go("west"), west)
