##Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## is-a
class Dog(Animal):
	
	def __init__(self, name):
		## has-a
		self.name = name

## is-a
class Cat(Animal):

	def __init__(self, name):
		##has-a
		self.name = name

##is-a
class Person(object):

	def __init__(self, name):
		## has-a
		self.name = name
		## Person has-a pet of some kind
		self.pet = None


	def greet(self):
		print "hello"
##is-a
class Employee(Person):

	def __init__(self, name, salary):
		## has-a Hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## has-a
		self.salary = salary

##is-a
class Fish(object):
	pass

##is-a
class Salmon(Fish):
	pass

##is-a
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")
## Satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet named Satan
mary.pet = satan

## Frank is-a Employee
frank = Employee("Frank", 120000)

## Frank has-a pet named Rover
frank.pet = rover

## Flipper is a fish
flipper = Fish()

## Crouse is-a Salmon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()

#Multiple inheritance is when one class has two or more parent classes. You do this by writing class something(other_thing, more_other_something).