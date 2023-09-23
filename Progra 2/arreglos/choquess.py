def cantidad_registros(archivo):
    referencia_archivo = open(archivo)
    filas = len(referencia_archivo.readlines())
    linea = referencia_archivo.readline()
    campos = linea.split(",")
    columnas = len(campos[0])
    referencia_archivo.close()
    return filas,columnas

def leer(restitucion,masas,velocidades,distancia,archivo):
    referencia_archivo = open(archivo)
    i = 0
    for registro in referencia_archivo:
        campos = registro.split(",")
        restitucion[i] = float(campos[0])
        for j in range(len(masas[0])):
            masas[i][j] = float(campos[j +1])
            velocidades[i][j] = float(campos[j + 3])
        distancia[i] = float(campos[-1])
        i += 1
    referencia_archivo.close()

def velocidad_final(restitucion,masas,velocidades):
    matriz_velocidades = [[None] * (len(velocidades[0])) for i in range(len(velocidades))]
    for i in range(len(velocidades)):
        denominador = masas[i][0] + masas[i][1]
        matriz_velocidades[i][0] = ((masas[i][1] * velocidades[i][1] * (1 + restitucion[i])) + (velocidades[i][0] * (masas[i][0] - masas[i][1] * restitucion[i]))) / denominador
        matriz_velocidades[i][1] = ((masas[i][0] * velocidades[i][0] * (1 + restitucion[i])) + (velocidades[i][1] * (masas[i][1] - masas[i][0] * restitucion[i]))) / denominador
    return matriz_velocidades

def energia_perdida(masas,velocidades_iniciales,velocidades_finales):
    vector_perdida = [None for i in range(len(masas))]
    for i in range(len(masas)):
        energia_inicial = (masas[i][0] * velocidades_iniciales[i][0]**2 + masas[i][1] * velocidades_iniciales[i][1]**2) / 2
        energia_final = (masas[i][0] * velocidades_finales[i][0]**2 + masas[i][1] * velocidades_finales[i][1]**2) / 2
        vector_perdida[i] = energia_inicial - energia_final
    return vector_perdida

def tipo_choque(restitucion):
    vector_tipo = [None for i in range(len(restitucion))]
    for i in range(len(restitucion)):
        if (0 < restitucion[i]) and (restitucion[i] < 1):
            vector_tipo[i] = "Inelástico"
        elif restitucion[i] == 0:
            vector_tipo[i] = "Plástico"
        else:
            vector_tipo[i] = "Elástico"
    return vector_tipo

def direccion(v_finales):
    direcciones = [[None] * 2 for i in range(len(v_finales))]
    for i in range(len(v_finales)):
        for j in range(len(v_finales[0])):
            if v_finales[i][j] < 0:
                direcciones[i][j] = "Izquierda"
            else:
                direcciones[i][j] = "Derecha"
    return direcciones

def caida(distancia,v_finales):
    caidas = [[None] * 2 for i in range(len(v_finales))]
    for i in range(len(caidas)):
        for j in range(len(caidas[0])):
            caidas[i][j] = "No"
            if v_finales[i][j] > 0:
                distancia_final = v_finales[i][j] * 5
                if distancia_final > distancia[i]:
                    caidas[i][j] = "Si"
    return caidas


def mostrar(restitucion,masas,v_iniciales,v_finales,q_perdida,tipo,direcciones,caidas):
    print('  e         ma        mb         vao       vbo      vaf      vbf       Q        Tipo        DirecciónA     DirecciónB       A_Cayó    B_Cayó')
    for i in range(len(restitucion)):
        print(f'{restitucion[i]:5.2f}',end="  ")
        print(f'{masas[i][0]:8.2f}  {masas[i][1]:8.2f}' ,end="  ")
        print(f'{v_iniciales[i][0]:10.2f} {v_iniciales[i][1]:8.2f}',end="")
        print(f'{v_finales[i][0]:10.2f} {v_finales[i][1]:8.2f}',end="")
        print(f'{q_perdida[i]:10.2f}    {tipo[i]:10}   ',end="")
        print(f'{direcciones[i][0]:10}     {direcciones[i][1]:10}',end="        ")
        print(f'{caidas[i][0]:5}      {caidas[i][1]:5}')


archivito = "Choques.txt"
filas,columnas = cantidad_registros(archivito)
vector_restitucion = [None for i in range(filas)]
masas = [[None] * 2 for i in range(filas)]
velocidades = [[None] * 2 for i in range(filas)]
distancia = [None for i in range(filas)]
leer(vector_restitucion,masas,velocidades,distancia,archivito)
velocidades_finales = velocidad_final(vector_restitucion,masas,velocidades)
print(velocidades_finales)
print(distancia)
perdida = energia_perdida(masas,velocidades,velocidades_finales)
tipos = tipo_choque(vector_restitucion)
direcciones = direccion(velocidades_finales)
caidas = caida(distancia,velocidades_finales)
print(velocidades_finales)
print(distancia)
print(caidas)
mostrar(vector_restitucion,masas,velocidades,velocidades_finales,perdida,tipos,direcciones,caidas)
