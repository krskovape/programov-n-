def read_int(dotaz):
    while True:
        try:
            astr = input(dotaz)
            num = int(astr)
            return num
        except ValueError:
            print("Nezadal jsi celé číslo.")


num = read_int("Zadej číslo: ")
print(f"Číslo je {num}")