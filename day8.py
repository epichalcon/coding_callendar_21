#https://adventofcode.com/2021/day/8

from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}day8.txt")
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


def toBinary(number):
    binary = ['0' for i in range(7)]
    for letter in number:
        binary[ord(letter) - 97] = '1'
    return ''.join(binary)

def rewire(numbers):
    len_map = {}
    for number in numbers:
        if len_map.get(len(number), None) == None:
            len_map[len(number)] = [toBinary(number)]
        else:
            len_map[len(number)].append(toBinary(number))
    
    code = {}
    for number in len_map[6]:
        if int(number,2) | int(len_map[4][0],2) == int(number,2):
            code[number] = '9'
        elif int(number,2) | int(len_map[3][0],2) == int(number,2):
            code[number] = '0'
        else:
            top_rigth_led = int(number,2)^int(len_map[7][0],2)
            code[number] = '6'


    for number in len_map[5]:
        if int(number,2) | int(len_map[2][0],2) == int(number,2):
            code[number] = '3'
        elif int(number,2) | top_rigth_led == int(number,2):
            code[number] = '2'
        else:
            code[number] = '5'

    return code

def decode(code, numbers):
    res = ''
    for number in numbers:
        if len(number) == 2:
            res += '1'
        elif len(number) == 3:
            res += '7'
        elif len(number) == 4:
            res += '4'
        elif len(number) == 7:
            res += '8'
        else:
            res += code[toBinary(number)]
        
    return int(res, 10)

def problem2(data):
    suma = 0
    for linea in data:
        splited = linea.split(' | ')
        coded = rewire(splited[0].split(' '))
        suma += decode(coded, splited[1].split(' '))
    return suma

print(problem2(data))