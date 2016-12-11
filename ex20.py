#imports argv from system
from sys import argv

#script and input_file are argv
script, input_file = argv

#print all method that prints everything in the argument
def print_all(f):
	print f.read()

#goes back to line 0
def rewind(f):
	f.seek(0)

#a function that prints whatever is in the line that it is on
def print_a_line(line_count, f):
	print line_count, f.readline()

#finds the file you put in as an argument in the runner.
current_file = open(input_file)

print ("First let's print the whole file: \n")

#prints the whole file that you put in in the runner
print_all(current_file)

print ("Now let's rewind, kind of like a tape.")

#goes back to line 0 in that file
rewind(current_file)

print ("Let's print three lines:")

#sets the current line in the file as line 1
current_line = 1
print_a_line(current_line, current_file)

#takes the current line from before, and adds 1 to make it line 2
current_line += 1
print_a_line(current_line, current_file)

#takes the second current line and adds one to make it line 3
current_line += 1
print_a_line(current_line, current_file)


#2. The first current line is passed in line 35 and is equal to 1. But passing it in the method as the first varibale, it becomes the line_count varibale for that method.
# in line 39 you add one to the current_line variable and make it 1+1 to 2. So when you pass it in the next call of print_a_line, current_line variable is 2, which makes line_count as 2.
