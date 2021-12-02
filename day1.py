from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}day1.txt")
data = gd.separarPorLineas(data)

def problem1(data):
    res = 0
    prev = data[0]
    for profundidad in data:
        if profundidad >= prev:
            res += 1
        prev = profundidad
    return res

def divide(data):
    divided = []
    i = 0
    while i + 2 < len(data):
        divided.append([int(data[i]),int(data[i+1]),int(data[i+2])])
        i += 1
    return divided

def problem2(data):
    res = 0
    divided = divide(data)
    prev = 0
    for thresom in divided:
        suma = sum(thresom)
        if prev == 0:
            prev = suma
        if suma > prev:
            res +=1
        prev = suma
    return res

print(problem2(data))