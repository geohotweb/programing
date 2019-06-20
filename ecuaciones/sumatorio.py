m = int(input('Dame el primer numero: '))
n = int(input('Dame el segundo numero: '))
i = n
m2 = int(input('numero2: '))

if n > m2:
	print(n,'Tiene que se menor o igual que',m2)

while i < m2:
	i += n
	m += i
	print(m)
