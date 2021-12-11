#https://adventofcode.com/2021/day/11

from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}day11.txt")
data = gd.separarPorLineas(data)
data = gd.getMatrizDeNumeros(data)

def external(data, i, j):
    return i < 0 or i >= len(data) or j < 0 or j >= len(data[0])

def propagate(data, i, j):
    direct = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    data[i][j] = -1
    for dx,dy in direct:
        if not external(data, i + dy, j+dx) and data[i + dy][j + dx] != -1:
            data[i + dy][j + dx] += 1
            if data[i + dy][j + dx] > 9:
                propagate(data, i + dy, j+dx)
    return data


def step(data):
    for i,row in enumerate(data):
        for j,_ in enumerate(row):
            if data[i][j] == 9:
                data = propagate(data,i,j)
            elif data[i][j] == -1:
                continue
            else:
                data[i][j] += 1
    return data

def countFlashes(data):
    res = 0
    for row,linea in enumerate(data):
        for col,_ in enumerate(linea):
            if data[row][col] > 9 or data[row][col] == -1:
                data[row][col] = 0
                res += 1
    return res


def problem1(data, iterations):
    it = 0
    res = 0
    while it < iterations:
        data = step(data)   
        res += countFlashes(data)
        it += 1
    return res

print(problem1(data,100))