'''
class Animal(object):
	def __init__(self, sound, name,age,fv_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.fv_color = fv_color
	def eat(self,food):
			print('yummy!! ' + self.name + 'is eating' + food)
	def description(self):
			print(self.name + 'is' + str(self.age) + 'years old loves the color ' + self.fv_color)
	def make_sound(self):
			print(self.sound*3)
a = Animal('meow','cat', 3,'blue')
a.eat("meat")
a.description()
a.make_sound()

class person(object):
	def __init__(self,name,age,city,gender):
		self.name=name
		self.age=age
		self.city=city
		self.gender = gender
	def eat_breakfast(self,fav_breakfast):
		print(self.name + ' is eating ' + fav_breakfast)
	def watch(self,fav_series):
		print(self.name + " is watching " + fav_series)
fav_breakfast=('pancakes')
s=person('sadeen',14,'jerusalem','female')
s.eat_breakfast("pancakes")
s.watch("cukur")
'''
