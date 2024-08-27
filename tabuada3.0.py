while True:
     n = int(input('digite um valor da tabuada'))
     if n < 0:
          break
     for c in range(1, 11):
      print(f'{n} x {c} = {n*c}')
print('acabou')

