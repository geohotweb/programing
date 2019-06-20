dinero = int(input("Dame el valor del dinero: "))
lista = [500, 200, 100, 50, 20, 10, 5, 2, 1]

for i in lista:
    queda = dinero // i
    dinero = dinero % i
    if  queda > 0:
        print("Le queda ",queda," billete",if i > 2 else,"monedas",if queda >1 else i)