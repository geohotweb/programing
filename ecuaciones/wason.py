#Programa que determina cual es el mayor de tres numeros.

primer_num = int(input('Dame el numero 1: '))
segundo_num = int(input('Dame el numero 2: '))
tercer_num = int(input('Dame el numero 3: '))

if primer_num > segundo_num:
	if primer_num > tercer_num:
		mayor=primer_num
	else:
		mayor=tercer_num
else:
	if segundo_num > tercer_num:
		mayor=segundo_num
	else:
		if tercer_num > primer_num:
			if tercer_num > segundo_num:
				mayor=tercer_num
print('El mayor es:',mayor)