#Este programa determina cual es las 5 palabra tiene el valor minimo de acuerdo con la tabla ascii
#siendo menor si alguna de las letras de una palabra introducida es mayusculas

pal1 = input('Dame la primera palabra: ')
pal2 = input('Dame la segunda palabra: ')
pal3 = input('Dame la tercera palabra: ')
pal4 = input('Dame la cuarta palabra: ')
pal5 = input('Dame la quinta palabra: ')

mayuscula = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
minuscula = 'abcdefghijklmnñopqrstuvwxyz'

mayuscula < minuscula

minimo = pal1

if minimo < pal2:
	if minimo < pal3:
		if minimo < pal4:
			if minimo < pal5:
				minimo = pal1
if pal2 < minimo:
	if pal2 < pal3:
		if pal2 < pal4:
			if pal2 < pal5:
				minimo = pal2
if pal3 < minimo:
	if pal3 < pal2:
		if pal3 < pal4:
			if pal3 < pal5:
				minimo = pal3
if pal4 < minimo:
	if pal4 < pal2:
		if pal4 < pal3:
			if pal4 < pal5:
				minimo = pal4
if pal5 < minimo:
	if pal5 < pal2:
		if pal5 < pal3:
			if pal5 < pal4:
				minimo = pal5
print('La menor de acuerdo con la tabla ASCII es:',minimo)
