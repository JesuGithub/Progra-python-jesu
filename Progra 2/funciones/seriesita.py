from math import sqrt

def distancia(puntox1, puntox2, puntoy1, puntoy2):
    distancita = sqrt((puntox2 - puntox1)**2 + (puntoy2 - puntoy1)**2)
    return distancita

def area(distancia1, distancia2, distancia3):
    semiperimetro = (distancia1 + distancia2 + distancia3) / 2
    area = sqrt(semiperimetro * (semiperimetro - distancia1) * (semiperimetro - distancia2) * (semiperimetro - distancia3))
    return area

def identificacion_triangulo(distancia1, distancia2, distancia3):
    if distancia1 == distancia2 == distancia3:
        tipo_triangulo = 'Equilátero'
    elif (distancia1 == distancia2) or (distancia1 == distancia3) or (distancia2 == distancia3):
        tipo_triangulo = 'Isósceles'
    elif (distancia1 != distancia2) or (distancia1 != distancia3) or (distancia2 != distancia3):
        tipo_triangulo = 'Escaleno'
    return tipo_triangulo

def verificacion_triangulo(distancia1, distancia2, distancia3):
    if distancia1 < (distancia2 + distancia3):
        return True
    elif distancia2 < (distancia1 + distancia3):
        return True
    elif distancia3 < (distancia1 + distancia2):
        return True
    else:
        return False

def verificacion_triangulo_tolerancia(distancia1, distancia2, distancia3):
    tolerancia = 0.001
    if abs(distancia1 - distancia2) < tolerancia:
        return True
    elif abs(distancia1 - distancia3) < tolerancia:
        return True
    elif abs(distancia2 - distancia3) < tolerancia:
        return True
    else:
        return False

def menu():
    respuesta = 'S'
    while (respuesta.upper() == 'S') :
        print('Punto 1')
        puntox1 = float(input('De el punto x1: '))
        puntoy1 = float(input('De el punto y1: '))
        print('Punto 2')
        puntox2 = float(input('De el punto x2: '))
        puntoy2 = float(input('De el punto y2: '))
        print('Punto 3')
        puntox3 = float(input('De el punto x3: '))
        puntoy3 = float(input('De el punto y3: '))

        distancia12 = distancia(puntox1, puntox2, puntoy1, puntoy2)
        distancia23 = distancia(puntox2, puntox3, puntoy2, puntoy3)
        distancia31 = distancia(puntox3, puntox1, puntoy3, puntoy1)

        if verificacion_triangulo_tolerancia(distancia12, distancia23, distancia31):
            tipo_triangulo = identificacion_triangulo(distancia12, distancia23, distancia31)
            area_triangulo = area(distancia12, distancia23, distancia31)

            print(f'\nEl triángulo es {tipo_triangulo} y su area: {area_triangulo}')
        else:
            print('Los puntos no forman un triángulo')
        respuesta = input('Continuar? S: Si  N: No -->')

menu()





