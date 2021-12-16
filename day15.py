#https://adventofcode.com/2021/day/15
# Muy poco eficiente
from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
import heapq

data = gd.getdata(f"{DIRECTORY}day15.txt")
data = gd.separarPorLineas(data)
data = gd.getMatrizDeNumeros(data)

def wraparround(num,inc):
    res = (num + inc)%10
    if num + inc >9:
        res += 1
    return res

def secondProblemData(data):
    new_data = [[None for j in range(len(data[0])*5)] for i in range(len(data)*5)]
    for i,row in enumerate(data):
        for j,num in enumerate(row):
            new_data[i][j] = num
            new_data[i + len(data)][j] = wraparround(num,1)
            new_data[i + len(data)*2][j] = wraparround(num,2)
            new_data[i + len(data)*3][j] = wraparround(num,3)
            new_data[i + len(data)*4][j] = wraparround(num,4)
    for i,row in enumerate(new_data):
        for j,num in enumerate(data[0]):
            if i == 49:
                print()
            new_data[i][j + len(data[0])*1] = wraparround(new_data[i][j],1)
            new_data[i][j + len(data[0])*2] = wraparround(new_data[i][j],2)
            new_data[i][j + len(data[0])*3] = wraparround(new_data[i][j],3)
            new_data[i][j + len(data[0])*4] = wraparround(new_data[i][j],4)
    return new_data


def external(data, i, j):
    return i < 0 or i >= len(data) or j < 0 or j >= len(data[0])

def get_adyacent(data, i, j):
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    res = []
    for dx, dy in directions:
        if not external(data, i+dx, j+dy):
            res.append((i+dx, j+dy))
    return res

class Entry():
    left = None
    right = None
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def replace_right(self, new):
        self.right = new

    def replace_left(self, new):
        self.left = new
    
    def __lt__(self,other):
        return self.left < other.left
    
    def __str__(self) -> str:
        return f'({self.left},{self.right})'
    
    def __repr__(self) -> str:
        return f'({self.left},{self.right})'

def dijkstra_nuevo(data:'list[list[int]]'):
    initial = (0,0)
    final = Entry((len(data)-1,len(data)-1),None)
    pq = []
    notInCloud = {}
    found = False
    for i,row in enumerate(data):
        for j,_ in enumerate(row):
            if (j,i) == initial:
                entry = Entry(0,(j,i))
                heapq.heappush(pq,entry)
                notInCloud[(j,i)] = entry
            else:
                entry = Entry(float('inf'),(j,i))
                notInCloud[(j,i)] = entry
                heapq.heappush(pq,entry)
    while len(pq) != 0 and not found:
        entry = heapq.heappop(pq)
        if entry.get_right() == final.get_left():
            found = True
            continue
        vertex = entry.get_right()
        notInCloud.pop(vertex)
        adyacents = get_adyacent(data,vertex[0], vertex[1])
        for adyx, adyy in adyacents:
            other_entry = notInCloud.get((adyx,adyy))
            if other_entry is not None:
                vertex_cost = entry.get_left()
                other_cost = other_entry.get_left()
                cost = data[adyy][adyx]

                new_cost_other = vertex_cost + cost
                if new_cost_other < other_cost:
                    other_entry.replace_left(new_cost_other)
                    heapq.heapify(pq)
                    if other_entry.get_right() == final.get_left():
                        final.replace_right(new_cost_other)
                

    return final.get_right()



data = secondProblemData(data)
print(dijkstra_nuevo(data))