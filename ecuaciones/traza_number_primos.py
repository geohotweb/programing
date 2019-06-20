#This program determine if a number introducted is cousin or not.
number = int(input('Giv me a number: '))

if number > 1:
	I_think_hes_cousin = True
	divider = 2
	while divider < number and I_think_hes_cousin:
		if number % divider == 0:
			I_think_hes_cousin = False
		divider += 1

else:
	I_think_hes_cousin = False

if I_think_hes_cousin:
	print('The number {0} is cousin.'.format(number))
else:
	print('The number {0} is not a cousin.'.format(number))
	