print ("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
	print ("There's a giant bear here eating a cheese cake. What do you do?")
	print ("1. Take the cake")
	print ("2. Scream at the bear")
	print ("3. Quietly go back from where you came.")

	bear = input("> ")

	if bear == "1":
		print ("The bear eats your face off. Good job!")

	elif bear == "2":
		print (" The bear eats your face off. Good job!")

	else:
		print("Well, doing %s is probably better. Bear runs away" % bear)

elif door == "2":
	print ("You stare into the endless abyss at Cthulu's retina.")
	print ("1. Blueberries")
	print ("2. Yellow jacket clothespins.")
	print ("3. Understanding revolves yelling melodies.")

	insanity = input("> ")

	if insanity == "1" or insanity == "2":
		print ("Your body survives powered by a wind of jello. Good job!")
		print ("1. You talk to Cthulu and try to reason with it.")
		print ("2. You stab the retina and hope for the best.")

		body = input("> ")

		if body == "1":
			print("Cthulu lets you pass and you encounter some interesting picture.")
		else:
			print("Cthulu laughs at you while burning your body in a searing pain.")
	else:
		print("The insanity rots your eyes into a pool of muck. Good job!")

else:
	print("You stumble around and fall on a knife and die. Good job!")