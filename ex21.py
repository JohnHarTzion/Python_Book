def add(a, b):
	print("ADDING %d + %d" % (a, b))
	return a + b

def substract(a, b):
	print("SUBRACTING %d - %d" % (a, b))
	return a - b

def multiply(a, b):
	print("MULTIPLYING %d * %d" % (a, b))
	return a * b

def divide(a, b):
	print("DIVIDING %d / %d" % (a, b))
	return a / b

print("Let's do some math with just functions")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

print("Here is a puzzle.")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

def normal(a, b, c, d, e):
	div = a/b
	mult = c * div
	sub = d - mult
	adit = e + sub
	print("Result: %d" % adit)
	return(adit)

normal(iq, 2, weight, height, age)