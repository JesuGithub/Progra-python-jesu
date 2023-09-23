def maximo(numerador, denominador):
    if denominador > numerador:
        temporalsito = denominador
        denominador = numerador
        numerador = temporalsito
    while numerador % denominador != 0:
        temporalsito = denominador
        denominador = numerador % denominador
        numerador = temporalsito
    return denominador


def sumita(numerador1, numerador2, denominador1, denominador2):
    numeradorsisimo = ((numerador1 * denominador2) + (numerador2 * denominador1))
    denominadorsisimo = (denominador1 * denominador2)
    maximito = maximo(numeradorsisimo, denominadorsisimo)
    print(maximito)
    numeradorsisimo = numeradorsisimo / maximito
    denominadorsisimo = denominadorsisimo / maximito
    frasesita = (f' {numeradorsisimo} / {denominadorsisimo}')
    print(frasesita)

def restica(numerador1, numerador2, denominador1, denominador2):
    numeradorsisimo = ((numerador1 * denominador2) - (numerador2 * denominador1))
    denominadorsisimo = (denominador1 * denominador2)
    maximito = maximo(numeradorsisimo, denominadorsisimo)
    numeradorsisimo = numeradorsisimo / maximito
    denominadorsisimo = denominadorsisimo / maximito

def multiplicacionsota(numerador1, numerador2, denominador1, denominador2):
    numeradorsisimo = (numerador1 * numerador2)
    denominadorsisimo = (denominador1 * denominador2)
    maximito = maximo(numeradorsisimo, denominadorsisimo)
    numeradorsisimo = numeradorsisimo / maximito
    denominadorsisimo = denominadorsisimo / maximito

def divisionsota(numerador1, numerador2, denominador1, denominador2):
    numeradorsisimo = (numerador1 * denominador2)
    denominadorsisimo = (numerador2 * denominador1)
    maximito = maximo(numeradorsisimo, denominadorsisimo)
    numeradorsisimo = numeradorsisimo / maximito
    denominadorsisimo = denominadorsisimo / maximito

def menusito():
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
        opcion = int(input('Seleccione una opción: '))
        listica = {1,2,3,4}
        if opcion in listica:
            numerador1 = int(input('Diga el primer numerador: '))
            denominador1 = int(input('Diga el primer denominador: '))
            numerador2 = int(input('Diga el segundo numerador: '))
            denominador2 = int(input('Diga el segundo denominador: '))


sumita(1,2,3,4)
