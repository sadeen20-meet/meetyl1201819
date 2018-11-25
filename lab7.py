from turtle import *
import random
import turtle
import math
class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius=radius
		self.color(color)
		self.speed(speed)
ball1=Ball(50,"pink",0)		
ball2=Ball(40,"blue",0)
def check_collision(ball1, ball2):

	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
turtle.mainloop()