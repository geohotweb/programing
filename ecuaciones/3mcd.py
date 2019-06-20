#This program calculate the maximmun common divisor of three numbers introducted by user.
num1 = int(input('Giv me the first number: '))
num2 = int(input('Giv me the second number: '))
num3 = int(input('Giv me the third number: '))

try:
	if num1 < num2 and num1 < num3:
		mcd = num1
	elif num2 < num1 and num2 < num3:
		mcd = num2
	else:
		mcd = num3

	while True:
		if num1%mcd==0 and num2%mcd==0 and num3%mcd==0:
			print('The mcd is',mcd)
			break

		else:
			mcd -= 1
except ZeroDivisionError:
		print('There was an error when dividing by 0')