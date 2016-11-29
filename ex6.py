#there are 10 types of people
x = "There are %d types of people." % 10
#variable for binary
binary = "binary"
#variable for don't
do_not = "don't"
#those who know binary and those who don't
y = "those who know %s and those who %s." % (binary, do_not)

#print "there are 10 types of people"
print (x)
#print "those who know binary and those who don't"
print (y)

#print "I said: there are 10 types of people"
print ("I said: %r." % x)
#print "I also said: those who know binary and those who don't"
print ("I also said: '%s'." % y)

#variable for False
hilarious = False
#varibale for "Isn't that joke so funny?! and insert another variable"
joke_evaluation = "Isn't that joke so funny?! %r"

#print isn't that joke so funny?! and insert False
print (joke_evaluation % hilarious)

#varibale "this is the left side of..."
w = "This is the left side of..."
#variable "a string with a right side"
e = "a string with a right side"

#print "this is the left side of...a string with a right side"
print (w + e)

#2. There are 5 places.
#3. There are 5 places, checking by the format characters.
#4. Because it is a math variable that adds both strings.