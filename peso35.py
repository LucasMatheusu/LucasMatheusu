peso = float(input('Qual e o seu peso? (KG)'))
altura = float(input('Qual e a sua altura ? (m)'))
imc = peso / (altura ** 2)
print('O imc dessa pessoa e de {:.1f} '.format(imc))
if imc < 18.5:
    print('voce esta abaixo do peso normal ')
elif imc >= 18.5 and imc < 25:
    print('voce esta com o peso ideal')
elif 25 <= imc < 30:
    print('voce esta em sobrepeso')
elif 30 <= imc < 40:
    print('Cuidado, voce esta na obesidade')
elif imc >= 40:
    print("Voce tem obesidade morbida, cuidado!!")


