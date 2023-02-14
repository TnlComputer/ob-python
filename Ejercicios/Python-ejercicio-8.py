# Se importa el módulo creado
import operaciones

a, b, c, d = (8, 5, 10, 2)

print("{} + {} = {}".format(a, b, operaciones.suma(a, b)))
print("{} - {} = {}".format(b, d, operaciones.resta(b, d)))
print("{} * {} = {}".format(b, b, operaciones.multiplicar(b, b)))
print("{} / {} = {}".format(a, c, operaciones.division(a, c)))
