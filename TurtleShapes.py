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
turtle.register_shape('new_shape',((100,0),(100,100),(0,100),(50,-50),(0,0)))

turtle.goto(50,-50)
turtle.goto(100,100)
turtle.goto(0,100)
turtle.goto(50,-50)
turtle.goto(0,0)
turtle.mainloop()
'''
class Animal(object):
	def__init__(self, sound, name,age,fv_color):
