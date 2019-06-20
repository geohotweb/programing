#Este programa determina cual es el numero maximo de cinco numeros dados

a = int(input('Dame el primer numero: '))
b = int(input('Dame el segundo numero: '))
c = int(input('Dame el tercer numero: '))
d = int(input('Dame el cuarto numero: '))
e = int(input('Dame el quinto numero: '))

candidato = a

if b > candidato:
	maximo = b
if c > candidato:
	maximo = c
if d > candidato:
	maximo = d
if e > candidato:
	maximo = e
print('El maximo es:',maximo)
