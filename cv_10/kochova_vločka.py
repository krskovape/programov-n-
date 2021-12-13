from turtle import forward, left, right, speed, exitonclick, setpos, penup, pendown

speed(0)
penup()
setpos(-200, 200)
pendown()

def vlocka(a, u):
    if (u == 0):
        forward(a)
        return
    vlocka(a/3, u-1)
    left(60)
    vlocka(a/3, u-1)
    right(120)
    vlocka(a/3, u-1)
    left(60)
    vlocka(a/3, u-1)

#vlocka(120,3)

for _ in range(3):
    vlocka(500,4)
    right(120)

exitonclick()
