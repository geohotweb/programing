número = float(input('Dame un numero: '))

for n in range(2, 102):
	print('La raiz {0} n-esima de {1} es {2}'.format(n, número, número**(1/n)))