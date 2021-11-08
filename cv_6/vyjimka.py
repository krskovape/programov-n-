def podil(a,b):
    return a/b
    #returnem končím, teď try block jakoby zakomentovaný
    try:
        res = a/b
    except ZeroDivisionError:
        res = 2000
    return res

def vydel_nulou(a):
    return podil(a,0)
    try:
        res = podil(a,0)
    except ZeroDivisionError:
        res = 1000
    return res

try:
    print(vydel_nulou(int(input("Zadej číslo: "))))
except ZeroDivisionError:
    print("Nulou dělit nelze")
except ValueError:
    print("Nezadal jsi číslo.")
#else - pokud výjimka nenastala, provede se před finally
else:
    pass
#finally - provede se, ať nastala výjimka nebo ne
finally:
    pass




try:
    val = int(input("Zadej číslo: "))
except ValueError:
    #print("Nebylo zadáno číslo!")
    #exit()
    print("Nebylo zadáno číslo, volím 42")
    val = 42
print(f"Bylo zadáno číslo {val}")