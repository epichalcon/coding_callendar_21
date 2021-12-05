from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}prueva.txt")
data = gd.separarPorLineas(data)

def parser(data):
    coords = []
    for line in data:
        devided = line.split(' -> ')
        beg = devided[0].split(',')
        end = devided[1].split(',')
        coords.append(beg + end)
    return coords

def makePlano(rows, cols):
    plano = []
    for i in range(rows):
        plano.append([])
        for j in range(cols):
            plano[i].append(0)

    return plano

def problem1(data):
    plano = makePlano(1000,1000);
    for elem in data:
        coords = list(map(int,elem))
        if coords[0] == coords[2]:
            if coords[1] <= coords[3]:
                sign = 1
            else:
                sign = -1
            while coords[1] != coords[3]:
                plano[coords[1]][coords[0]] += 1
                coords[1] += sign
            plano[coords[1]][coords[0]] += 1

        elif coords[1] == coords[3]:
            if coords[0] <= coords[2]:
                sign = 1
            else:
                sign = -1

            while coords[0] != coords[2]:
                plano[coords[1]][coords[0]] += 1
                coords[0] += sign
            plano[coords[1]][coords[0]] += 1

    return plano


def sumOverlap(plano):
    count = 0
    for row in plano:
        for col in row:
            if col > 1:
                count += 1

    return count


data = parser(data)
plano = problem1(data)
print(sumOverlap(plano))