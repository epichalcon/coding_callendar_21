#https://adventofcode.com/2021/day/10

from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}prueva.txt")
data = gd.separarPorLineas(data)

def problem1(data) -> int:
    openers = ('(','[','{','<')
    closers = (')',']','}','>')
    points = {
        0: 3,
        1:57,
        2:1197,
        3:25137
    }
    res = 0
    for line in data:
        stack = []
        for char in line:
            try:
                opener = openers.index(char)
                stack.append(opener)
            except ValueError:
                closer = closers.index(char)
                lastOpener = stack.pop()
                if closer != lastOpener:
                    res += points[closer]
    return res

print(problem1(data))