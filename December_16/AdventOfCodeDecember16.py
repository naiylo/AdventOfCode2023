# AdventOfCode 16.12.2023

with open(r"./AdventOfCode2023/December_16/day16_1.txt") as fin:
    lines = fin.read().strip().split("\n")
    for i in range(len(lines)):
        new = lines[i].replace("\\","7")
        lines[i] = new
        # print(lines[i])
    example1 = lines

with open(r"./AdventOfCode2023/December_16/day16_2.txt") as fin:
    lines = fin.read().strip().split("\n")
    for i in range(len(lines)):
        new = lines[i].replace("\\","7")
        lines[i] = new
        # print(lines[i])
    example2 = lines   

# Task one:

# Directions:
#           N = 0
#       W = 1   E = 2
#           S = 3

import numpy as np

def getNextAkt(matrix,akt):
    aktX = akt[1]
    aktY = akt[0]
    direction = akt[2]
    x = len(matrix[0]) -1
    y = len(matrix) -1
    next = []
    try:
        match direction:
            case 0:
                if aktY - 1 < 0:
                    return [next]
                next = matrix[aktY-1][aktX]
                if next == "." or next == "|":
                    return [[aktY-1, aktX, 0]]
                if next == "7":
                    return [[aktY-1, aktX, 1]]
                if next == "/":
                    return [[aktY-1, aktX, 2]]
                if next == "-":
                    return [[aktY-1, aktX, 1], [aktY-1, aktX, 2]]
            case 3:
                if aktY + 1 > y:
                    return [next]
                next = matrix[aktY+1][aktX]
                if next == "." or next == "|":
                    return [[aktY+1, aktX, 3]]
                if next == "7":
                    return [[aktY+1, aktX, 2]]
                if next == "/":
                    return [[aktY+1, aktX, 1]]
                if next == "-":
                    return [[aktY+1, aktX, 1], [aktY+1, aktX, 2]]
            case 1:
                if aktX -1 < 0:
                    return [next]
                next = matrix[aktY][aktX-1]
                if next == "." or next == "-":
                    return [[aktY, aktX-1, 1]]
                if next == "7":
                    return [[aktY, aktX-1, 0]]
                if next == "/":
                    return [[aktY, aktX-1, 3]]
                if next == "|":
                    return [[aktY, aktX-1, 0],[aktY, aktX-1, 3]]
            case 2:
                if aktX +1 > x:
                    return [next]
                next = matrix[aktY][aktX+1]
                if next == "." or next == "-":
                    return [[aktY, aktX+1, 2]]
                if next == "7":
                    return [[aktY, aktX+1, 3]]
                if next == "/":
                    return [[aktY, aktX+1, 0]]
                if next == "|":
                    return [[aktY, aktX+1, 0],[aktY, aktX+1, 3]]
    except: print("error")
              

def findEnergized(string):
    sum = 0
    matrix = string
    whereToGo = []
    found = []
    # Startingpoint with direction beeing east
    start = matrix[0][0]
    if start == "." or start == "-":
        whereToGo.append([0,0,2])
    if start == "|" or start == "7":
        whereToGo.append([0,0,3])     
    while whereToGo != []:
        akt = whereToGo.pop()
        if akt != []:
            found.append((akt[0],akt[1],akt[2]))
            next = getNextAkt(matrix,akt)
            if next != [[]]:
                for i in next:
                    if (i[0],i[1],i[2]) not in found:
                        whereToGo.append(i)
        # print(whereToGo)
        # print(found)
        # print("----")
    final = []
    for i in found:
        final.append((i[0],i[1]))
    final = set(final)
    return len(final)

# Task two:

def howManyEnergized(string,start):
    sum = 0
    matrix = string
    whereToGo = []
    found = []
    # Startingpoint with direction beeing east
    first = matrix[start[1]][start[0]]
    firstDirection = start[2]
    # print(first)
    # print(firstDirection)
    match firstDirection:
        case 0:
            if first == "." or first == "|":
                whereToGo.append(start)
            if first == "7":
                whereToGo.append([start[0],start[1],1])
            if first == "/":
                whereToGo.append([start[0],start[1],2]) 
            if first == "-":
                whereToGo.append([start[0],start[1],2])
                whereToGo.append([start[0],start[1],1])
        case 3:
            if first == "." or first == "|":
                whereToGo.append(start)
            if first == "7":
                whereToGo.append([start[0],start[1],2])
            if first == "/":
                whereToGo.append([start[0],start[1],1]) 
            if first == "-":
                whereToGo.append([start[0],start[1],2])
                whereToGo.append([start[0],start[1],1])
        case 1:
            if first == "." or first == "-":
                whereToGo.append(start)
            if first == "7":
                whereToGo.append([start[0],start[1],3])
            if first == "/":
                whereToGo.append([start[0],start[1],0]) 
            if first == "|":
                whereToGo.append([start[0],start[1],0])
                whereToGo.append([start[0],start[1],3])
        case 2:
            if first == "." or first == "-":
                whereToGo.append(start)
            if first == "7":
                whereToGo.append([start[0],start[1],0])
            if first == "/":
                whereToGo.append([start[0],start[1],3]) 
            if first == "|":
                whereToGo.append([start[0],start[1],0])
                whereToGo.append([start[0],start[1],3])
    # print(whereToGo)
    while whereToGo != []:
        akt = whereToGo.pop()
        if akt != []:
            found.append((akt[0],akt[1],akt[2]))
            next = getNextAkt(matrix,akt)
            if next != [[]]:
                for i in next:
                    if (i[0],i[1],i[2]) not in found:
                        whereToGo.append(i)
        # print(whereToGo)
        # print(found)
        # print("----")
    final = []
    for i in found:
        final.append((i[0],i[1]))
    final = set(final)
    return len(final)

def findMostEnergized(string):
    most = []
    toStart = []
    n, m = len(string)-1, len(string[0])-1
    # Top-left corner
    most.append(howManyEnergized(string,[0,0,2]))
    most.append(howManyEnergized(string,[0,0,3]))
    # Top-right corner
    most.append(howManyEnergized(string,[0,m,1]))
    most.append(howManyEnergized(string,[0,m,3]))
    # Bottom-left corner
    most.append(howManyEnergized(string,[n,0,0]))
    most.append(howManyEnergized(string,[n,0,2]))
    # Bottom-right corner
    most.append(howManyEnergized(string,[n,m,0]))
    most.append(howManyEnergized(string,[n,m,1]))
    # All top and bottom starts
    for i  in range(1,m):
        result = howManyEnergized(string,[0,i,3])
        result2 = howManyEnergized(string,[n,i,0])
        most.append(result)
        most.append(result2)
    # All left and right starts
    for i  in range(1,n):
        result = howManyEnergized(string,[0,i,2])
        result2 = howManyEnergized(string,[m,i,1])
        most.append(result)
        most.append(result2)
    return max(most) 


if __name__ == "__main__":
    print("Result with function findEnergized:")
    print("Example 1:")
    print(findEnergized(example1))
    print("Example 2:")
    print(findEnergized(example2))
    print("Result with function findMostEnergized:")
    print("Example 1:")
    print(findMostEnergized(example1))
    print("Example 2:")
    print(findMostEnergized(example2))