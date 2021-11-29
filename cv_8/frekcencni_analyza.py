#vypiste pro slovo, kolik má jakých písmen

#slovnik['klic1'] = 42

slovo = "abeceda"
#slovnik == dict(slovo)
slovnik = {}

for key in range(len(slovo)):
    slovnik[slovo[key]]=key
print(slovnik)