from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}day6.txt")

data = list(map(int, data.split(',')))

def problem1(data,iterations):# muy ineficiente
    i = 0
    while i < iterations:
        aux = []
        for fish in data:
            if fish == 0:
                aux.append(6)
                aux.append(8)
            else:
                aux.append(fish - 1)
            data = aux
        i += 1
    return len(data)

def problem2(data, iterations): # complegidad n*m donde n es el numero de iteraciones y m es el tamaño del mapa
    mapa = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0
    }
    suma = 0
    for fish in data:
        mapa[fish] += 1
        suma += 1
    i = 0
    while i < iterations:
        j = 1
        nuevos = mapa.get(0)
        while j < 9:
            mapa[j-1] = mapa.get(j) 
            j += 1
        mapa[6] += nuevos
        mapa[8] = nuevos
        suma += nuevos
        i += 1
    return suma

print(problem2(data, 256))