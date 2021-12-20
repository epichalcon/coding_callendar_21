#https://adventofcode.com/2021/day/18

from binarytree import Node
import binarytree
from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}prueba.txt")
data = gd.separarPorLineas(data)

def parser(data:'list[str]'):
    scaners = []
    beacons = []
    for line in data:
        if line != '' and not line.startswith('---'):
            line = line.split(',')
            coords = []
            for coord in line:
                coords.append(int(coord))
            beacons.append(coords)
        else:
            scaners.append(beacons)
            beacons = []

    scaners.append(beacons)
    return scaners[1:]

print(parser(data))