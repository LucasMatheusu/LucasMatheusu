from random import shuffle
n1 = str(input('primeiro aluno'))
n2 = str(input('terceiro aluno'))
n3 = str(input("segundo aluno"))
lista = [n1, n2, n3]
shuffle(lista)
print('o aluno sorteado foi ')
print(lista)
