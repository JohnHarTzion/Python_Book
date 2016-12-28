def scan(word):

	dict1 = {
			'north': 'direction',
			'south': 'direction',
			'east': 'direction',
			'west': 'direction',
			'go': 'verb',
			'leave': 'verb',
			'kill': 'verb',
			'eat': 'verb',
			'the': 'stop',
			'out': 'stop',
			'in': 'stop',
			'of':'stop',
			'bear': 'noun',
			'princess': 'noun',
			'ASDFADFASDF': 'error',
			'IAS': 'error'
	}
	a = word.split()
	key = []

	for i in a:
		if type(i) is str and i in dict1:
			key.append((dict1[i], i))
		elif type(int(i)) is int:
			key.append(('number' , int(i)))
	return key