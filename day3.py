from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
import math
data = gd.getdata(f"{DIRECTORY}day3.txt")
data = gd.separarPorLineas(data)

'''
    Dada una posición consigue la frecuencia de unos que hay en ella
'''
def bitCounter(data, i):
    suma = 0
    for j,_ in enumerate(data):
        suma += int(data[j][i], 10)
    return suma

'''
    Retorna un diccionaro con la frecuencia de unos por posicion
'''
def bitWordCounter(data):
    counter = {}
    for i,_ in enumerate(data[0]):
        counter[i] = bitCounter(data, i)
    return counter

'''
    Se tienen unos bits que representan el consumo del submarino. 
    Para conseguirlo se tienen dos mediciones: Gamma y Epsilon
    Para conseguir Gamma, cada posicion es igual al valor de bit mas comun en esa posicion
    Epsilon es el bit menos comun en esa posicion. 
    El consumo total es la multiplicación en decimal de ambos:
    00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010
    
    Gamma = 10110
    Epsilon = 01001
    '''
def problem1(data):
    counter = bitWordCounter(data)
    gamma_rate = ""
    epsilon_rate = ""
    half = len(data)/2
    #gamma
    for i,_ in enumerate(data[0]):
        if counter.get(i) > half:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    return gamma_rate * epsilon_rate

'''
    Por cada posición elimina los datos que tengan el bit mas o menos comun dependiendo de 
    mostCommon 
    00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010
    Así si mostCommon = true:
    i = 0
    11110
    10110
    10111
    10101
    11100
    10000
    11001
    i = 1
    10110
    10111
    10101
    10000
    i = 2
    10110
    10111
    10101
    i = 3
    10110
    10111
    i = 4
    10111
    '''
def rating(data, mostCommon:bool):
    for i,_ in enumerate(data[0]):
        count = bitCounter(data, i)
        aux = []
        bit = '0'
        if (count >= len(data)-count and mostCommon) or (count < len(data)-count and not mostCommon):
            bit = '1';
        
        for j,_ in enumerate(data):
            if data[j][i] == bit:
                aux.append(data[j])
        
        data = aux
        if(len(data) == 1):
            break#perdon por el break
    return data[0]

def problem2(data):
    ox = int(rating(data, True), 2)
    co2 = int(rating(data, False), 2)
    return ox * co2


print(problem1(data))
print(problem2(data))