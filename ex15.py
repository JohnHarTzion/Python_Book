#imports argv from system
from sys import argv

#brings script and filename from argv
script, filename = argv

#sets variable txt to open a filename
txt = open(filename)

#prints the filename
print ("Here is your file %r:" % filename)
#prints the actual text in the file
print (txt.read())

#prints a request for the file name
print ("type the filename again:")
#sets variable named file_again with an input console
file_again = input(">")

#creates a variable with the name txt_again
txt_again = open(file_again)

#prints the txt in the file opened
print (txt_again.read())