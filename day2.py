from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}day2.txt")
data = gd.separarPorLineas(data)

def problem1(data):
    x, y = 0,0
    for inst in data:
        direc, units = inst.split()
        
        if direc == 'forward':
            x += int(units)
        elif direc == 'up':
            y -= int(units)
        else:
            y += int(units)
        
    return x*y

def problem2(data):
    x,y,aim = 0,0,0

    for inst in data:
        direc, units = inst.split()
        if direc == 'forward':
            x += int(units)
            y += int(units)*aim
        elif direc == 'up':
            aim -= int(units)
        else:
            aim += int(units)
    return x*y

print(problem2(data))