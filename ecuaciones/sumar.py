#Este programa muestra la suma de los numero que forman el valor introducido en m.

m = int(input('Dame el primer numero: '))
n = int(input('Dame el segundo numero: '))
i = n
m2 = int(input('numero2: '))
while i < m2:
	i += n
	m += i
	print(m)
