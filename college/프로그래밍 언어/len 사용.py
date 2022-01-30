import turtle
t=turtle.Turtle()
s=int(turtle.textinput("","write the score"))
if s >0:
    t.goto(100,100)
    t.write("양수입니다")
elif s==0:
    t.goto(100,0)
    t.write("0 입니다")
elif s<0:
    t,goto(100,-100)
    t.write("음수입니다")
