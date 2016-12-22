from sys import exit
from random import randint
from ex45_base import *

class Scene(object):

	def enter(self):
		print("This scene is not yet configured. Subclass it and implement enter()")
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print("\n----------")
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)


class Entrance(Scene):

	def enter(self):
		print("You are John Smith, the secret operative for the DIS, the Department of International Security.")
		print("You go around saving the country from different threats.")
		print("You are at the entrance of a secret nuclear site for the Syrian Governmant.")
		print("You are going to need to use stealth and cunning to reach the general with the codes and disable the system.")
		print("There is a door in front of you.")
		print("What do you do?")

		action = raw_input("> ")

		if action == "open door":
			print("You open the door and the alarm goes off.")
			print("Within seconds you are surrounded by 50 soldiers and get shot for traspassing.")
			return 'death'

		elif action == "look for alarm":
			print("You look for an alarm and you find it next to the door.")
			print("Which one of your items do you want to use?")
			print("Warning: Certain items are only useable once. Be careful.")
			print("1. Knife")
			print("2. Gum Wrapper")
			print("3. EMP Grenade")

			item = raw_input("> ")

			if item == "1":
				print("You use the knife to disable the alarm and ")
				return 'weapons_room'
			elif item == "2":
				print("You take the gum wrapper and wrap it around the alarm.")
				print("You open the door and the alarm still goes off.")
				print("You are surrounded by 50 soliders and get shot for traspassing.")
				return 'death'
			elif item == "3":
				global EMP
				EMP = False
				print("You place an EMP grenade in front of the gate and it neutralizes the alarm.")
				return 'weapons_room'
			else:
				print("That was not an option.")
				return 'entrance'
		else:
			print("That was no an option.")
			return 'entrance'


class FinishedScene(Scene):
	
	def enter(self):
		exit(1)

class WeaponsRoom(Scene):
	
	def enter(self):
		print("You walk into the weapons room undetected and see a guard.")
		print("He is about to radio in that he sees you.")
		print("What do you do?")
		print("1. Kill with the knife.")
		print("2. Try and choke him out")
		print("3. Throw the wrapper as a distraction and then choke him out.")

		action = raw_input("> ")

		if action == "1":
			print("You kill the guard before he could say anything. The coast is clear.")
			print("Do you grab a grenade, a rifle, or just pick up a rock?")
			print("1. Grenade")
			print("2. A rifle")
			print("3. Pick up a rock")

			pick = raw_input("> ")

			if pick == "1":
				print("You pick up a grenade.")
				return 'jail_room'
			if pick == "2":
				print("You pick up a rifle.")
				global gun
				gun = True 

				return 'jail_room'
			if pick == "3":
				print("You pick up a rock.")
				return 'jail_room'
			else:
				print("That was not an option.")
				return 'weapons_room'
		elif action == "2":
			print("You try and choke him out before he could say anything.")
			print("Too bad the radio button was clicked the whole time and you were heard.")
			print("In no time 100 soldiers have you surounded and they shoot you.")
			return 'death'

		elif action == "3":
			print("You throw the wrapper at the guard and he thinks that it's a grenade.")
			print("However, he quickly realizes it's not and pulls out a gun and shoots you.")
			return 'death'

		else:
			print("That was not an option")
			return 'weapons_room'

class Jail(Scene):
	
	def enter(self):
		print("You walk into the jail area and see a bunch of cells.")
		print("You try and look ahead to see if there are any guards.")
		print("There are 2 guards walking around. Only one has a radio on him.")
		print("What do you do?")
		print("1. Grab the guard with the radio, choke him out, and put him in a cell.")
		print("2. Grab the guard without radio, choke him out, and put him in a cell.")
		global gun
		if gun:
			print("3. Shoot both guards.")
		if not gun:
			print("3. Knife both guards. ")

		action = raw_input("> ")

		if action == "1":
			print("You grab the guard with the radio and choke him out. You throw him in a cell.")
			print("The other guard doesn't see anything, and then you choke him out too.")
			return 'boss_room'
		elif action == "2":
			print("You grab the guard without the radio, choke him out, and throw him into a cell.")
			print("The other guard notices that the first guard disappeared and he alerts others through the radio.")
			print("Within seconds 100s of guards surround you and shoot you.")
			return 'death'
		if gun and action == "3":
			print("You shoot both guards. The noise alerts others and they show up and shoot you.")
			return 'death'
		if not gun  and action == "3":
			print("You try and use the martial arts you know to overpower both guards.")
			print("You are much better than them and take out the guard with the radio first, then the other guard.")
			return 'boss_room'

class Exit(Scene):
	
	def enter(self):
		print("You reach the exit with the codes and run out.")
		print("There is a boat waiting for you where you use it to reach a friendly submarine waiting for you.")
		print("You get on the submarine and give your superior the codes.")
		print("The world is safe. YOU WIN!")
		exit(1)

class BossRoom(Scene):
	
	def enter(self):
		print("Here, you see the general that has the codes.")
		print("Do you:")
		global EMP
		global gun
		
		if EMP and not gun:
			print("1. Use the EMP grenade and turn off the lights, then steal the codes.")
			print("2. Knife the general and take the codes.")
			print("3. Try and choke the general out.")
		elif not EMP and gun:
			print("1. Shoot the general and take the codes.")
			print("2. Knife the general and take the codes.")
			print("3. Try and choke the general out.")
		elif not EMP and not gun:
			print("1. Knife the general and take the codes.")
			print("2. Try and choke the general out.")


		action = raw_input("> ")

		if EMP and not gun and action == "1":
			print("You turn the lights off and steal the codes quickly. The general is disoriented and doesn't see you.")
			return 'exit'
		elif EMP and not gun and action == "2":
			print(knife)
			return 'death'
		elif EMP and not gun and action == "3":
			print(choke)
			return 'death'
		elif not EMP and gun and action == "1":
			print("You shoot the general, take the codes, and quickly run to the exit. No one sees you and you run away.")
			return 'exit'
		elif not EMP and gun and action == "2":
			print(knife)
			return 'death'
		elif not EMP and gun and action == "3":
			print(choke)
			return 'death'
		elif not EMP and not gun and action == "1":
			print(knife)
			return 'death'
		elif not EMP and not gun and action == "2":
			print(choke)
			return 'death'

class End(Scene):

	quips = [
	"You died. You kinda suck at this.",
	"Your mom would be proud....if you were smarter.",
	"Such a luser.",
	"I have a small puppy that's better than this."
	]

	def enter(self):
		print End.quips[randint(0,len(self.quips)-1)]
		exit(1)

class Map(object):
		
		scenes = {
			'entrance':Entrance(),
			'weapons_room':WeaponsRoom(),
			'jail_room':Jail(),
			'exit':Exit(),
			'finished':FinishedScene(),
			'death':End(),
			'boss_room':BossRoom()
		}

		def __init__(self, start_scene):

			self.start_scene = start_scene

		def next_scene(self, scene_name):
			return Map.scenes.get(scene_name)

		def opening_scene(self):
			return self.next_scene(self.start_scene)


a_map = Map('entrance')
a_game = Engine(a_map)
a_game.play()