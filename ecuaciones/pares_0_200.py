#ESte programa muestra todos los numeros pares positivos comprendidos de entre 0 y 200

def par():
	for i in range(0, 201):
		if i % 2 ==0:
			print('el numero par que quieres es {0}'.format(i))
par()