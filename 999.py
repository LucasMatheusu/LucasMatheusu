nm = cont = soma = 0
nm = int(input('Digite um número [999 para parar]'))
while nm != 999:
    soma += nm
    cont += 1
    nm = int(input('Digite um número [999 para parar]'))
print('acabou, voce digitou {} numeros, a soma foi {}'.format(cont, soma))