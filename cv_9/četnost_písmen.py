import collections
from typing import Counter

slovo = str(input("Zadej slovo: "))
slovnik = {}

#1
for key in slovo:
    if key in slovnik:
        slovnik[key] += 1
    else:
        slovnik[key] = 1

for (key, val) in slovnik.items():
    print(f"Znak {key} je ve slově '{slovo}' {val}x")

#2
for pismeno in slovo:
    slovnik[pismeno] = slovnik.setdefault(pismeno, 0) + 1  #pokud písmeno ve slovníku není, vytvoří ho tam s hodnotou nula

#3
slovnik = Counter(slovo)
print(slovnik['a'])