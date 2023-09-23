import math

# Pedir al usuario que ingrese las coordenadas de los tres puntos
x1, y1 = map(float, input("Ingrese las coordenadas del primer punto (x1 y1): ").split())
x2, y2 = map(float, input("Ingrese las coordenadas del segundo punto (x2 y2): ").split())
x3, y3 = map(float, input("Ingrese las coordenadas del tercer punto (x3 y3): ").split())

# Verificar que los tres puntos no estén alineados
if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
    # Calcular las distancias entre los puntos
    d1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    d2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    d3 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

    # Verificar si se cumple el teorema de Pitágoras para un triángulo rectángulo
    if d1 ** 2 + d2 ** 2 == d3 ** 2 or d1 ** 2 + d3 ** 2 == d2 ** 2 or d2 ** 2 + d3 ** 2 == d1 ** 2:
        print("Los puntos forman un triángulo rectángulo.")
    # Verificar si dos de las distancias son iguales para un triángulo isósceles
    elif d1 == d2 or d1 == d3 or d2 == d3:
        print("Los puntos forman un triángulo isósceles.")
    # Si no se cumple ninguna de las condiciones anteriores, se tiene un triángulo escaleno
    else:
        print("Los puntos forman un triángulo escaleno.")
else:
    print("Los puntos están alineados y no forman un triángulo.")