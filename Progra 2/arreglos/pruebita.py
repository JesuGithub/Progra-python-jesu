from random import randint
filas = int(input('Cuantos alumnos son? : '))
columnas = int(input('Cuantas notas tiene cada uno? : '))
matriz = [[None] * columnas for i in range(filas)]
vector = [None for i in range(filas)]

#notas
for f in range(filas):
    for c in range(columnas):
        notica = int(input(f'Digame la nota {c+1} del alumno {f+1}: '))
        matriz[f][c] = notica

for f in range(filas):
    sumita = 0
    for c in range(columnas):
        sumita += matriz[f][c]
    vector[f] = sumita/columnas

for i in range(filas):
    print(f'El alumno {i+1} tuvo un promedio de: {vector[i]}')

print(len(matriz))
print(len(matriz[0]))