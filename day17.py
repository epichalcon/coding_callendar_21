#https://adventofcode.com/2021/day/17

from typing import Counter
from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY

PRUEBAX = [20,30]
PRUEBAY = [-10,-5]

DAYX = [57,116]
DAYY = [-198,-148]

def check_in_target(x,y,targetx, targety):
    minx = min(targetx)
    miny = min(targety)
    maxx = max(targetx)
    maxy = max(targety)
    if x in range(minx, maxx+1) and y in range(miny, maxy+1):
        return True
    return False


def simulate(x,y,velx, vely):
    x += velx
    y += vely
    vely -= 1
    if velx > 0:
        velx -= 1
    elif velx < 0:
        velx += 1
    return x, y, velx, vely

def enters_target(x,y,velx, vely, targetx,targety):
    in_target = False
    while y >= min(targety) and x <= max(targetx) and not in_target:
        in_target = check_in_target(x,y,targetx,targety)
        x, y, velx, vely = simulate(x,y,velx, vely)
    return in_target

def get_max_point(x,y,velx, vely):
    while vely > 0:
        x, y, velx, vely = simulate(x,y,velx, vely)
    return x,y
    

def problem1(targetx,targety):
    x, y = 0,0

    velx = 1
    while velx*(velx+1)/2 < min(targetx) :
        velx += 1
    
    vely = abs(min(targety) - y) - 1

    if not enters_target(x,y,velx,vely,targetx,targety):
        return 'error'

    maxx, maxy = get_max_point(x,y,velx,vely)

    return maxy

def problem2(targetx, targety):

    min_velx = 1
    max_velx = max(targetx)
    while min_velx*(min_velx+1)/2 < min(targetx) :
        min_velx += 1
    
    max_vely = abs(min(targety)) - 1
    min_vely = min(targety)

    res = 0
    for velx in range(min_velx, max_velx+1):
        for vely in range(min_vely, max_vely+1):
            if enters_target(0,0,velx, vely, targetx, targety):
                res += 1

    return res

print(problem2(DAYX,DAYY))