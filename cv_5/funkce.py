def read_int(prompt):
    astr = input(prompt)
    return int(astr)

def print_float3(num):
    print(f"{num:.3f}")

def square_area(side):
    return side*side

side = 37
area = square_area(side)
print(f"Plocha čtverce o straně {side} je {area}" )

print_float3(12.345678)

num = read_int("Zadej číslo: ")
print(f"Zadal jsi {num}")

from math import pi
def plocha_kruhu(polomer):
    return pi*(polomer*polomer)

polomer = int(input("Zadej poloměr kruhu: "))
plocha = plocha_kruhu(polomer)
print(f"Plocha kruhu o poloměru {polomer} je {plocha}")