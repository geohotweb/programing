#Este programa determina cual de los dos ultimos numeros dados es el cuadrado del primer numero dado.

def mostrar():
	num1 = int(input('Ingrese el primer numero: '))
	num2 = int(input('Ingrese el segundo numero: '))
	num0 = num1**2
	if num0 == num1**2 and num2==num1**2:
		print('El segundo numero es el cuadrado del primero')

	else num2 >num0:
		print('El segundo numero es mayor que el cuadrado del primero')
	
mostrar()
