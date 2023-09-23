def cantFilas(nombresito_archivo):
    archivo = open(nombresito_archivo)
    filas = len(archivo.readlines())
    archivo.close()
    return filas

def cantColumnas(nombresito_archivo):
    archivo = open(nombresito_archivo)
    archivo.seek(1)
    for registro in archivo:
        columnas = registro.split(",")
    columna_retornable = len(columnas)
    archivo.close()
    return columna_retornable

def get_archivo(nombresito_archivo):
    archivo = open(nombresito_archivo,"r")
    return archivo

def leer(referencia_archivo,maximos_minimos,nombres,porcentajes):
    linea = referencia_archivo.readline()
    campos_minimos = linea.split(",")

    # Ingresando al vector de minimos y maximos
    for i in range(len(maximos_minimos)):
        maximos_minimos[i] = float(campos_minimos[i])

    i = 0
    for registro in referencia_archivo:
        campo = registro.split(',')
        nombres[i] = int(campo[0])
        for j in range(len(porcentajes[0])):
            porcentajes[i][j] = float(campo[j+1])
        i += 1

def promedio(porcentajes):
    promedio = [[None] * 2 for i in range(len(porcentajes))]
    for i in range(len(porcentajes)):
        sumaMG = 0
        sumaC = 0
        for j in range(len(porcentajes[0])):
            if j < 3:
                sumaC += porcentajes[i][j]
            else:
                sumaMG += porcentajes[i][j]
            promedio[i][0] = sumaC/3
            promedio[i][1] = sumaMG/3
    return promedio

def status(maximos_minimos,promedios):
    aprobados = [None for i in range(len(promedios))]
    for i in range(len(promedios)):
            if (maximos_minimos[0] < promedios[i][0] and promedios[i][0] < maximos_minimos[1]) and (maximos_minimos[2] < promedios[i][1] and promedios[i][1] < maximos_minimos[3]):
                aprobados[i] = "APROBADO"
            else:
                aprobados[i] = "REPROBADO"
    return aprobados

def mostrar(lotes,promedios,estatus):
    print('LOTE     PROMEDIO C%  PROMEDIO MG%     ESTATUS')
    contador = 0
    for i in range(len(promedios)):
        print(f'{lotes[i]} ',end="     ")
        for j in range(len(promedios[0])):
            print(f'{promedios[i][j]:.2f}', end="         ")
        print(estatus[i])
        if (estatus[i] == "REPROBADO"):
            contador += 1
    if contador > 0:
        porcentaje = (contador / len(lotes)) * (100)
        print(f'\nPorcentaje de lotes rechazados: {porcentaje}')
    else:
        print('No se rechazó ningún lote')
    coste_rechazos = contador * 2500
    print(f'Monto de las perdidas de lotes rechazados: {coste_rechazos} $')

filas = cantFilas("Lotes.txt") - 1
columnas = cantColumnas("Lotes.txt") - 1
archivo = get_archivo("Lotes.txt")
maximos_minimos = [None for i in range(4)]
nombres = [None for i in range(filas)]
print(nombres)
matriz_porcentaje = [[None] * columnas for i in range(filas)]
leer(archivo,maximos_minimos,nombres,matriz_porcentaje)
promedios = promedio(matriz_porcentaje)
aprobadotes = status(maximos_minimos, promedios)
mostrar(nombres,promedios,aprobadotes)
print(maximos_minimos)
print(promedios)
