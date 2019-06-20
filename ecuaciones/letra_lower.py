#Este programa vuelve a ejecutar el while mientras el texto introducido tiene alguna letra mayuscula

x = input('Introduce aqui el texto: ')

mayusculas = 'ABCDEFGHEJKLMNOPQRSTUVWXYZ'

while x != x.lower():
	x = input('Introduce aqui de nuevo el texto: ')
print('El texto introducido es:',x)
