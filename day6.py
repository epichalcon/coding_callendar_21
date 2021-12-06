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

def problem2(data, iterations): # complegidad o(n)
    lista = [0 for i in range(9)]
    suma = 0
    for fish in data:
        lista[fish] += 1
        suma += 1
    i = 0
    while i < iterations:
        j = 1
        nuevos = lista[0]
        while j < 9:
            lista[j-1] = lista[j] 
            j += 1
        lista[6] += nuevos
        lista[8] = nuevos
        suma += nuevos
        i += 1
    return suma

print(problem2(data, 256))