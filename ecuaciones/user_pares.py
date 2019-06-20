#Este programa muestra el los numeros pares positivos entre 2 y un numero cualquiera introducido por el usuario.

numero = int(input('Dame un numero: '))

for n in range(2, numero+1):
	if n % 2==0:
		print('Los numeros son {0}'.format(n))