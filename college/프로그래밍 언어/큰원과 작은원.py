import turtle
import random
t=turtle.Turtle()
#screen=turtle.Screen()
def snowman(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(50)
    t.penup()
    t.right(90)
    t.forward(200)
    t.left(90)
    t.pendown()
    t.circle(100)

for i in range(3):
    x=random.randint(-100,100)
    y=random.randint(-100,100)
    snowman(x,y)
