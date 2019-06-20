#Este programa determina cual es el numero maximo de tres numeros dados

a = int(input('Dame el primer numero: '))
b = int(input('Dame el segundo numero: '))
c = int(input('Dame el tercer numero: '))

if a > b: 
	if a > c:
		maximo = a
	else:
		maximo = c
else:
	if b > c:
		maximo = b
	else:
		if c > a:
			if c > b:
				maximo = c
		else:
			print('Los numeros son iguales.')
print('el maximo es',maximo)
