import turtle
from turtle import Turtle
import math
class Ball(Turtle):
	def __init__(self, x, y, radius, dx, dy, color):
		Turtle.__init__(self)
		self.shape("circle")
		self.goto(x,y)
		self.radius=radius
		self.dx=dx
		self.dy=dy
		self.shapesize(radius/10)
		self.color(color)
	def move(self,width,height):
		self.width=width
		self.height=height
		oldx=self.xcor()
		oldy=self.ycor()
		newx=oldx+self.dx
		newy=oldy+self.dy
		Ball.goto(newx,newy)




		
ball1=Ball(100,100,20, 5, 5, "pink")		
ball2=Ball(50,50,20,3,3,"blue")
	def check_collision(ball1, ball2):

	D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	if(D >)
turtle.mainloop()