#https://adventofcode.com/2021/day/13

from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}day13.txt")
data = gd.separarPorLineas(data)

def parser(data):
    coords = []
    inst = []
    maxx = 0
    maxy = 0
    for line in data:
        if line == '':
            continue
        if line.startswith('f'):
            inst.append(line.split(' ')[2])
        else:
            aux = line.split(',')
            coords.append([int(aux[0]), int(aux[1])])
            maxx = max(int(aux[0]), maxx)
            maxy = max(int(aux[1]), maxy)
    return coords, inst, maxx, maxy

def createPaper(coords, maxx, maxy):
    paper = [['.' for i in range(maxx+1)] for i in range(maxy+1)]
    for x, y in coords:
        paper[y][x] = '#'
    return paper


def sumaMatriz(paper):
    suma = 0
    for row in paper:
        for col in row:
            if col == '#':
                suma += 1
    return suma

def problem1(coords, inst, maxx, maxy, totalIterations):
    paper = createPaper(coords,maxx,maxy)
    it = 0
    if totalIterations == -1:
        totalIterations = len(inst)
    while it < totalIterations:
        axis, num = inst[it].split('=')
        num = int(num)
        if axis == 'y':
            for i in range(num + 1, len(paper)):
                dif = i - num
                for j,col in enumerate(paper[i]):
                    if col == '#':
                        paper[num - dif][j] = '#'
            paper = paper[0:num]
        if axis == 'x':
            for i,row in enumerate(paper):
                for j in range(num + 1,len(row)):
                    dif = j - num
                    if row[j] == '#':
                        paper[i][num - dif] = '#'
            paper = [[col for col in row[0:num]]for row in paper]
        it += 1

    return sumaMatriz(paper), paper
        
    
def show(paper):
    for row in paper:
        print(''.join(row))

coords, inst, maxx, maxy = parser(data)
res, paper = problem1(coords, inst, maxx, maxy, -1)
show(paper)