from turtle import forward, left, speed

speed(0)

def spirala(a):
    if (a == 0):
        return
    forward(a)
    left(60)
    spirala(a-1)

spirala(80)