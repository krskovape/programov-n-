print(1+2)
print(1.2)
print("2+2=",2+2)
print("Čtverec o straně 479 má obsah",479**2, "a obvod", 4*479)

strana_ctverce = 156
print("Čtverec o straně",strana_ctverce,"má obsah",strana_ctverce**2,"a obvod",strana_ctverce*4)

poloměr = -3
PI = 3.14
print("Kruh o poloměru",poloměr,"má obsah",PI*poloměr**2,"a obvod",2*PI*poloměr)

if poloměr<0:
    print("Strana čtverce nesmí být záporná")
else:
    print("Kruh o poloměru",poloměr,"má obsah",PI*poloměr**2,"a obvod",2*PI*poloměr)


if poloměr<0:
    print("Strana čtverce nesmí být záporná")
    quit()
elif poloměr>10:
    print("Poloměr je moc velký")
    quit()
else:
    print("Kruh o poloměru",poloměr,"má obsah",PI*poloměr**2,"a obvod",2*PI*poloměr)

