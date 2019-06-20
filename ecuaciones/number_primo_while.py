#This program determine if a number is cousin or not.
number = int(input('Giv me a number: '))

if number > 1:
	I_think_hes_a_cousin = True
	divider = 2
	while divider < number:
		if number % divider ==0:
			I_think_hes_a_cousin = False
		divider += 1

else:
	I_think_hes_a_cousin = False

if I_think_hes_a_cousin:
	print('The numer {0} in cousin.'.format(number))
else:
	print('The number is not a cousin.'.format(number))
	