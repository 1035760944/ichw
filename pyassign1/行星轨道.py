import turtle
from math import*

def gety(a,b,x,opt):
    if opt==1:
        return b*sqrt(1-x**2/a**2)
    else:
        return -b*sqrt(1-x**2/a**2)

def init(a,t):
    t.penup()
    t.goto(-a, 0)
    t.pendown()

def  draw(a,b,t):
    for x in range(2*a):
        t.goto(x - a, gety(a, b, x - a, -1))
    for x in range(2*a+1):
        t.goto(a - x, gety(a, b, a - x, 1))

t=turtle.Pen()
t.speed(0)
init(20,t)
draw(20,18,t)
t=turtle.Pen()
t.speed(0)
init(40,t)
draw(40,36,t)
t=turtle.Pen()
t.speed(0)
init(60,t)
draw(60,54,t)
t=turtle.Pen()
t.speed(0)
init(80,t)
draw(80,72,t)
t=turtle.Pen()
t.speed(0)
init(100,t)
draw(100,90,t)
t=turtle.Pen()
t.speed(0)
init(120,t)
draw(120,108,t)
t=turtle.Pen()
t.speed(0)
init(140,t)
draw(140,126,t)
t=turtle.Pen()
t.speed(0)
init(160,t)
draw(160,144,t)
turtle.done()
