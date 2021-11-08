from turtle import forward,left, exitonclick, speed,right

#x = int(input("Zadej x: "))
#y = int(input("Zadej y: "))
x=4
y=3

speed(0)

for _ in range(y):
    for _ in range(x):
        for _ in range(8):
            forward(30)
            left(60)
        right(120)
    right(120)
    for _ in range(x):
        forward(30)
        right(60)
        forward(30)
        left(60)
    right(120)
    forward(30)
    right(60)
    forward(30)
    right(60)
exitonclick()