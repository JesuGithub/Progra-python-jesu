def registro(arch):  # 1
    archivo = open(arch, "r")
    cantReg = len(archivo.readlines())
    archivo.close()
    return cantReg


def llenado(arch, tiempo):  # 2
    archivo = open(arch, "r")

    fila = len(tiempo)
    maquina = [None for i in range(fila)]
    f = 0
    for info in archivo:
        campo = info.split(",")
        maquina[f] = campo[0]

        for c in range(4):
            tiempo[f][c] = int(campo[c + 1])
        f += 1
    archivo.close()
    return maquina


def duracion(tiempo):  # 3
    matriz_tiempo = [[None] * 2 for i in range(len(tiempo))]

    for f in range(len(tiempo)):
        duracion = 0
        inicio = tiempo[0] * 60 + tiempo[1]
        final = tiempo[2] * 60 + tiempo[3]

        duracion = final - inicio

        matriz_tiempo[f][0] = duracion // 60  # horas
        matriz_tiempo[f][1] = duracion % 60  # min

    h, m = matriz_tiempo[f][0], matriz_tiempo[f][1]
    return h, m


def matriz_tiempo(tiempo):  # 5
    fila = len(tiempo)
    m_tiempo = [[None] * 2 for i in range(fila)]

    for f in range(fila):
        vect_tiempo = duracion(tiempo[f])
        m_tiempo[f][0], m_tiempo[f][1] = vect_tiempo[0], vect_tiempo[1]

    return m_tiempo


def costo(tiempo_total,i): # 4
    costico = (tiempo_total[i][0]) * 3 + ((tiempo_total[i][1] // 15) + 1) * 0.75
    return costico


def monto(vect_tiempo):  # 6
    fila = len(vect_tiempo)
    vect_monto = [None for i in range(fila)]

    for f in range(fila):
        vect_monto[f] = costo(vect_tiempo,f)

    return vect_monto


def mostrar(nombre, tiempo, monto):  # 7
    fila = len(tiempo);
    columna = len(tiempo[0])
    print("maquina     tiempo    monto")
    for f in range(fila):
        print(f"{nombre[f]:12}", end="")
        print(f"{tiempo[f][0]:02d}:{tiempo[f][1]:02d}", end="")
        print(f"    {monto[f]:6.2f}", end="")
        print()


# codigo principal
archivo = "Alquiler.txt"
fila = registro(archivo)

tiempo = [[None] * 4 for i in range(fila)]
nombre = llenado(archivo, tiempo)
tiempo = [[None] * 4 for i in range(fila)]

nombre = llenado(archivo, tiempo)
t = matriz_tiempo(tiempo)
m = monto(t)
mostrar(nombre, t, m)