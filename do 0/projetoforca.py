palavra = "python"
letras_usuarios = []
chances = 4
ganhou = False

while True:
    for letra in palavra:
        if letra.lower() in letras_usuarios:
            print(letra, end=" ")
        else:
            print('=', end=" ")
    print(f'voce tem {chances} chances')
    tentativa = input('Escolha uma letra para advinhar:')
    letras_usuarios.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuarios:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f'Parabens, voçê ganhou. A palavra era : {palavra}')
else:
    print(f"Voce perdeu. a palavra era {palavra}")