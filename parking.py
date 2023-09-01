from math import floor
total = float(0)
div = 0

day = int(input(f'Que día (numerico) usó el estacionamiento: '))
time = int(input(f'Tiempo de uso en minutos: '))

if day in [1,2,3]:

    if(time >= 5 and time <=60):
        total = 0

    else:
        div = time/60
        total = 2*div
        total = floor(total)

elif day in [4,5]:
    if(time >= 5 and time <=60):
        total = 0
    else:
        div = time/60
        total = 2.5*div

elif day in [6,7]:
    if(time >= 5 and time <=60):
        total = 0
    else:
        div = time/60
        total = 3*div
        total = floor(total)

print(f'Dia: {day}    Tiempo: {time} minutos')
print(f'Total a pagar: ${total}')