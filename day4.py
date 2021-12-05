from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}day4.txt")
data = gd.separarPorLineas(data)


'''Separa los datos en los numeros y las matrices'''
def parser(data):
    matrices = []
    matriz = []
    i = 0#numero de matriz
    j = 0#numero de fila
    for lineNumb,line in enumerate(data):
        if lineNumb == 0:
            numeros = line.split(',')

        elif line == '' and lineNumb != 1:
            matrices.append(matriz)
            matriz = []

        elif line != '':
            k = 0#numero de columna
            row = []

            for x,letter in enumerate(line):
                if letter == ' ' and x != 0 and line[x-1] != ' ':
                    k += 1
                elif letter != ' ':
                    if k == len(row):
                        row.append(letter)
                    else:
                        row[k] += letter
            matriz.append([int(x) for x in row])

    matrices.append(matriz)
    matriz = []
    return numeros, matrices
    


def sumaMatriz(matriz):
    sum = 0
    for row in matriz:
        for col in row:
            if col != '-':
                sum += col 
    return sum

def crearMapa(matrices):
    mapa = {}
    for k,matriz in enumerate(matrices):
        for i,row in enumerate(matriz):
            mapa[str(k) + '-' + str(i)] = len(row)
    for k,matriz in enumerate(matrices):
        for i,col in enumerate(matriz):
            mapa[str(k) + '-' + chr(i + 97)] = len(col)

    return mapa

def simularJuego(numeros, matrices, mapa):

    ganado = -1
    x = 0#indice del numero a comprobar
    while ganado == -1 and x < len(numeros):
        numero = int(numeros[x])
        for i,matriz in enumerate(matrices):
            for j,row in enumerate(matriz):
                for k, col in enumerate(row):
                    if col == numero:
                        matrices[i][j][k] = '-'
                        mapa[str(i) + '-' + str(j)] -= 1
                        mapa[str(i) + '-' + chr(k + 97)] -= 1
                        if mapa[str(i) + '-' + str(j)] == 0 or mapa[str(i) + '-' + chr(k + 97)] == 0:
                            ganado = i
        x += 1
    return numero, ganado

def problem1(numeros, matrices):
    mapa = crearMapa(matrices)
    numero, ganador = simularJuego(numeros, matrices, mapa)

    return numero * sumaMatriz(matrices[ganador])


def problem2(numeros, matrices):
    x = 0
    eliminados = 0
    mapa = crearMapa(matrices)
    ultimo = []
    while eliminados < len(matrices):
        numero = int(numeros[x])
        for i,matriz in enumerate(matrices):
            if len(matriz) != 0:
                for j,row in enumerate(matriz):
                    for k, col in enumerate(row):
                        if col == numero:
                            matrices[i][j][k] = '-'
                            mapa[str(i) + '-' + str(j)] -= 1
                            mapa[str(i) + '-' + chr(k + 97)] -= 1
                            if mapa[str(i) + '-' + str(j)] == 0 or mapa[str(i) + '-' + chr(k + 97)] == 0:
                                ultimo = matriz.copy()
                                matrices[i] = []
                                eliminados += 1
        x += 1
    return numero * sumaMatriz(ultimo)


numeros, matrices = parser(data)
print(problem2(numeros, matrices))
