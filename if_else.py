temperature = int(input('Qual é a temperatura da carne? '))

if temperature < 48:
	print('Cozinhar por mais alguns minutos.')
elif temperature >= 48 and temperature <= 53:
	print('O ponto de cozimento da carne é selada.')
elif temperature >= 54 and temperature <= 59:
	print('O ponto de cozimento da carne é ao ponto para mal passado.')
elif temperature >= 60 and temperature <= 64:
	print('O ponto de cozimento da carne é ao ponto.')
elif temperature >= 65 and temperature <= 70:
	print('O ponto de cozimento da carne é ao para bem passado.')
elif temperature >= 71 and temperature <= 80:
	print('O ponto de cozimento da carne é bem passada.')
else:
	print('A carne está queimada :(')