nota = float(input('introduce la nota: '))

if nota < 5:
	print('Suspenso.')
elif nota >= 5 and nota <7:
	print('Aprobado.')
elif nota >= 7 and nota < 9:
	print('Notable.')
elif nota >= 9 and nota < 10:
	print('Sobresaliente.')
elif nota == 10:
	print('Matricula de Honor.')
