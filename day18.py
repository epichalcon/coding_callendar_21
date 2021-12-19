#https://adventofcode.com/2021/day/18

from binarytree import Node
import binarytree
from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}day18.txt")
data = gd.separarPorLineas(data)

def construct_tree(line: str, node = Node(-1)):
    if line.startswith('['):
        node.left, line = construct_tree(line[1:],Node(-1))
    if line.startswith(','):
        node.right, line = construct_tree(line[1:],Node(-1))
    if line.startswith(']'):
        return node, line[1:]
    else:
        return Node(int(line[0])), line[1:]

def easyExplode(tree:Node, node:Node, depth):
    splitlist = []
    side_exp(tree, node, node.left, node.left.val, 'l',depth, splitlist)
    side_exp(tree,node, node.right, node.right.val, 'r', depth, splitlist)
    node.val = 0
    del node[1]
    del node[2]
    return tree

def side_exp(tree:Node,parent:Node, node:Node,value, side, depth, splitlist = []):
    if depth < 0:
        return tree
    new_parent = binarytree.get_parent(tree, parent)
    if side == 'l':
        if parent.left == node:
            tree = side_exp(tree,new_parent, parent,value, 'l', depth-1, splitlist)
        else:
            change = parent.left
            depth += 1
            while change.right != None:
                change = change.right
                depth += 1
            change.val += value
            if change.val > 9:
                splitlist.append((change, depth))
    else:
        if parent.right == node:
            tree = side_exp(tree,new_parent, parent,value, 'r',depth-1, splitlist)
        else:
            change = parent.right
            depth += 1
            while change.left != None:
                change = change.left
                depth += 1
            change.val += value
            if change.val > 9:
                splitlist.append((change, depth))
    return tree
    

def explode(tree:Node, node:Node, depth):
    splitlist = []
    side_exp(tree, node, node.left, node.left.val, 'l',depth, splitlist)
    side_exp(tree,node, node.right, node.right.val, 'r', depth, splitlist)
    node.val = 0
    del node[1]
    del node[2]
    for change, depth in splitlist:
        tree = split(tree, change, depth)
    return tree

def split(tree, node, depth):
    if node.val <= 9:
        return tree
    node.left = Node(node.val//2)
    node.right = Node(node.val//2)
    if node.val%2 != 0:
        node.right.val += 1
    node.val = -1
    if depth >= 4:
        explode(tree, node, depth)
    return tree

def snail_reduce(tree:Node, node:Node, depth):
    if depth >= 4 and node.val == -1 and node.left.val != -1 and node.right.val != -1:
        tree = explode(tree, node, depth)
    elif node.val > 9:
        tree = split(tree, node, depth)
    return tree

def snail_sum(tree:Node, node: Node, depth = 0):
    if tree.height <= 4 and tree.max_node_value <= 9:
        return tree
    
    snail_reduce(tree, node, depth)
    
    if node.left != None:
        tree = snail_sum(tree, node.left, depth + 1)
    if node.right != None:
        tree = snail_sum(tree, node.right, depth + 1)
    
    return tree

def makePerfect(tree:Node, node: Node, depth = 0):
    if tree.height <= 4 and tree.max_node_value <= 9:
        return tree
    
    if depth >= 4 and node.val == -1 and node.left.val != -1 and node.right.val != -1:
        tree = easyExplode(tree, node, depth)
    
    if node.left != None:
        tree = makePerfect(tree, node.left, depth + 1)
    if node.right != None:
        tree = makePerfect(tree, node.right, depth + 1)
    
    return tree

def construct_data_tree(data):
    prev = -1
    for line in data:
        newRoot = Node(-1)
        tree = construct_tree(line,Node(-1))[0]
        if prev != -1:
            newRoot.left = prev
            newRoot.right = tree
            newRoot = makePerfect(newRoot, newRoot)
            newRoot = snail_sum(newRoot, newRoot)

            prev = newRoot
        else:
            prev = tree
    return newRoot

def magnitude(node):
    if node.val != -1:
        return node.val
    
    res = 0
    if node.left != None:
        res += magnitude(node.left)*3
    if node.right != None:
        res += magnitude(node.right)*2
    return res
    
def problem1(tree):
    return magnitude(tree)

def problem2(data):
    maxsum = 0
    for line1 in data:
        for line2 in data:
            if line1 != line2:
                tree = Node(-1)
                tree.left = construct_tree(line1,Node(-1))[0]
                tree.right = construct_tree(line2,Node(-1))[0]
                reduced_tree = makePerfect(tree, tree)
                reduced_tree = snail_sum(reduced_tree, reduced_tree)
                maxsum = max(maxsum, magnitude(reduced_tree))
    return maxsum
                
print(problem2(data))