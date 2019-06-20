Limite = int(input('Giv me a number: '))

for number in range(2, Limite+1):
	I_think_hes_a_cousin = True
	for divider in range(2, number):
		if number%divider ==0:
			I_think_hes_a_cousin = False
			break
	if I_think_hes_a_cousin:
		print(number, end='')
print()