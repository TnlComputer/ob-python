import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 19:
    print("Tenes que salir de trabajar")
else:
    print("Quedan {} horas y {} minutos para finalizar tu horario laboral".format(
        18 - int(hora), 59-int(minutos)))
