from math import pi
def plocha_kruhu(polomer):
    return pi*(polomer*polomer)

polomer = int(input("Zadej poloměr kruhu: "))
plocha = plocha_kruhu(polomer)
print(f"Plocha kruhu o poloměru {polomer} je {plocha}")