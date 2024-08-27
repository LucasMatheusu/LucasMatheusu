from math import hypot
cat = float(input("Comprimento do  cateto"))
ca = float(input("comprimento do cateto  adja"))
h1 = hypot(cat, ca)
print("A hipotenusa vai ser {:.2f}".format(h1))
