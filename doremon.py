from turtle import *
bgcolor('lightgreen')
speed(10)

color('red')
penup()
goto(-100,220)
pendown()
write('DOREMON',font=('constantia',30,'bold'))
penup()
goto(0,0)
pendown()

color('black')

#ryftghjlk
fillcolor('deepskyblue')
begin_fill()
circle(100)
end_fill()
fillcolor('white')
begin_fill()


circle(80)
end_fill()
lt(90)

#lefteye
penup()
goto(0,150)
pendown()

fillcolor('white')
begin_fill()
circle(20)
end_fill()

penup()
goto(-3,150)
pendown()

fillcolor('black')
begin_fill()
circle(10)
end_fill()
penup()
goto(-4,150)
pendown()
fillcolor('white')
begin_fill()
circle(5)
end_fill()

#righteye
penup()
goto(0,150)
pendown()

fillcolor('white')
begin_fill()
circle(-20)
end_fill()

penup()
goto(3,150)
pendown()
fillcolor('black')
begin_fill()
circle(-10)
end_fill()
penup()
goto(4,150)
pendown()
fillcolor('white')
begin_fill()
circle(-5)
end_fill()

#nose
penup()
goto(10,110)
pendown()
fillcolor('red')
begin_fill()
circle(10)
end_fill()

#mouth

penup()
goto(-37,28)
pendown()
rt(128)
speed(5)
circle(60,80)

penup()
goto(-20,95)
pendown()
lt(48)
lt(80)
fd(40)

penup()
goto(20,95)
pendown()
rt(160)
fd(40)

rt(10)
penup()
goto(-60,80)
pendown()
fd(120)

penup()
goto(-20,65)
pendown()
lt(190)
fd(40)

penup()
goto(20,65)
pendown()
lt(160)
fd(40)


hideturtle()
input()