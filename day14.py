#https://adventofcode.com/2021/day/14

from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}day14.txt")
data = gd.separarPorLineas(data)
from collections import Counter

def parser(data):
    mapa = {}
    for line in data:
        aux = line.split(' -> ')
        mapa[aux[0]] = aux[1]
    return mapa

def polymerMaker(poly, mapa, iterations):
    it = 0
    while it < iterations:
        i = 0
        aux = ''
        while i < len(poly) - 1:
            if i == 0:
                aux += poly[i]
            key = poly[i]+poly[i+1]
            aux += mapa[key]
            aux += poly[i+1]
            i += 1
        poly = aux
        it += 1
    return poly


def problem(poly, mapa, iterations):
    poly = polymerMaker(poly,mapa, iterations)
    counter = Counter(poly)
    maxResult = counter
    maxResult = max(maxResult, key = maxResult.get)
    minResult = counter
    minResult = min(minResult, key = minResult.get)
    return counter[maxResult] - counter[minResult]


poly = data[0]
mapa = parser(data[2:len(data)])
print(problem1(poly, mapa,10))