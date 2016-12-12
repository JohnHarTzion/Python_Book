people = 20
cats = 30
dogs = 15

if people < cats:
	print ("Too many cats! The world is doomed")

if people > cats:
	print ("Not many cats! The world is saved")

if people < dogs:
	print ("The world is drooled on!")

if people > dogs:
	print ("The world is dry!")


dogs += 5

if people >= dogs:
	print ("People are greater than or equal to dogs.")

if people <= dogs:
	print ("People are less than or equal to dogs.")

if people == dogs:
	print ("People are dogs.")

#1. If makes the code check to see if the variables match the statement after the if.
#2. Because if it is not indented, Python does not read it as part of the if statement.
#3. If it is not indented, then Python either gives an error or does what the code says.
#4. Yes you can. An if statement can compare more than just two variables, so you can use and or or
#5. If you change the variables, then the prints will change because the variables are the ones who determine which statement gets printed.