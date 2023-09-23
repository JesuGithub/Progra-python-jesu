def cantidadFilas(nombre_archivo):
    archivo = open(nombre_archivo)
    filas = len(archivo.readlines())
    archivo.close()
    return filas

def cantidadColumnas(nombre_archivo):
    archivo = open(nombre_archivo)
    archivo.seek(1)
    for registro in archivo:
        campo = registro.split(",")
    columnas = len(campo)
    archivo.close()
    return columnas

def leer(nombres,datos_bateos,ponches,nombre_archivo): # 1
    archivo = open(nombre_archivo)
    i = 0
    j = 0
    for registro in archivo:
        campo = registro.split(',')
        nombres[i] = campo[0]
        ponches[i] = int(campo[1])

        datos_bateos[i] = [int(dato) for dato in campo[2:]]
        i += 1
    archivo.close()

def promedio(datos_bateos,ponches): # 2
    vector_promedio = [None for i in range(len(datos_bateos))]
    for i in range(len(datos_bateos)):
        hits = 0
        for j in range(len(datos_bateos[0])):
            hits += int(datos_bateos[i][j])
        veces_bateos = hits + ponches[i]
        promedito = hits / veces_bateos
        vector_promedio[i] = promedito
        promedito = 0
    return vector_promedio

def embases(datos_bateos,ponches): # 3
    vector_embases = [None for i in range(len(datos_bateos))]
    for i in range(len(datos_bateos)):
        hits = 0
        for j in range(len(datos_bateos[0])):
            hits += int(datos_bateos[i][j])
        vector_embases[i] = hits
    return vector_embases

def mayor(nombres,promedio):
    promedio_mayor = 0
    for i in range(len(promedio)):
        if promedio[i] > promedio_mayor:
            promedio_mayor = promedio[i]
            nombre_mayor = nombres[i]
    return nombre_mayor

def mostrar(nombres,datos_bateos,promedio,ponches,embases):
    print('NOMBRE           PONCHE  SENCILLOS  DOBLES  TRIPLES  HOMERUN  PROMEDIO  SE ENBASÓ')
    promedio_mayor = 0
    contador = 0
    contador_sencillos = 0
    contador_hits = 0
    nombre_mayor2 = ""
    for i in range(len(datos_bateos)):
        print(f'{nombres[i]:12}    {ponches[i]:5}',end="    ")
        for j in range(len(datos_bateos[0])):
            print(f'{datos_bateos[i][j]:5}',end="    ")
        print(f'  {promedio[i]:5.3f}      {embases[i]:5}')

        if promedio[i] > promedio_mayor:
            promedio_mayor = promedio[i]
            nombre_mayor = nombres[i]
        elif promedio[i] == promedio_mayor:
            nombre_mayor2 = nombres[i]

        if promedio[i] > 0.300:
            contador += 1

        contador_sencillos += datos_bateos[i][0]
        contador_hits += embases[i]

    porcentaje_sencillos = (contador_sencillos * 100) / contador_hits
    porcentaje = (contador * 100) / len(promedio)
    print()
    print(f'Bateador con mayor promedio: {nombre_mayor}')
    if nombre_mayor2 == "":
        print('No hubo otro bateador con el mayor promedio')
    else:
        print(f'El ultimo bateador con mayor promedio fue: {nombre_mayor2}')
    print(f'Porcentaje de bateadores con mas de 0.300 de promedio: {porcentaje:.2f}')
    print(f'Porcentaje de secillos bateados: {porcentaje_sencillos:.2f}')



archivito = "Rendimiento.txt"
filas = cantidadFilas(archivito)
columnas = cantidadColumnas(archivito) - 2
vector_nombres = [None for i in range(filas)]
vector_embasado = [None for i in range(filas)]
vector_ponches = [None for i in range(filas)]
matriz_hits = [[None] * columnas for i in range(filas)]
leer(vector_nombres,matriz_hits,vector_ponches,archivito)
print(columnas)
print(vector_nombres)
print(vector_ponches)
print(matriz_hits)
vector_promedio = promedio(matriz_hits,vector_ponches)
vector_embases = embases(matriz_hits,vector_ponches)
print(vector_promedio)
print(embases(matriz_hits,vector_ponches))
mostrar(vector_nombres,matriz_hits,vector_promedio,vector_ponches,vector_embases)

# Abre el archivo en modo lectura
# with open('Rendimiento.txt', 'r') as archivo:
#     # Itera a través de cada línea en el archivo
#     for linea in archivo:
#         # Divide la línea en partes usando la coma como separador
#         partes = linea.split(',')
#
#         # Comprueba si hay al menos tres partes después de dividir (índice 2 tiene el tercer elemento)
#         if len(partes) > 2:
#             # Itera a través de las partes a partir de la tercera (índice 2)
#             for dato in partes[2:]:
#                 # Imprime cada dato después de la segunda coma
#                 print(dato.strip(), end=" ")
#             print()# strip() elimina espacios en blanco alrededor
# print(promedio(matriz_hits))