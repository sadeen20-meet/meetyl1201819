'''
import turtle
angle=145
length=120
for i in range(5):
	turtle.forward(length)
	turtle.right(angle)



turtle.mainloop()
'''
'''
import turtle 
turtle.begin_fill()
turtle.goto(0,100)
turtle.goto(100,100)
turtle.goto(100,0)
turtle.goto(0,0)
turtle.goto(40,-60)
turtle.goto(100,0)
turtle.end_fill()
turtle.mainloop()
'''
import turtle
turtle.speed(0)
turtle.pen(10)

for s in range (365):

	
	turtle.forward(300)
	turtle.right(45)
	turtle.forward(150)
	turtle.right(100)
	turtle.forward(75)
	turtle.penup()
	turtle.home()
	turtle.right(s)
	
	turtle.pendown()


turtle.mainloop()
