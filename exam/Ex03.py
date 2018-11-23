from turtle import *
import math

def tri(length = 100):
    t1.left(60)
    for i in range(3):
        t1.right(120)
        t1.forward(length)

def rec(length=100):
    t1.right(15)
    for i in range(4):
        t1.right(90)
        t1.forward(length)


wn = Screen()
t1 = Turtle()

R=int(input())

r = R/2

t1.home()
t1.circle(r) #r은 반지름.
t1.goto(0,R)

tri(math.sqrt(3)*r)
rec(math.sqrt(2)*r)
print('%.2f'%(R*r))

wn.mainloop()