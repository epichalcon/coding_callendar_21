#https://adventofcode.com/2021/day/9

from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}day9.txt")
data = gd.separarPorLineas(data)

data = [[*map(int,list(line))] for line in data]

def external(data, i, j):
    return i < 0 or i >= len(data) or j < 0 or j >= len(data[0])

def is_low_point(data, i, j) -> bool:
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    res = True
    for dy, dx in directions:
        if not external(data, i+dy, j+dx) and data[i + dy][j + dx] <= data[i][j]:
            res = False
            break
    return res

def find_low_points(data):
    low_points = []
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if is_low_point(data, i, j):
                low_points.append((i,j))

    return low_points


def problem1(data) -> int:
    suma = 0
    low_points = find_low_points(data)
    for y,x in low_points:
        suma += data[y][x] + 1
    return suma

def fill_basin(data:list, point:tuple, low_points:list, basin:list, visited_low_points:list):
    i, j = point
    basin.append((i, j))
    if (i,j) in low_points:
        visited_low_points.append(point)
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    for dy, dx in directions:
        if not external(data, i+dy, j+dx) and data[i + dy][j + dx] != 9 and not (i+dy, j+dx) in basin:
            fill_basin(data, (i+dy,j+dx),low_points, basin, visited_low_points)


def separate_basins(data, low_points):
    basins = []
    visited_low_points = []
    for point in low_points:
        if not point in visited_low_points:
            basin = []
            other_low_points = fill_basin(data, point, low_points, basin, visited_low_points)
            basins.append(basin)

    return basins

def problem2(data) -> int:
    res = 1
    low_points = find_low_points(data)
    basins = separate_basins(data, low_points)
    largest = [*map(len,basins[0:3])]
    for i,basin in enumerate(basins):
        if i > 2 and len(basin) > min(largest):
            largest.remove(min(largest))
            largest.append(len(basin))
    for num in largest:
        res *= num
    return res


print(problem2(data))