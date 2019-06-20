def mcd(a, b):
	resto = 0

	while a > 0:
		resto = a
		a = a%b
		b = resto
	return b

num1 = int(input('Giv me the first number: '))
num2 = int(input('Giv me the second number: '))

print('The maximum common divider of',num1,'and',num2,'is',mcd(num1,num2))