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


def problem1(data, iterations):
    poly = data[0]
    mapa = parser(data[2:len(data)])
    poly = polymerMaker(poly,mapa, iterations)
    counter = Counter(poly)
    maxResult = counter
    maxResult = max(maxResult, key = maxResult.get)
    minResult = counter
    minResult = min(minResult, key = minResult.get)
    return counter[maxResult] - counter[minResult]

def increaseMap(mapa, key, amount):
    if mapa.get(key) is None:
        mapa[key] = amount
    else:
        mapa[key] += amount


def initializeCounters(poly):
    pairCount = {}
    letterCount = {}
    i = 0
    while i < len(poly) - 1:
        increaseMap(letterCount, poly[i], 1)
        key = poly[i]+poly[i+1]
        increaseMap(pairCount, key, 1)
        i += 1
    increaseMap(letterCount,poly[i],1)
    
    return pairCount, letterCount

def problem2(data, iterations):
    poly = data[0]
    template = parser(data[2:len(data)])
    pairCount, letterCount = initializeCounters(poly)
    for _ in range(iterations):
        aux = {}
        for polymer in pairCount:
            newComp = template[polymer]
            increaseMap(aux, polymer[0] + newComp, pairCount[polymer])
            increaseMap(aux, newComp + polymer[1],pairCount[polymer])
            increaseMap(letterCount, newComp,pairCount[polymer])
        pairCount = aux.copy()
    counter = letterCount
    maxResult = counter
    maxResult = max(maxResult, key = maxResult.get)
    minResult = counter
    minResult = min(minResult, key = minResult.get)
    return counter[maxResult] - counter[minResult]


print(problem2(data,40))