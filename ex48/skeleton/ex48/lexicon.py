def scan(word):

	dict1 = {
			'north': 'direction',
			'south': 'direction',
			'east': 'direction',
			'go': 'verb',
			'kill': 'verb',
			'eat': 'verb',
			'the': 'stop',
			'in': 'stop',
			'of':'stop',
			'bear': 'noun',
			'princess': 'noun',
			1234: 'number',
			3: 'number',
			91234: 'number',
			'ASDFADFASDF': 'error',
			'IAS': 'error'
	}
	a = word.split()
	key = []

	for i in a:
		if type(i) == str and i in dict1:
			key.append((dict1[i], i))
		if type(i) == int and int(i) in dict1:
			key.append((dict1[i], int(i)))


	return key