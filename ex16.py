from sys import argv

script, filename = argv

print ("We're going to erase %r" % filename)
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

input("?")

print ("opening the file...")
target = open(filename, 'w')

print ("Truncating the file...")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print ("I'm going to write these to files")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we close it")
target.close()

txt = open(filename)

print(txt.read())

#4. The 'w' tells python to open in write mode.
#5. Truncate is not neccesary if you have the 'w' because it is redundent.