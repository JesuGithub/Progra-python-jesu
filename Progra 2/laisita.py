from math import sin, cos, tan, log, sqrt


def calculator():

    def function():
        """
        Esta funcion calcula el valor del seno, coseno, tangente, logaritmo

        :return: valor de la funcion utilizada por el usuario
        """
        f = {'s': sin, 'c': cos, 't': tan, 'l': log}

        print("Para seleccionar una funcion ingrese: ")
        print("seno: 's', coseno: 'c', tangente: 't', logaritmo: 'l'")
        functions = input("Que funcion desea utilizar?: ")
        number = int(input("Put the number you want apply on the function: "))

        results = f[functions](number)
        return ("resultado obtenido de la funcion aplicada: ", results)

    def plus():
        """
        Suma o resta dos o mas valores
        :return: valor obtenido de la suma
        """
        amount_number = int(input("how much numbers you gonna sum?: "))
        numbers = []

        for n in range(1, amount_number + 1):
            number = float(input("Ingrese el valor a sumar: "))
            numbers = numbers.append(number)

        return (f"la suma de los numeros es:{sum(numbers)}")

    def subtration():
        """
        Resta dos o mas valores
        :return: valor obtenido de la resta
        """
        amount_number = int(input("how much numbers you gonna sum?: "))
        numbers = 0

        for n in range(1, amount_number + 1):
            number = float(input("Ingrese el valor a restar: "))
            numbers -= number

        return (f"la resta de los numeros es:{numbers}")

    def raiz():
        """
        Saca la raiz cuadrada de un valor

        :return: valor obtenido de la raiz cuadrada de el valor introducido
        """
        number = float(input("Ingrese el numero que desea conocer su raiz: "))

        return (f"la raiz cuadrada de {number} es: {sqrt(number)}")
    global aqui
    print("Bienvenid@", "\nEn este programa podras ejecutar calculos a travez de nuestra calculadora interactiva")
    print("Opciones disponibles a trabajar:")
    print("Funciones(sin,cos,tag,log) --> 1", "\nSuma --> 2", "\nResta --> 3", "\nRaiz cuadrada --> 4")
    opcion = input("ingrese el numero de la opcion que desea trabajar: ")

    if opcion == "1":
        aqui = function()
    elif opcion == "2":
        aqui = plus()
    elif opcion == "3":
        aqui = subtration()
    elif opcion == "4":
        aqui = raiz()
    return aqui



print(calculator())