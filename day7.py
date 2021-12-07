from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
import numpy as np
data = gd.getdata(f"{DIRECTORY}day7.txt")

data = list(map(int, data.split(',')))

def problem1(data):
    a = np.array(data)
    median_value = np.percentile(a, 50) 
    suma = 0
    for pos in data:
        suma += abs(median_value - pos)

    return int(suma)


print(problem1(data))