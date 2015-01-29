""" 
A do-nothing program, an exercise for me 
to hammer in some concepts to myself
"""

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a animal
class Dog(Animal):
	def __init__(self, name):
		## Dog has-a name
		self.name = name
	def woof():
		print "{} says Woof!".format(self.name)

## Cat is-a animal
class Cat(Animal):
	
	def __init__(self, name):
		## Cat has-a name
		self.name = name
	def meow():
		print "{} says Meow!".format(self.name)
		
## Person is-a object
class Person(object):
	def __init__(self, name):
		## Person has-a name
		self.name = name
		
		## Person has-a pet of some kind
		self.pet = None

## Employee is-a person
class Employee(Person):
	def __init__(self, name, salary):
		## Employee has-a name because it is-a person? 
		## hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## Employee has-a name
		self.salary = salary
		
## Fish is-a object
class Fish(object):
	def swim():
		print "Swim, swim, swim!"
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass
	
## Halibut is-a Fish
class Halibut(Fish):
	pass
	
## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## mary has-a pet, satan
mary.pet = satan

mary.pet.meow
## frank is-a Employee, that has-a name "Frank", and has a salary, 120000
frank = Employee("Frank", 120000)

## frank has-a pet, rover
frank.pet = rover

frank.fired

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
harry.swim