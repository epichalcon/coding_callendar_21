#https://adventofcode.com/2021/day/10

from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}prueva.txt")
data = gd.separarPorLineas(data)

class CloserNotExpected(Exception):
    closer = ''
    def __init__(self, closer) -> None:
        self.closer = closer



def syntaxChecker(line) -> list:
    openers = ('(','[','{','<')
    closers = (')',']','}','>')
    stack = []
    for char in line:
        try:
            opener = openers.index(char)
            stack.append(opener)
        except ValueError:
            closer = closers.index(char)
            lastOpener = stack.pop()
            if closer != lastOpener:
                raise CloserNotExpected(closer)
    return stack




def problem1(data) -> int:
    res = 0
    points = {
        0: 3,
        1:57,
        2:1197,
        3:25137
    }
    for line in data:
        try:
            syntaxChecker(line)
        except CloserNotExpected as exc:
            res += points[exc.closer]

    return res




print(problem1(data))