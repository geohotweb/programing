#Este programa determina cual es el capital, final durante n cantidad de años

def capital():
	c = int(input('Introduzca la cantidad: '))
	x = int(input('Introduzca el por ciento de interes: '))
	n = int(input('Introduce el numero de años: '))
	cap = c*(1+x/100)**n
	
	if c >= 0 and x >=0:
		print('El capital final es ',cap,'Euros, del',x,'porciento anual 				durante',n,'años')
	else:
		print('El numero del por cien anual es negativo por lo que no se 				puede obtener su resultado')
capital()
