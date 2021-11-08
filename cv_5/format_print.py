#jmeno = "Hugo"
#vek = 40
#jmeno = input("Zadej jméno\\\n")
#vek = int(input(f"{jmeno}, zadej věk: "))
#astr = f"Ahoj \"{jmeno}\", {vek} {{}} let stary"
#print(astr)

print("\N{SMILING FACE WITH SMILING EYES}")
print("\U0001F60A")

pattern = "Toto je {}. iterace cyklu"
for i in range(10):
    print(pattern.format(i))

pattern = "{poradi}: Toto je {poradi}. iterace cyklu"
for i in range(10):
    print(pattern.format(poradi=i))

#číslo na tři desetinná místa - za : formát, .precision, f- fixed position?
print(f"1/3 = {1/3:.3f}")

a= input()
#strip ořeže bílé znaky (mezera, tabulátor, konec řádky) na začátku a konci řádku, lstrip a pstrip jen z jedné strany
a = a.strip()
