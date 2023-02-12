def bisiesto(fecha):
    resultado = fecha % 4
    if resultado == 0:
        print("La fecha ingresada es Bisiesto")
    else:
        print("La fecha ingresada no es Bisiesto")


print("ingrese el año a calcular")
fecha = int(input())
bisiesto(fecha)
