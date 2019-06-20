#Este complicadisimo programa determina cual de los ultimos cuatro numeros dados es el mas cercano al primero.

x1=int(input('Dame el numero uno: '))
x2=int(input('Dame el nunero dos: '))
x3=int(input('Dame el numero tres: '))
x4=int(input('Dame el numero cuatro: '))
x5=int(input('Dame el numero cinco: '))

a=abs(x1-x2)
b=abs(x1-x3)
c=abs(x1-x4)
d=abs(x1-x5)

result=a<b<c<d
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x2))

result=a<b<d<c
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x2))

result=a<c<b<d
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x2))

result=a<c<d<b
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x2))

result=a<d<c<b
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x2))

result=a<d<b<d
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x2))

result=b<a<c<d
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x3))

result=b<a<d<c
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x3))

result=b<c<a<d
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x3))

result=b<c<d<a
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x3))

result=b<d<c<d
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x3))

result=b<d<d<c
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x3))

result=c<a<b<d
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x4))

result=c<a<d<b
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x4))

result=c<b<a<d
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x4))

result=c<b<d<a
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x4))

result=c<d<a<b
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x4))

result=c<d<b<a
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x4))

result=d<a<b<c
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x5))

result=d<a<c<b
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x5))

result=d<b<c<a
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x5))

result=d<b<a<c
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x5))

result=d<c<a<b
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x5))

result=d<c<b<a
if result == True:
	print('El numero mas proximo a {0} es {1}'.format(x1,x5))