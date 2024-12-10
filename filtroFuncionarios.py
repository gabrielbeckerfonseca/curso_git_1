funcionarios = set(['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'])
turno_dia = set(['Ana', 'Marcos', 'Alice', 'Melissa'])
turno_noite = set(['Pedro', 'Sophia', 'Bruno'])
tem_carro = set(['Marcos', 'Alice', 'Bruno', 'Melissa'])


lista1 = turno_noite.intersection(tem_carro)
print(f'Os funcionários {lista1} trabalham a noite e tem carro.')
lista2 = turno_dia.intersection(tem_carro)
print(f'Os funcionários {lista2} trabalham de dia e tem carro.')
lista3 = funcionarios.difference(tem_carro)
print(f'Os funcionários {lista3} não tem carro.')
