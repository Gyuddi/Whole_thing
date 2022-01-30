import turtle
turtle.setup(width = 1000, height = 1000)

screen=turtle.Screen()
img1="토끼.gif"
img2="거북이.gif"
screen.addshape(img1)
screen.addshape(img2)

t1=turtle.Turtle()
t1.shape(img1)
t2=turtle.Turtle()
t2.shape(img2)


t1.penup()
t1.goto(-300,0)

t2.penup()
t2.goto(-300,-100)
