#Este programa determina cual de las dos personas que introducen su edad es mayor

persona1 = int(input('Introduce la edad de la primera persona: '))
persona2 = int(input('Introduce la edad de la segunda persona: '))

if persona1 < persona2:
	print('La segunda persona es mayor que la primera persona')

elif persona1 == persona2:
	print('Las dos personas tienen la misma edad')
else:
	print('La primera persona es mayor que la segunda persona')
