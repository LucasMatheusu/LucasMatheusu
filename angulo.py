from math import radians, sin, tan, cos
an = float(input('digite o angulo que voce deseja'))
seno = sin(radians(an))
print('O ãngulo de {} tem o SENO de {:.2f}'.format(an, seno))
tangente = tan(radians(an))
print("o angulo de {} tem a TANGENTE de {:.2f} ".format(an, tangente))
cosseno =cos(radians(an))
print("o angulo de {} tem o COSSENO de {:.2f}".format(an, cosseno))
