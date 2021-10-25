from turtle import forward,left, exitonclick, speed,right

x = int(input("Zadej x: "))
y = int(input("Zadej y: "))

speed(0)

for _ in range(y):
    for _ in range(x):
        for _ in range(4):
            forward(30)
            left(90)
        forward(30)
    left(180)
    forward(30*x)
    right(90)
    forward(30)
    right(90)
exitonclick()