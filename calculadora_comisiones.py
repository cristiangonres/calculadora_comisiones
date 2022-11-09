name = input("¿Nombre del vendedor? ")
sales = float(input("¿Ventas realizadas? "))

def calcula_comision(name, sales):
    comision = round(sales*0.13, 2)
    print(f"El vendedor {name} ha vendidod {sales}€ y recibe una comisión del 13% que supone un total de: {comision}€")
    

calcula_comision(name, sales)