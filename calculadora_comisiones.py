name = input("¿Nombre del vendedor? ")
ventas = float(input("¿Ventas realizadas? "))

def calcula_comision(name, ventas):
    comision = round(ventas*0.13, 2)
    print(f"El vendedor {name} ha vendidod {ventas} y recibe una comisión del 13% que supone un total de: {comision}")
    

calcula_comision(name, ventas)