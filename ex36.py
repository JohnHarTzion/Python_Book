from sys import exit

def first_room():
	print("You are in a dark room and only a small source of light.")
	candle = False
	matches = False
	door = False

	next = raw_input("> ")

	if next == "search room":
		print("You find a candle and matches on the floor. You light the candle and see a door.")
		candle = True
		matches = True
		door = True

		next = raw_input("> ")

		if next == "open door":
			second_room()

	else:
		print("You can't see anything.")

def second_room():
	print("You open the door and see 2 buttons, one on your right and one on your left. Which one do you press?")

	next = raw_input("> ")

	if next == "left":
		print("The door opens and you walk through it.")
		third_room()

	if next == "right":
		dead("The walls slam on you and you are crushed.")
		exit(0)
	else:
		print("That was not one of the choices.")
		second_room()

def third_room():
	print("In this room you three chests. Do you open number 1, number 2, or number 3?")

	next = raw_input("> ")

	if int(next):
		chest = next
	else:
		print("Those are not the choices.")
		third_room()
	if chest == "1":
		dead("You open chest number 1 and a trap door opens under you and you fall to your death.")
	elif chest == "2":
		print("You open chest number 2 and see 1000 pieces of gold. You win!")
	elif chest == "3":
		dead("You open chest number 3 and a rock falls on top of you and crushes you.")

def dead(why):
	print(why, "You lose!")
	exit(0)

first_room()