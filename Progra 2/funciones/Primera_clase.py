import random

def juego_epico(numero, numerito_random):
    if numero > numerito_random:
        print('El numero misterioso es menor')
        otro_numero = int(input('Digame otro numero: '))
        juego_epico(otro_numero, numerito_random)
    elif numero < numerito_random:
        print('El numero misterioso es mayor')
        otro_numero = int(input('Digame otro numero: '))
        juego_epico(otro_numero, numerito_random)
    else:
        print('HAS GANADO!!!!!!!!!!!!!!!!!!!!')
        return True

# numerosote = int(input('Digame un numero: '))
# numero_random = random.randint(1,100)
# juego_epico(numerosote, numero_random)

# Función para separar palabras en letras

def separacion(palabra, separador):
    """

    :param palabra: Palabra la cual vamos a iterar y separar en palabras
    :param separador: El separador que usaremos para separar las letras de las palabras
    :return: Imprime la palabra separada por el separador
    """

    listica = list(palabra)
    if len(listica) > 80:
        print('Caracteres invalidos, debe ser menor a 80 caracteres')
        palabrota = input('Digame la nueva palabra a separar: ')
        separadorsote = input('Digame con que quiere separar la palabra: ')
        return separacion(palabrota, separadorsote)
    else:
        print(*listica, sep=separador)

separacion('Lai Chang', "!")

def centrador(palabra):
    print(f'{palabra:^160}')

centrador('Ale')
