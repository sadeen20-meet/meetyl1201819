import turtle #so important we use it all the time it doesn't need a comment 
from turtle import Turtle 
import time #we will need it later in the code 
import math # we will need it later in the collision part 
import random #we are ging everytime we need the value of the variables to be chosen randomly 

turtle.tracer(0,1) #makes the turtle move smoother abd zero is the best 
turtle.penup() #we don't need lines all around 
turtle.hideturtle()#we don't need to see that black arrow
score=0#we will need it later in making the score method 
lives=3#we will need it later 
# global waiting
waiting=0
#i want my ball to move by arrows yes it needs more lines and code but it's more fun and easier so
#here is how i made it 
turtle.register_shape("bgpic.gif")
turtle.bgpic("bgpic.gif")
UP_ARROW = "Up" 
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right" 
SPACEBAR = "space" 
P=""
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
    global direction #it's always the same 
    if not direction == DOWN:



        direction=UP #this means that the direction is now up 
   
        # print("You pressed the up key")#no need for this just to make sure my code works well 
def down():
    global direction
    if not direction == UP:
        direction=DOWN #this means that the direction now is down 
    
        # print('you pressed the down key!')#no need for this just to make sure my code works well 

def left():
    global direction
    if not direction == RIGHT:
        direction=LEFT #this means that the direction now is left 
   
        # print('you pressed the left key!')#no need for this just to make sure my code works well 

def right():
    global direction
    if not direction == LEFT:
        direction=RIGHT #this means that the direction now  is right 
   
        # print('you pressed the right key!')#no need for this just to make sure my code works well 

global paused
paused = False
def pause():
	global paused
	paused = not paused
	print("game is paused")
	if paused == False:
		run_game()


turtle.onkeypress(up, UP_ARROW) 
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(pause, SPACEBAR)
turtle.listen()
#i made the whole game in one file idk why nut yeah so here is the code for the class
#the class Ball inherits from the big class turtle and here is how the code goes :
class Ball(Turtle):
	def __init__(self, radius, x, y, dx, dy, color):
		Turtle.__init__(self)
		self.shape("circle")
		self.penup()
		self.radius=radius
		self.dx=dx
		self.dy=dy
		self.shapesize(radius/10)
		self.color(color)
		self.goto(x, y)
#as i said i want it to move by using the arrows 
	def move_my_ball(self,width,height):
		global direction
		if direction==RIGHT:#if the direction is right it will do the following method so it moves to the right 
			self.goto( self.xcor() + self.dx,self.ycor())
			# print("You moved right!")#no need for this just to make sure my code works well 
		#and same with the other directions 
		elif direction==LEFT:
			self.goto(self.xcor() - self.dx,self.ycor())
			# print("You moved left!")
		
		elif direction==UP:
			self.goto(self.xcor(), self.ycor()+self.dy)
			# print('you moved up !')
			
		elif direction==DOWN:
			self.goto(self.xcor(), self.ycor()-self.dy)

			# print('you moved down!')
		oldx=self.xcor()            
		oldy=self.ycor()
		newx=oldx+self.dx
		newy=oldy+self.dy
		#and if the hit the limit of the width or height that we want it well change its direction to the opposite of 
		#what it was ,here"s the code:
		if newx >= width: 
			direction=LEFT
		if newx <= -width:
			direction=RIGHT
			
		if newy>= height:
			direction=DOWN
		if newy<= -height:
			direction=UP

			

############P A U S E ### who ever is reading this i hope you are having a good day <3 don't forget to smile today 
#you are so beautiful inside out don't ever forget this okay?and good luck with your work <3 ###

#this functon i will use it in another function called move_all_balls so as you can tell it moves the other balls 
	def move(self, width, height):
		oldx=self.xcor()            
		oldy=self.ycor()
		newx=oldx+self.dx
		newy=oldy+self.dy
		#and if the hit the limit of the width or height that we want it well change its direction to the opposite of 
		#what it was ,here"s the code:
		if newx >= width or newx <= -width:
			self.dx= -self.dx
			newx=oldx + self.dx
		if newy>= height or newy<= -height:
			self.dy= -self.dy
			newy=oldy + self.dy
		self.goto(newx,newy)
		turtle.penup()		

#variables we need to add we will use them later 
RUNNING=True 
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

#here's MY_BALL's characterstics ;)
MY_BALL=Ball(40,0,0,10,10,"blue")

#these will help us with the variables that their values will be cjosen randomly but also in the range that we want:

NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=5
BALLS=[]
#so we want to make balls of course but we want them to have values that are chosen randomly so here is the code:
for i in range (NUMBER_OF_BALLS):
	RADUIS=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT- MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	color=(random.random(),random.random(),random.random())
	BALL=Ball(RADUIS, x, y, dx, dy, color)#the code can tell what this is ,it's basically definding the balls 
	BALLS.append(BALL)					  #as many as the for loop work and add them to BALLS list 

#here's the function that continue the move funcion's work whic is to move all the balls 
def move_all_balls(BALLS, width,height):#when we call the function we will put the height and width that we want the
	for BALL in BALLS:					# ballsto move in 
		BALL.move(width, height)


#here we start the code of the collision thing you of course know  this game so as you now when the balls colide
#they go to a different direction and the size and color of them changes so here's the code 
def collide(ball_a , ball_b):
	if (ball_a==ball_b): #this checks if ball a and ball b are actually the same ball so if yes nothing will happen 
		return False
	else:#if not ! it will check if there is a collision by doing this math method that depends on the radius 
		x2=ball_a.xcor()
		x1=ball_b.xcor()
		y2=ball_a.ycor()
		y1=ball_b.ycor()
		D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
		if ball_a.radius + ball_b.radius >= D:
			return True
		else:
			return False
def check_all_balls_collision():# while coding this my laptop went craaazzzyyyy the mouse didn't work nothing worked 
#the laptop stopped working augh ,,, anyways this is he code where we use the "collide" function to check if there is 
#a collision and if yes all the values of the two colliding balles change so the game continues and for this we used 
#a nested loop(one or more than one loop inside each other)
	for ball_a in BALLS:
		for ball_b in BALLS:

			if collide(ball_a,ball_b):
				color=(random.random(),random.random(),random.random())
				RADUIS=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT- MAXIMUM_BALL_RADIUS)
				y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				while x in range (int(-MY_BALL.radius+MY_BALL.xcor()),int(MY_BALL.xcor()+MY_BALL.radius)):
					x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT- MAXIMUM_BALL_RADIUS)
				while y in range (int(-MY_BALL.radius+MY_BALL.ycor()),int(MY_BALL.ycor()+MY_BALL.radius)):
					y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

				dx= 0
				dy= 0
				while dx==0:
					dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while dy == 0:
					dy= random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)

				if ball_a.radius<ball_b.radius:
					ball_a.goto(x,y)
					ball_a.radius=RADUIS
					ball_a.shapesize(RADUIS/10)
					ball_a.dx=dx
					ball_a.dy=dy
					ball_a.color(color)
					ball_b.radius=ball_b.radius+1
					ball_b.shapesize(ball_b.radius/10)
				else:
					ball_b.goto(x,y)
					ball_b.radius=RADUIS
					ball_b.shapesize(RADUIS/10)
					ball_b.color(color)
					ball_b.dx=dx
					ball_b.dy=dy
					ball_a.radius=ball_a.radius+1
					ball_a.shapesize(ball_a.radius/10)	


def check_myball_collision():
	global score
	global lives
	for BALL in BALLS:
		if collide(MY_BALL,BALL):
			MY_BALL_RADIUS=MY_BALL.radius
			ballRadius=BALL.radius
			RADUIS=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
			x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT- MAXIMUM_BALL_RADIUS)
			y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			while x in range (int(-MY_BALL.radius+MY_BALL.xcor()),int(MY_BALL.xcor()+MY_BALL.radius)):
				x=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT- MAXIMUM_BALL_RADIUS)
			while y in range (int(-MY_BALL.radius+MY_BALL.ycor()),int(MY_BALL.ycor()+MY_BALL.radius)):
				y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS,SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

			dx= 0
			dy= 0
			while dx==0:
				dx=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
			while dy == 0:
				dy= random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)

			if MY_BALL_RADIUS< ballRadius:
				lives=lives-1
				turtle.write("you have just lost a life",move=False, align="center", font=("Arial", 30, "normal"))
				lives_label.clear()
				lives_label.write("lives: "+str(lives),font=("Arial", 25,"normal"))
				global waiting
				waiting += 50
				time.sleep(1)
				turtle.undo()
				return False
			if MY_BALL_RADIUS> ballRadius:
				if ballRadius>30:
					MY_BALL.radius=MY_BALL.radius+5
				if ballRadius<30:
					MY_BALL.radius= MY_BALL.radius+3
				MY_BALL.shapesize(MY_BALL.radius/10)
				BALL.goto(x,y)
				BALL.radius=RADUIS
				BALL.shapesize(RADUIS/10)
				BALL.dx=dx
				BALL.dy=dy

				if ballRadius > 30:

					score=score+10
					num_label.clear()
					num_label.write("score: "+str (score),font=("Arial", 25,"normal"))

				else:
					score= score + 2
					num_label.clear()
					num_label.write("score: "+str (score),font=("Arial", 25,"normal"))

	return True
				

'''
def paused():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        

        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

'''


def game_over():
	if lives==0:
		turtle.write("oppsyy game over :( ",move=False, align="center", font=("Arial", 40, "normal"))
		turtle.penup()
		turtle.goto(0,-50)
		turtle.write("your score is " + str(score),align="center",font=("Arial", 40,"normal"))
		time.sleep(30000)
		print ("oppssyyy game over")


		quit()

def congrats_youwon():
	if MY_BALL.radius>= 100:
		turtle.write("yohoo you won! :) ",move=False, align="center", font=("Arial", 40, "normal"))
		turtle.penup()
		turtle.goto(0,-70)
		turtle.write("your score is " + str(score),align="center",font=("Arial", 40,"normal"))
		for a in range(10):
			color=(random.random(),random.random(),random.random())
			MY_BALL.color(color)
		time.sleep(30000)
		quit()








#this draws a border so it's easier and more clear for the player 
border=turtle.clone()
border.ht()
border.penup()
border.goto(-750,500)
border.pendown()
border.goto(750,500)
border.goto(750,-500)
border.goto(-750,-500)
border.goto(-750,500)
'''
import tkinter as tk
from PIL import ImageTk

canvas = Canvas(width = 200, height = 200, bg = 'blue')
canvas.pack(expand = YES, fill = BOTH)
image = Image.open("/home/student/Pictures/milky-way-concordia-pakistan.jpg")
backgroundImage=ImageTk.PhotoImage(image)

mainloop()
'''

#numbers label for the lives  
lives_label=turtle.Turtle()
lives_label.ht()
lives_label.penup()
lives_label.color('pink')
lives_label.width('10')
lives_label.goto(500,400)
lives_label.write("lives: "+str(lives),font=("Arial", 25,"normal"))


#numbers label for the score 
num_label=turtle.Turtle()
num_label.ht()
num_label.penup()
num_label.color('black')
num_label.width('10')
num_label.goto(550,-500)
num_label.write("score: "+str (score),font=("Arial", 25,"normal"))


#annnddd heeerrreee where we press the start button of the game yoohooo  , we call all the functions we coded so 
#the game starts foreveeerr cause whle true is always true 
def run_game():
	global paused
	global lives
	global waiting
	while lives>0:

		if not paused:
			MY_BALL.penup()#we don't need lines on the screen 
			MY_BALL.move_my_ball(700,500)
			turtle.update()
			move_all_balls(BALLS, 700, 500)
			check_all_balls_collision()
			if waiting == 0:
				check_myball_collision()
			else:
				waiting -= 1
			turtle.update()
			time.sleep(SLEEP)


	if lives <= 0:
		game_over()


	if MY_BALL.radius>=100:
		congrats_youwon()

run_game()
turtle.mainloop()
