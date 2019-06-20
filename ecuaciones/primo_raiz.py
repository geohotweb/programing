from math import sqrt

número = int(input('Giv me a number: '))

for divisor in range(2, número):
	div = sqrt(número)
	print('{0} entre {1}'.format(número, divisor), end='')
	print(' es {0} con resto {1}'.format(número//divisor, número % divisor))
	if div==0 or número==85:
		print('Its not cousin.')
		break
	else:
		if div>0:
			print('Is cousin.')
			break
