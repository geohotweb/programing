print('Este programa recibe una cantidad de numeros los que el usuario introduzca' +' y muestra el mayor que ha introducido cuando el numero que recibe el programa es negativo')

num = int(input('Introduce un numero: '))
print(num)

mayor = num
while num > 0:
	num = int(input('Introduce otro numero: '))
	print(num)

print('El mayor numero que has introducido es',mayor)