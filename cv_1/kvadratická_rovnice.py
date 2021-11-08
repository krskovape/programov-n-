from math import sqrt

a = 3
b = 4
c = 1

d = b**2-4*a*c

if d<0:
    print("Rovnice nemá reálné řešení")
elif d==0:
    print("Rovnice má dvonásobný kořen x=",(-b+sqrt(d))/2*a)
else:
    print("Rovnice má kořeny x1=",(-b+sqrt(d))/2*a,"a x2=",(-b-sqrt(d))/2*a)