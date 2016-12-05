from sys import argv

script, user_name = argv
prompt = 'Answer: '

print ("Hi %s, I'm the %s script." % (user_name, script))
print ("I'd like to ask you a few questions")
print ("Do you like me %s?" % user_name)
likes = input(prompt)

print ("Where do you live %s?" % user_name)
lives = input(prompt)

print ("How old are you %s?" % user_name)
old = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print ("Alright, so you said %r about liking me. You live in %r. Not sure where that is. You said you are %r And you have a %r computer. Nice." % (likes, lives, old, computer))