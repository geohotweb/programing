#Este programa al contrario del anterior dice que las palabras con letra minuscula no importa si esta organizada alfabeticamente, si es minuscula es menor que la misma con una letra mayuscula.

pal1 = input('Dame la primera palabra: ')
pal2 = input('Dame la segunda palabra: ')
pal3 = input('Dame la tercera palabra: ')
pal4 = input('Dame la cuarta palabra: ')
pal5 = input('Dame la quinta palabra: ')



minimo = pal1

if minimo < pal2:
	if minimo < pal3:
		if minimo < pal4:
			if minimo < pal5:
				minimo = pal1.lower()
if pal2 < minimo:
	if pal2 < pal3:
		if pal2 < pal4:
			if pal2 < pal5:
				minimo = pal2.lower()
if pal3 < minimo:
	if pal3 < pal2:
		if pal3 < pal4:
			if pal3 < pal5:
				minimo = pal3.lower()
if pal4 < minimo:
	if pal4 < pal2:
		if pal4 < pal3:
			if pal4 < pal5:
				minimo = pal4.lower()
if pal5 < minimo:
	if pal5 < pal2:
		if pal5 < pal3:
			if pal5 < pal4:
				minimo = pal5.lower()
print('La menor es:',minimo)
