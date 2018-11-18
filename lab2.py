list1=[1,2,3,4]
def make_list ():
	a=[list1[0],list1[3]]
	print(a)
make_list()
s=[1,2,4,5,8,9]
def less_than_five(d):
	for number in s:
		if number  < 5 :
			print (number)
less_than_five(s)
l2=[1,20,30,40,50,60,70]
l3=[1,10,20,40,60,4]
l4=[]
for x in l2:
	for y in l3:
		if x==y:
			l4.append(x)
print (l4)

import tkinter as tk
from tkinter import simpledialog
answer = int(simpledialog.askstring("Input", "please enter your number!", parent=tk.Tk().withdraw()))
if answer > 1 :
	prime = True
	for a in range (2,answer):
		if (answer % a) == 0:
			
			prime=False
	if prime == False:
		print(answer , "is not prime try another one ")
	else:
		print(answer,"is a prime!")