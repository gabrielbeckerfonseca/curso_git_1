rendimento = int(input('Qual o rendimento da tinta por lata? '))
altura = int(input('Qual a altura da parede? '))
largura = int(input('Qual a largura da parede? '))

def resultado():
	area = altura * largura
	total = area / rendimento	
	print(f'Você necessista de {total} latas de tinta para pintar sua parede.')

resultado()