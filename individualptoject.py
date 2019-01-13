import turtle 
from turtle import Turtle 
import time
import math
import random 
turtle.tracer(1)
turtle.penup()
turtle.hideturtle()
score=0
pos_list=[]
UP_ARROW = "Up" 
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right" 
SPACEBAR = "space" 

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
direction = UP
UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300
def up():
    global direction
    if not direction == DOWN:
        direction=UP
   
        print("You pressed the up key")
def down():
    global direction
    if not direction == UP:
        direction=DOWN
    
        print('you pressed the down key!')

def left():
    global direction
    if not direction == RIGHT:
        direction=LEFT
   
        print('you pressed the left key!')

def right():
    global direction
    if not direction == LEFT:
        direction=RIGHT
   
        print('youpressed the right key!')


turtle.onkeypress(up, UP_ARROW) 
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)

turtle.listen()

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
	def move_Ball (self,screen_width,screen_height):
		



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
	def move(self,width,height):
		oldx=self.xcor()
		oldy=self.ycor()
		newx=oldx+self.dx
		newy=oldy+self.dy
		if newx >= width or newx <= -width:
			self.dx= -self.dx
			newx=oldx + self.dx
		if newy>= height or newy<= -height:
			self.dy= -self.dy
			newy=oldy + self.dy
		self.goto(newx,newy)



border=turtle.clone()
border.ht()
border.penup()
border.goto(-300,300)
border.pendown()
border.goto(300,300)
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)

#numbers label!
num_label=turtle.Turtle()
num_label.ht()
num_label.penup()
num_label.color('blue')
num_label.width('10')
num_label.goto(0,-400)
num_label.write(str (score))