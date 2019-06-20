#This program determines if a number is cousin or not
number = int(input('Dame un numero para determinar si es primo: '))

if number > 1:
	I_think_hes_a_cousin = True
	for divider in range(2, number):
		if number % divider == 0:
			I_think_hes_a_cousin = False

else:
	I_think_hes_a_cousin = False

if I_think_hes_a_cousin:
	print('The number {0} is cousin.'.format(number))
else:
	print('The number {0} is not a cousin.'.format(number))
	