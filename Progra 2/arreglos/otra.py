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


def leer(nombresito_archivo,nombres,notas,promedio):
    archivo = open(nombresito_archivo)
    columnas = len(notas[0])
    i = 0
    for registro in archivo:
        campos = registro.split(',')
        nombres[i] = campos[0]
        suma = 0
        for j in range(columnas):
            notas[i][j] = float(campos[j+1])
            suma += float(campos[j+1])
        promediosito = suma / len(notas[0])
        promedio[i] = promediosito
        i += 1
    archivo.close()

def ordenanza(nombres,promedio):
    for i in range(len(promedio)):
        for j in range(i+1,len(promedio)):
            if promedio[i] < promedio[j]:
                temporal = promedio[i]
                promedio[i] = promedio[j]
                promedio[j] = temporal

                temporal = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = temporal


def impresion(nombres,notas,promedio):
    print('POSICIÓN        NOMBRE                       NOTAS                  PROMEDIO')
    filas = len(notas)
    columnas = len(notas[0])
    for i in range(filas):
        print(f'{i+1:2}.             {nombres[i]:14}', end="")
        for j in range(columnas):
            print(f'{notas[i][j]:10.2f}',end="")
        print(f'    {promedio[i]:10.2f}')


archivito = "Colegio.txt"
filas = cantFilas(archivito)
columnas = cantColumnas(archivito) - 1
matriz = [[None] * columnas for i in range(filas)]
nombres_vector = [None for i in range(filas)]
promedio_vector = [None for i in range(filas)]
leer(archivito,nombres_vector,matriz,promedio_vector)
ordenanza(nombres_vector, promedio_vector)
impresion(nombres_vector, matriz,promedio_vector)


