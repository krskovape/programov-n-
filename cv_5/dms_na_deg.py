smer = str(input("Zadej DMS, pokud převádíš dms->deg, DEG, pokud deg->dms"))

a = 'N049° 13´ 37.1234'
stupne = int(a[1:4])
minuty = int(a[6:8])
vteriny = float(a[10:-1])
vysledek = stupne + minuty/60 + vteriny/3600
print(f"Stupně: {a[0]}{vysledek:.3f}")

x = 49.227
deg = int(x)
amin1 = (x-deg)*60
amin = int(amin1)
sec = float((amin1-amin)*60)
print(f"Stupně: {deg}° {amin}´ {sec:.3f}´´")