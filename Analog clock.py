import turtle
from turtle import*
import time

bgcolor('blue')
s=turtle.Screen()
s.tracer(0)

t=turtle.Turtle()
t.lt(90)
t.ht()


c=turtle.Turtle()
c.shape('circle')
c.pensize(20)

#circle
c.pu()
c.goto(0,-120)
c.pd()
c.fillcolor('yellow')
c.begin_fill()
c.circle(120)
c.end_fill()
c.pu()
c.goto(0,120)
c.color('lime')
c.hideturtle()


#stamp
for i in range(13):
    if i ==0:
        i=12
    c.stamp()
    c.color('black')
    b=c.pos()+(0,-8)
    c.setposition(b)
    c.write(i,move=False,font=('arial',10,'bold'),align='center')
    b=c.pos()-(0,-8)
    c.setposition(b)
    c.color('lime')
    c.circle(-120,30)

m=turtle.Turtle()
m.lt(90)
m.pensize(3)
m.ht()
m.fd(85)
m.bk(85)

h=turtle.Turtle()
h.lt(90)
h.pensize(5)
h.ht()
h.fd(70)
h.bk(70)


while True:
    for i in range(12):
        for i in range(60):
            t.clear()
            t.fd(100)
            t.bk(100)
            t.rt(6)
            s.update()
            time.sleep(1)
        m.clear()
        m.rt(6)
        m.fd(85)
        m.bk(85)
        s.update()
    h.clear()
    h.rt(6)
    h.fd(70)
    h.bk(70)
    s.update()



