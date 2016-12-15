class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
birthday = "Happy birthday to you", "I don't want to get sued", "So I'll stop right there."
bulls = "They rally around the the family", "with pockets full of shells"

happy_bday = Song(birthday)

bulls_on_parade = Song(bulls)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

happy_joy = Song(["Happy happy",
					"Joy joy"])

