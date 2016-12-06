from sys import argv
from os.path import exists

script, from_file, to_file = argv

#We could do these two on one line too, how?
indata = open(from_file).read(); out_file = open(to_file, 'w').write(indata); print ("Alright, all done")