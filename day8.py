
from numpy.core.fromnumeric import mean
from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
import numpy as np
import math
data = gd.getdata(f"{DIRECTORY}prueva.txt")
data = gd.separarPorLineas(data)

def problem1(data):
    suma = 0
    for linea in data:
        right = linea.split(' | ')[1]
        numbers = right.split(' ')
        for number in numbers:
            if len(number) in [2,4,3,7]:
                suma += 1
    return suma

print(problem1(data))
