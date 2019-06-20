#Este programa muestra los numeros pares positivos de manera inversa

def par():
	for i in range(200+1, 0-2, -1):
		if i % 2 ==0:
			print(i)
par()