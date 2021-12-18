#https://adventofcode.com/2021/day/15

from typing import Literal
import typing
from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY

data = gd.getdata(f"{DIRECTORY}day16.txt")

VERSION = 3
ID = 3
LITERAL = 4
N_PACK = 11
LEN_PACK = 15
def operate(typeid, literals):
    res = 0
    if typeid == 0:
        res = sum(literals)
    elif typeid == 1:
        res = 1
        for num in literals:
            res *= num
    elif typeid == 2:
        res = min(literals)
    elif typeid == 3:
        res = max(literals)
    elif typeid == 5:
        res = int(literals[0] > literals[1])
    elif typeid == 6:
        res = int(literals[0] < literals[1])
    elif typeid == 7:
        res = int(literals[0] == literals[1])
    return res

def problem1(data: str, numPack = False):
    if data.replace('0','') == '':
        return [], data
    data = data[VERSION:]
    typeid = int(data[:ID],2)
    data = data[ID:]
    if typeid != 4:
        literals = []
        if data.startswith('1'):
            data = data[1:]
            number_pack = int(data[:N_PACK],2)
            data = data[N_PACK:]
            for i in range(number_pack):
                result, data= problem1(data, True)
                literals.extend(result)
            literals = [operate(typeid, literals)]
            result, data = problem1(data)
            literals.extend(result)

        elif data.startswith('0'):
            data = data[1:]
            len_pack = int(data[:LEN_PACK],2)
            data = data[LEN_PACK:]
            literals = problem1(data[:len_pack])[0]
            literals = [operate(typeid, literals)]
            res, data = problem1(data[len_pack:])
            literals.extend(res)
    else:
        literals = []
        while data.startswith('1'):
            data = data[1:]
            literals.append(int(data[:LITERAL], 2))
            data = data[LITERAL:]
        data = data[1:]
        literals.append(int(data[:LITERAL], 2))
        data = data[LITERAL:]
        if not numPack:
            res, data = problem1(data)
            literals.extend(res)

    return literals, data

def problem2(data: str):
    res = 0
    if data.replace('0','') == '':
        return res, data
    version = int(data[:VERSION],2)
    data = data[VERSION:]
    typeid = int(data[:ID],2)
    data = data[ID:]
    if typeid != 4:
        if data.startswith('1'):
            data = data[1:]
            number_pack = int(data[:N_PACK],2)
            data = data[N_PACK:]
            for i in range(number_pack):
                inside_sum, data= problem1(data)
                continue_sum, data = problem1(data)
                res += inside_sum + continue_sum
        
        elif data.startswith('0'):
            data = data[1:]
            len_pack = int(data[:LEN_PACK],2)
            data = data[LEN_PACK:]
            inside_sum = problem1(data[:len_pack])[0]
            continue_sum, data = problem1(data[len_pack:])
            res += inside_sum + continue_sum
    else:
        while data.startswith('1'):
            data = data[LITERAL+1:]
        versum,data = problem1(data[LITERAL+1:])
        res += versum

    return res + version, data


if int(data[0],16) < 8:
    data = '1' + data
    binary_data = bin(int(data,16))[3:]
else:
    binary_data = bin(int(data,16))[2:]
print(problem1(binary_data))