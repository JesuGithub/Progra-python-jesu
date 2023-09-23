"""
Super programa pro Bv
Jesús Araujo
"""
def maximito(numerador, denominador):
    """

    :param numerador: Numerador de la operación de fracciones
    :param denominador: Denominador de la operación de fracciones
    :return: EL común denominador entre numerador y denominador
    """
    if denominador > numerador:
        temporal = denominador
        denominador = numerador
        numerador = temporal
    while numerador % denominador != 0:
        temporal = denominador
        denominador = numerador % denominador
        numerador = temporal
    return denominador

# Suma de Fracciones
def sumita(numerador1, numerador2, denominador1, denominador2):
    """

    :param numerador1: Numerador de la fracción 1
    :param numerador2: Numerador de la fracción 2
    :param denominador1: Denominador de la fracción 1
    :param denominador2: Denominador de la fracción 2
    :return: El numerador y el denominador simplificados de la suma de fracciones
    """
    numerador = (numerador1 * denominador2) + (denominador1 * numerador2)
    denominador = denominador1 * denominador2
    maximote = maximito(numerador, denominador)
    numerador = numerador // maximote
    denominador = denominador // maximote
    return numerador, denominador

# Multiplicación de Fracciones
def multiplicacionsita(numerador1, numerador2, denominador1, denominador2):
    """

    :param numerador1: Numerador de la fracción 1
    :param numerador2: Numerador de la fracción 2
    :param denominador1: Denominador de la fracción 1
    :param denominador2: Denominador de la fracción 2
    :return: El numerador y el denominador simplificados de la multiplicación de fracciones
    """
    numerador = (numerador1 * numerador2)
    denominador = denominador1 * denominador2
    maximote = maximito(numerador, denominador)
    numerador = numerador // maximote
    denominador = denominador // maximote
    return numerador, denominador

# División de Fracciones
def divisionsita(numerador1, numerador2, denominador1, denominador2):
    """

    :param numerador1: Numerador de la fracción 1
    :param numerador2: Numerador de la fracción 2
    :param denominador1: Denominador de la fracción 1
    :param denominador2: Denominador de la fracción 2
    :return: El numerador y el denominador simplificados de la división de fracciones
    """
    numerador = (numerador1 * denominador2)
    denominador = denominador1 * numerador2
    maximote = maximito(numerador, denominador)
    numerador = numerador // maximote
    denominador = denominador // maximote
    return numerador, denominador

# Menu de opciones
def superProFracciones():
    while True:
        print('''
        Bienvenido!!!!
        Elija una opción:
        1) Sumar Fracciones
        2) Restar Fracciones
        3) Multiplicar Fracciones
        4) Dividir Fracciones
        Terminar con otro valor
        ''')
        opcion = int(input('Seleccione su opción de trabajo: '))

        if 1 <= opcion <= 4:
            print("\nFracción 1:")
            numerador1 = int(input('Diga el primer numerador: '))
            denominador1 = int(input('Diga el primer denominador: '))
            print("Fracción 2:")
            numerador2 = int(input('Diga el segundo numerador: '))
            denominador2 = int(input('Diga el segundo denominador: '))
            if opcion == 1:
                numerador, denominador = sumita(numerador1, numerador2, denominador1, denominador2)
                nombresito = 'Suma'
                operacion = 'más'
            elif opcion == 2:
                numerador, denominador = sumita(numerador1, (-1 * numerador2), denominador1, denominador2)
                nombresito = 'resta'
                operacion  = 'menos'
            elif opcion == 3:
                numerador, denominador = multiplicacionsita(numerador1, numerador2, denominador1, denominador2)
                nombresito = 'multiplicación'
                operacion = 'por'
            elif opcion == 4:
                numerador, denominador = divisionsita(numerador1, numerador2, denominador1, denominador2)
                nombresito = 'división'
                operacion = 'entre'

            print('')
            print(f'El resultado de la {nombresito} de fracciones de {numerador1}/{denominador1} '
                  f'{operacion} {numerador2}/{denominador2} es: '
                  f'{numerador} / {denominador}')
            superProFracciones()
        else:
            break

superProFracciones()