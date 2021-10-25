from random import randrange

z=10
y=randrange(z)
#print(y)

x=-1

print("Hádej číslo menší než",z,":")

while x!=y:
    x = int(input())
    if x>y:
        print("Hádané číslo je menší, zadej nové číslo:")
    elif x<y:
        print("Hádané číslo je větší, zadej nové číslo:")

print("Správně, číslo je" ,y)