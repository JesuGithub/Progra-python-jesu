def cantFilas(nombresito_archivo):
    archivo = open(nombresito_archivo)
    filas = len(archivo.readlines())
    archivo.close()
    return filas

def cantColumnas(nombresito_archivo):
    archivo = open(nombresito_archivo)
    for registro in archivo:
        columnas = registro.split(",")
    columna_retornable = len(columnas)
    archivo.close()
    return columna_retornable

def leer(nombres,horas,archivo): # 1
    archivito = open(archivo,"r")
    i = 0
    for info in archivito:
        campo = info.split(",")
        nombres[i] = campo[0]

        for j in range(len(horas[0])):
            horas[i][j] = int(campo[j + 1])
        i += 1
    archivito.close()

def tiempito(matriz_tiempo): # 2
    matriz_tiempo_total = [[None] * 2 for i in range(len(matriz_tiempo))]
    for i in range(len(matriz_tiempo)):
        for j in range(len(matriz_tiempo[0])):
            tiempo_inicio = (matriz_tiempo[i][0] * 60) + matriz_tiempo[i][1]
            tiempo_final = (matriz_tiempo[i][2] * 60) + matriz_tiempo[i][3]

            tiempo_total = tiempo_final - tiempo_inicio

            horas = tiempo_total//60
            minutos = tiempo_total%60
        matriz_tiempo_total[i][0] = horas
        matriz_tiempo_total[i][1] = minutos
    return matriz_tiempo_total

def costo(tiempo_total): # 3
    matriz_costo = [None for i in range(len(tiempo_total))]
    for i in range(len(tiempo_total)):
        costico = (tiempo_total[i][0] // 1 ) * 3 + ((tiempo_total[i][1] // 15) + 1) * 0.75
        matriz_costo[i] = costico
    return matriz_costo

def mostrar(nombres,tiempo_total,costos): # 4
    print('MAQUINA    TIEMPO ALQUILAR     MONTO A PAGAR')
    for i in range(len(nombres)):
        print(f'{nombres[i]:10}',end="       ")
        print(f'{tiempo_total[i][0]:02d}:{tiempo_total[i][1]:02d}', end="             ")
        print(f'{costos[i]:2.2f}')


filas = cantFilas("Alquiler.txt")
columnas = cantColumnas("Alquiler.txt") - 1

vector_nombres = [None for i in range(filas)]
matriz_horas = [[None] * columnas for i in range(filas)]
archivo = "Alquiler.txt"
leer(vector_nombres,matriz_horas,archivo)
tiempo_total = tiempito(matriz_horas)
matriz_costo = costo(tiempo_total)
mostrar(vector_nombres, tiempo_total, matriz_costo)
