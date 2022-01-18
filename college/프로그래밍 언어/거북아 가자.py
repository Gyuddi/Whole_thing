import turtle
t=turtle.Turtle()

x1=int(input("큰 원의 중심좌표 x1"))
y1=int(input("큰 원의 중심좌표 y1"))
r1=int(input("큰원 반지름"))
x2=int(input("작은 원의 중심좌표 x2"))
y2=int(input("작은 원의 중심좌표 y2"))
r2=int(input("작은원 반지름"))

t.up()
t.goto(x1,y1)
t.down()
t.circle(r1)
t.up()
t.goto(x2,y2)
t.down()
t.circle(r2)
#원점 사이의 거리와 작은 원의 반지름의 합이 큰 원의 반지름보다 작아야한다.
if (((x1-x2)**2+(y1-y2)**2)**0.5)+r2<=r1:
    t.write("이 원은 큰 원의 내부에 있습니다")
else:
    t.write("이 원은 큰 원의 외부에 있습니다.")
       
