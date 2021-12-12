#https://adventofcode.com/2021/day/12

from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}day12.txt")
data = gd.separarPorLineas(data)

def toGraph(data):
    graph = {}
    for line in data:
        line = line.split('-')
        if graph.get(line[0]) is not None:
            graph[line[0]].append(line[1])
        else:
            graph[line[0]] = [line[1]]
        if graph.get(line[1]) is not None:
            graph[line[1]].append(line[0])
        else:
            graph[line[1]] = [line[0]]
    return graph

def isBigCave(node):
    return 65 <= ord(node[0]) and ord(node[0]) <= 90

'''
si se puede visitar mas veces se guarda un True 
si no se guarda un False'''
def markAsVisited(node, problem, visited:set, repeted):
    if problem == 1:
        if node == 'start':
            visited.add(node)
        elif not isBigCave(node):
            visited.add(node)
    else:
        if node == 'start':
            repeted = None
            visited.add(node)
        elif not isBigCave(node):
            if node in visited and repeted is None:
                repeted = node
            else:
                visited.add(node)
    return repeted


def removeFromVisited(node, problem, visited:set, repeted):
    if problem == 1:
        if node == 'start' or not isBigCave(node):
            visited.remove(node)
    else:
        if node == 'start':
            visited.remove(node)
        elif not isBigCave(node):
            if repeted == node:
                repeted = None
            else:
                visited.remove(node)
    return repeted



def getAllPaths(graph:dict, node, visited:set, paths:list, path:list, repeted, problem:int):
    if (repeted != None and node in visited) or (node == 'start' and repeted != 'start'):
        return 

    if(node == 'end'):
        paths.append(path.copy())
        return
        
    
    repeted = markAsVisited(node, problem, visited, repeted)
    path.append(node)


    for edge in graph.get(node):
        getAllPaths(graph, edge, visited, paths, path, repeted, problem)
    
    repeted = removeFromVisited(node, problem, visited, repeted)
    path.pop()

    return


def problem(graph,problem):
    paths = []
    getAllPaths(graph, 'start', set(), paths,[],'start',problem)
    return len(paths)


graph = toGraph(data)
print(problem(graph,2))