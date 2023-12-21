# AdventOfCode 16.12.2002

example1 = """.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

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
                print(next)
                if next == "." or "|":
                    return [[aktY-1, aktX, 0]]
                if next == "\\":
                    return [[aktY-1, aktX, 1]]
                if next == "/":
                    return [[aktY-1, aktX, 2]]
                if next == "-":
                    return [[aktY-1, aktX, 1], [aktY-1, aktX, 2]]
            case 3:
                if aktY + 1 > y:
                    return [next]
                next = matrix[aktY+1][aktX]
                print(next)
                if next == "." or "|":
                    return [[aktY+1, aktX, 0]]
                if next == "\\":
                    return [[aktY+1, aktX, 2]]
                if next == "/":
                    return [[aktY+1, aktX, 1]]
                if next == "-":
                    return [[aktY+1, aktX, 1], [aktY+1, aktX, 2]]
            case 1:
                if aktX -1 < 0:
                    return [next]
                next = matrix[aktY][aktX-1]
                print(next)
                if next == "." or "-":
                    return [[aktY, aktX-1, 1]]
                if next == "\\":
                    return [[aktY, aktX-1, 0]]
                if next == "/":
                    return [[aktY, aktX-1, 3]]
                if next == "|":
                    return [[aktY, aktX-1, 0],[aktY, aktX-1, 3]]
            case 2:
                if aktX +1 > x:
                    return [next]
                next = matrix[aktY][aktX+1]
                print(next)
                if next == "." or "-":
                    return [[aktY, aktX+1, 1]]
                if next == "\\":
                    return [[aktY, aktX+1, 3]]
                if next == "/":
                    return [[aktY, aktX+1, 0]]
                if next == "|":
                    return [[aktY, aktX+1, 0],[aktY, aktX+1, 3]]
    except: print("error")
              

def findEnergized(string):
    sum = 0
    rows = string.split("\n")
    matrix = [list(row) for row in rows]
    whereToGo = []
    found = []
    # Startingpoint with direction beeing east
    whereToGo.append([0,0,2])
    while whereToGo != []:
        akt = whereToGo.pop()
        if akt != []:
            found.append([akt[0],akt[1]])
        print(akt)
        print(matrix[akt[1]][akt[0]])
        next = getNextAkt(matrix,akt)
        print(next)
        for i in next:
            whereToGo.append(i)
        print(whereToGo)
            
                

if __name__ == "__main__":
    print("Result with function findEnergized:")
    print("Example 1:")
    print(findEnergized(example1))