#Este progama calcula el desglose de una cantidad introduccida por el usuario.

n = int(input('Dame la cantidad: '))

#Introducimos los billetes y monedas.
a = 500
b = 200
c = 100
d = 50
e = 20
f = 10
g = 5
h = 2
i = 1

desgloce1 = n//a
desgloce2 = n//b
desgloce3 = n//c
desgloce4 = n//d
desgloce5 = n//e
desgloce6 = n//f
desgloce7 = n//g
desgloce8 = n//h
desgloce9 = n//i

if desgloce1 > 0:
	print(desgloce1,'billetes de',a)

if desgloce2 > 0:
	print(desgloce2,'billetes de',b)

if desgloce3 > 0:
	print(desgloce3,'billetes de',c)

if desgloce4 > 0:
	print(desgloce4,'billetes de',d)

if desgloce5 > 0:
	print(desgloce5,'billetes de',e)

if desgloce6 > 0:
	print(desgloce6,'billetes de',f)

if desgloce7 > 0:
	print(desgloce7,'billetes de',g)

if desgloce8 > 0:
	print(desgloce8,'monedas de',h)

if desgloce9 > 0:
	print(desgloce9,'monedas de',i)
	