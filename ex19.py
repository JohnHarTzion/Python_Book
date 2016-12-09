def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print ("You have %d cheeses!" % cheese_count)
	print ("You have %d boxes of crackers" % boxes_of_crackers)
	print ("Man, that's not enough for a party!")
	print ("get a blanket.\n")

print ("We can just give the function numbers directly.")
cheese_and_crackers(20, 30)

print ("OR, we can use variable from our script:")
amount_of_cheeses = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheeses, amount_of_crackers)

print ("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheeses+100, amount_of_crackers+1000)

def dollars_and_cents(dollars, cents):
	print ("You have %d dollars" % dollars)
	print ("You have %d cents \n" % cents)

print("directly:")
dollars_and_cents(10, 35)

print("Variables:")
amount_of_dollars = 20
amount_of_cents = 45

dollars_and_cents(amount_of_dollars, amount_of_cents)

print ("Math:")
dollars_and_cents(10+5, 20+30)

print ("Math and variables:")
dollars_and_cents(amount_of_dollars+5, amount_of_cents+10)

print ("Variable math:")
dollars_and_cents(amount_of_dollars+amount_of_dollars, amount_of_cents+amount_of_cents)

print ("Variable deduction:")
dollars_and_cents(20+5-amount_of_dollars, 40+20-amount_of_cents)

print ("Half Math:")
dollars_and_cents(amount_of_dollars+2, amount_of_cents)

print ("User input:")
dollars = int(input(">"))
cents = int(input(">"))
dollars_and_cents(dollars, cents)
