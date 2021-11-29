# slovniky - seznam dvojic klíč hodnota
# {"klic1":"hodnota1","klic2":"hodnota2"}
# jedenslovník popisuje jednu entitu, každý atribut je klíč
# jako hodnotu můžu uložit cokoliv, k líč musí být NEMĚNNÝ - vnitřní struktura se nemění
# ve slovníku musí být prostě klíče neměnné
# -> uchování nějaké hodnoty
# překladová tabulka (slovník)
# výhoda: pokud mě zajímmají jen klíče -> rychle na ně odpovídá -> rychle dokáže klíč najít

slovnik = {'klic1':'hodnota1','klic2':'hodnota2'}
print(slovnik['klic1'])
slovnik['klic3'] = 'hodnota3'
print(slovnik)
slovnik['klic1'] = 42
print(slovnik)

for key in slovnik: # vzdy iteruje pres klice, pres hodnoty musime napsat .values
    print(f"{key} -> {slovnik[key]}")
for val in slovnik.values(): 
    print(f"value: {val}")
for (key, val) in slovnik.items(): # tiskne celé n-tice
    print(f"{key} -> {val}")

if 'klic1' in slovnik:
    print(slovnik['klic1'])