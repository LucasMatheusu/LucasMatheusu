t = int(input('numero da tabuada voce quer?'))
for c in range(1, 16):
     print('{} x {} = \033[34m{} '.format(t, c, t*c))