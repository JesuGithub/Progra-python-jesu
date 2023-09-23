"""
Distancia entre dos numeros
"""
from math import *

def distancia(punto_x1, punto_x2, punto_y1, punto_y2 ):
    distancita = sqrt((punto_x2 - punto_x1)**2 + (punto_y2 - punto_y2)**2)
    return distancita

def pendiente(punto_x1, punto_x2, punto_y1, punto_y2):
    orientacion = ''
    if punto_x2 == punto_x1:
        return None
    else:
        pendienticota = (punto_y2 - punto_y1) // (punto_x2 - punto_x1)
        return pendienticota

valorcito_x1 = float(input('De el valor de x1: '))
valorcito_y1 = float(input('De el valor de y1: '))
valorcito_x2 = float(input('De el valor de x2: '))
valorcito_y2 = float(input('De el valor de y2: '))

print('Los puntos dados definen una recta: ')
print(f'Longitud: {distancia(valorcito_x1, valorcito_x2, valorcito_y1, valorcito_y2)}')
print(f'Pendiente: {pendiente(valorcito_x1, valorcito_x2, valorcito_y1, valorcito_y2)}')
pendientica = pendiente(valorcito_x1, valorcito_x2, valorcito_y1, valorcito_y2)
if pendientica == None:
    orientacion = 'Infinita'
elif pendientica < 0:
    orientacion = 'Descendente'
elif pendientica > 0:
    orientacion = 'Ascendente'
elif pendientica == 0:
    orientacion = 'Horizontal'
print(f'Orientacion: {orientacion}')