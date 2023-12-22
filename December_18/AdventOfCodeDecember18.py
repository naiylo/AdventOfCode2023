# AdventOfCode 18.12.2023

with open(r"./AdventOfCode2023/December_18/day18_1.txt") as fin:
    example1 = fin.read().strip().split("\n")
   
with open(r"./AdventOfCode2023/December_18/day18_2.txt") as fin:
    example2 = fin.read().strip().split("\n")

# Task one:

import numpy as  np
from shapely.geometry import Polygon, Point

def findCubicBruteForce(string):
    instructions = [j.split()[i:i+3] for j in string for i in range(0, len(j.split()), 3)]
    marked = []
    akt = (0,0)
    while instructions != []:
        current = instructions.pop(0)
        # print(current)
        stepsToGo = int(current[1])
        while stepsToGo > 0:
            match current[0]:
                case "R":
                    akt = (akt[0],akt[1]+1)
                case "L":
                    akt = (akt[0],akt[1]-1)
                case "U":
                    akt = (akt[0]-1,akt[1])
                case "D":
                    akt = (akt[0]+1,akt[1])
            marked.append(akt)
            stepsToGo -= 1
    # print(marked)
    # To get the dimension
    nMax = 0
    nMin = 0
    for i in marked:
        if i[0] > nMax:
            nMax = i[0]
        if i[0] < nMin:
            nMin = i[0]
    mMax = 0
    mMin = 0
    for i in marked:
        if i[1] > mMax:
            mMax = i[1]
        if i[1] < nMin:
            nMin = i[1]
    n = nMax + abs(nMin)
    m = mMax + abs(mMin)
    matrix = [[' ' for _ in range((m+1)*2)] for _ in range((n+1)*2)]
    # print(np.array(matrix))
    # Just for visualization
    for i in range(len(marked)):
        shifted = (marked[i][0]+n,marked[i][1]+m)
        marked[i] = shifted
        matrix[marked[i][0]][marked[i][1]] = "#"
    # print(np.array(matrix))
    
    polygon = Polygon(marked)
    matrix = np.array(matrix)
    rows, cols = np.indices(matrix.shape)
    points = [Point([i, j]) for i, j in zip(rows.flatten(), cols.flatten())]
    insidePoints = np.array([polygon.contains(p) for p in points])
    count = np.sum(insidePoints)

    return count + len(marked)

def findCubic(string):
    instructions = [j.split()[i:i+3] for j in string for i in range(0, len(j.split()), 3)]
    # print(instructions)
    edges = []
    next = 0
    akt = (0,0)
    for i in instructions:
        match i[0]:
            case "R":
                next = (akt[1] + int(i[1]), akt[0])
            case "L":
                next = (akt[1] - int(i[1]), akt[0])
            case "D":
                next = (akt[1], akt[0] - int(i[1]))
            case "U":
                next = (akt[1], akt[0] + int(i[1]))
        akt = (next[1], next[0])
        edges.append(next)
    # print(edges)

    # To get the needed shift
    nMin = min(edge[0] for edge in edges)
    mMin = min(edge[1] for edge in edges)

    nShift = abs(nMin)
    mShift = abs(mMin)
    # Shift every edge so that everything is positive
    edges = [(edge[0] + nShift, edge[1] + mShift) for edge in edges]

    polygon = Polygon(edges)
    area = polygon.area

    # We add half the perimeter
    perimeter = 0
    for i in instructions:
        perimeter += int(i[1])

    return int(area + perimeter/2 + 1)


# Task two: 

def findTrueCubic(string):
    instructions = [j.split()[i:i+3][2] for j in string for i in range(0, len(j.split()), 3)]
    instructions = [[j[7],int(j[2:7],16)] for j in instructions]
    # print(instructions)
    edges = []
    akt = (0,0)
    next = 0
    for i in instructions:
        match i[0]:
            case "0":
                next = (akt[1] + int(i[1]), akt[0])
            case "2":
                next = (akt[1] - int(i[1]), akt[0])
            case "1":
                next = (akt[1], akt[0] - int(i[1]))
            case "3":
                next = (akt[1], akt[0] + int(i[1]))
        akt = (next[1], next[0])
        edges.append(next)
    # print(edges)

    # To get the needed shift
    nMin = min(edge[0] for edge in edges)
    mMin = min(edge[1] for edge in edges)

    nShift = abs(nMin)
    mShift = abs(mMin)
    # Shift every edge so that everything is positive
    edges = [(edge[0] + nShift, edge[1] + mShift) for edge in edges]

    polygon = Polygon(edges)
    area = polygon.area

    # We add half the perimeter
    perimeter = 0
    for i in instructions:
        perimeter += int(i[1])

    return int(area + perimeter/2 + 1)

    
if __name__ == "__main__":
    print("Result with function findCubic:")
    print("Example 1:")
    print(findCubic(example1))
    print("Example 2:")
    #print(findCubic(example2))
    print("Result with function findTrueCubic:")
    print("Example 1:")
    print(findTrueCubic(example1))
    print("Example 2:")
    print(findTrueCubic(example2))