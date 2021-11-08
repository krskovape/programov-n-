# open(jmeno, mode='r')
#.read()
#.write()
#.close()
#with open(...) as f:
    #blok souboru, když blok skončí, soubor se automaticky zavře

with open("C:\\Users\\petak\\Desktop\\Úvod do programování\\cv_6\\soubor.txt", encoding="utf-8") as f:
    obsah = f.read()
    print(obsah)

with open("C:\\Users\\petak\\Desktop\\Úvod do programování\\cv_6\\soubor.txt", encoding="utf-8") as f:
    for radek in f:
        print(f"Řádek: {radek}")

with open("C:\\Users\\petak\\Desktop\\Úvod do programování\\cv_6\\soubor.txt", encoding="utf-8") as f:
    for radek in f:
        print(f"Řádek: {radek.rstrip()}") #na konci řádku vždy znak pro nový řádek, proto v předchozím případě prázdný řádek mezi, rstrip ho ořízne

with open("C:\\Users\\petak\\Desktop\\Úvod do programování\\cv_6\\soubor_out.txt", mode="w", encoding="utf-8") as f:
    f.write("Ahoj")