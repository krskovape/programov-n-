l = ["a", 2, None, True, "asd"]
print(f"L:{l}")
print(l[2:4])
l.append("Posledni")
print(f"L:{l}")
print(l.pop())
print(f"L:{l}")
del l[3]
print(f"L:{l}")
l[1] = l[1]+4
print(f"L:{l}")