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

print(problem1(data, 256))