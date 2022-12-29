import datetime
import time
import os

while True:
    hora_actual = datetime.datetime.now()
    horas = hora_actual.hour
    minutos = hora_actual.minute
    segundos = hora_actual.second

    print(f"{horas:02}:{minutos:02}:{segundos:02}")

    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

