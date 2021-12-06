from pyproj import Transformer

#always_xy=True - první vždy délka a druhá šířka

wgs2jtsk = Transformer.from_crs(4326,5514,always_xy=True)
jtsk2wgs = Transformer.from_crs(5514,4326,always_xy=True)

out = wgs2jtsk.transform(15,50)

print(out)
print(jtsk2wgs.transform(*out))    #*out - vybere parametry z out a dosadí je na stejnou pozici