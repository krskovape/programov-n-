from turtle import forward, left, right, speed, exitonclick

speed(0)

def vlocka(a, u):
    if (u == 0):
        return
    a /= 3
    forward(a)
    left(60)
    forward(a)
    right(60)
    forward(60)
