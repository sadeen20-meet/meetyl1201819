import turtle 
from turtle import Turtle 
import time
import math
import random 
turtle.tracer(1)
turtle.penup()
turtle.hideturtle()
class Ball(Turtle):
	def __init__(self, radius, x, y, dx, dy, color):
		Turtle.__init__(self)
		self.shape("circle")
		self.radius=radius
		self.x=x
		self.y=y
		self.dx=random.randint(20,40)/40
		self.dy=random.randint(30,50)/40
		self.shapesize(radius/10)
		self.color(color)
	def move (self,screen_width,screen_height):
		



RUNNING=True 
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(40,0,0,3,3,"blue")
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5
BALLS=[]
for BALL in range (NUMBER_OF_BALLS):
	RADUIS=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHt- MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	color=(random.random(),random.random(),random.random())
	BALL=Ball(RADUIS, x, y, dx, dy, color)
	BALLS.append(BALL)

#moving code!!!
