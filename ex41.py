import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class X[Y]:":
		"make a class named X that is-a Y.",
	"class X(object): \n\tdef __init__(self, j)":
		"class X has a-__init__ that takes self and J parameters.",
	"class X(object):\n\tdef M(self,j)":
		"class x has a-function named M that takes self and J parameters.",
	"foo = x()":
		"set foo to an instance of class X.",
	"foo.M(J)":
		"from foo get the M function, and call it with parameters self, M.",
	"foo.k = Q:":
		"from foo get the k attribute and set it to Q."
}

PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST == True

for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip())

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("###"))]
	other_names = random.sample(WORDS, snippet.count("###"))
	results = []
	param_names = []

	for i in range(0, snippet.count("###")):
		param_count = random.randint(1,3)
		param_names.append('.'.join(random.sample(WORDS, param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]

	for word in class_names:
		result = result.replace("###", word, 1)

	for word in other_names:
		result = result.replace("###", word, 1)

	for word in param_names:
		result = result.replace("###", word, 1)

	results.append(result)
	results.append("hey")
	print results

	return results

try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question
				print question

			raw_input("> ")
			print("ANSWER: %s\n\n" % answer)

except EOFError:
	print("\nBye")