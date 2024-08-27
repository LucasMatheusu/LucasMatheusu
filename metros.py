medida = float(input('Uma distancia em metros'))
cm = medida * 100
mm = medida * 1000
km = medida * 10000
dm = medida * 100000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm e {}km e {}dm '.format(medida, cm  , mm, km, dm))
