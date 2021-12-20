#https://adventofcode.com/2021/day/20

from getdata.getdata import GetData as gd
from constants.constants import  DIRECTORY
data = gd.getdata(f"{DIRECTORY}day20.txt")
data = gd.separarPorLineas(data)

def get_new_image(image,i):
    if i == 0:
        filler = '.'
    else:
        filler = image[0][0]
    blank = [filler for _ in range(len(image[0])+6)]
    new_image = [blank]
    new_image.append(blank)
    new_image.append(blank)
    for row in image:
        newrow = [filler,filler,filler]
        for col in row: 
            newrow.append(col)
        newrow.append(filler)
        newrow.append(filler)
        newrow.append(filler)
        new_image.append(newrow)
    new_image.append(blank)
    new_image.append(blank)
    new_image.append(blank)
    return new_image

def external(data, i, j):
    return i < 0 or i >= len(data) or j < 0 or j >= len(data[0])

def enhan_index(image,i, j):
    binary = ''
    binary += ''.join(image[i-1][j-1:j+2])
    binary += ''.join(image[i][j-1:j+2])
    binary += ''.join(image[i+1][j-1:j+2])
    binary = binary.replace('.','0')
    binary = binary.replace('#','1')

    return int(binary,2)


def iteration(image, enhan):
    new_image = []
    for i,row in enumerate(image):
        if i >= 1 and i <= len(image)-2:
            new_row = []
            for j,col in enumerate(row):
                if j >= 1 and j <= len(row)-2:
                    new_row.append(enhan[enhan_index(image,i,j)])
            new_image.append(new_row)
            
    return new_image

def total_count(image):
    res = 0
    for row in image:
        res += row.count('#')
    return res


def problem1(enhan, image, iterations):
    i = 0
    while i < iterations:
        image = get_new_image(image,i)
        image = iteration(image, enhan)
        i+=1
    
    return total_count(image)
    
enhancement = data[0]
image = data[2:]
print(problem1(enhancement, image,50))