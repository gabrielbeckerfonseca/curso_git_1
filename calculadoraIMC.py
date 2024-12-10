altura = float(input('Qual é a sua altura em cm? '))
peso = float(input('Qual é o seu peso em kg? '))

imc = peso / (altura/100) ** 2
if imc < 18.5:
	print('Abaixo do peso.')
elif imc >= 18.5 and imc < 24.9:
	print('Peso normal.')
elif imc >= 25 and imc <= 29.9:
	print('Sobrepeso.')
elif imc >= 30 and imc <= 39.9:
	print('Obesidade.')
else:
	print('Obesidade grave.')

print(imc)