"""
Funcion para saber si un numero es perfecto
"""

# Declaracion de la funcion
def numero_perfecto(numerito):
    valores = 0
    for i in range(1, numerito):
        if (numerito % i) == 0:
            valores += i
    return valores == numerito

if numero_perfecto(8128):
    print('perfecto jiji')
else:
    print('NO')

def impresion_perfectos():
    for i in range(1, 10001):
        if numero_perfecto(i):
            print(i)

impresion_perfectos()