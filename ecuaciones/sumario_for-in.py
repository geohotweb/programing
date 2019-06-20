#Este programa pide dos valores para poder calcular y imprimir por pantalla el valor de m.

n = int(input('give me the value n: '))
m = int(input('give me the value m: '))
i = n

for i in range(m):
	i += n
	m += i
print(m)