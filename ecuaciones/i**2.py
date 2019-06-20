#Este programa imprime el valor de i al cuadrado multiplicandolo a su vez por n para asi poder mandar el resultado que se espera
n = int(input('Dame el valor de n: '))
m = int(input('Dame el valor de m: '))
i = n

for i in range(m):
	i += n
	m += i**2
print('El resultado esperado es {0}'.format(m))
