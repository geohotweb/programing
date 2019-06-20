
c = int(input('Dame la capital inicial: '))
x = int(input('Dame el valor en porcentaje: '))
n = int(input('Dame la cantidad de años: '))
c_final = c*(1+x/100)**n
n_a = c_final-c/(1+x/100)*n


if x <=0:
	print('No se puede calcular el capital final si la tasa de interes es igual o menor a',int(0),'')
if c == c_final and c_final ==10000:
	print('Para obtener la cantidad de',c,'no hace falta esperar nada.')
else:
	print('Se tardo {0:.4f}'.format(n_a),'años para conseguir un capital final de ',int(c_final),'euros apartir de un capital inicial de',c,'euros')
