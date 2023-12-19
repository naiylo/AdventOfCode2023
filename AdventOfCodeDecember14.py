# AdventOfCode 14.12.2023

# Explanation: You reach the place where all of the mirrors were pointing: 
# a massive parabolic reflector dish attached to the side of another large mountain
# The dish is made up of many small mirrors, but while the mirrors themselves are 
# roughly in the shape of a parabolic reflector dish, each individual mirror seems to be 
# pointing in slightly the wrong direction. If the dish is meant to focus light, all it's 
# doing right now is sending it in a vague direction. In short: if you move the rocks, you 
# can focus the dish. The platform even has a control panel on the side that lets you tilt 
# it in one of four directions! The rounded rocks (O) will roll when the platform is tilted, 
# while the cube-shaped rocks (#) will stay in place. You note the positions of all of the empty 
# spaces (.) and rocks

example1 = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

example2 = """#.###...OO.#.O.O..O#.....#O#..O....#.#OO....O..#.....O##..#....#..#O...OOO#....##...OO#..O....O....O
...O..........#.OO#....O....#..O.#.....##.##O..OOOO#....#OO..O...O#O.O###O..#..O.O..O..OO...OO#.O..O
O............O....#....O....OO.#...#O..#.O......OO..#.........#O#..#.#......#..O#...###O...O.....OO.
..#...#..O.#O#..OO#O..#O.....O...#.............OO.O..O...O...O....O....#.#.#O........#...O..OO#..#.#
#.........#..#....O##.O#...O#..O#....O.##O.#.#..#....#..OO..#..##..O.##.O#..O#.....O......O....#O...
...O#O....OO.....#....O#.......O#O..............O....OO..O#.........O#.O.OO..O...O#.O..O...O...#....
..O.O#.....O#....OO#..O.#.#O...#..##.OO.O.O..#O....OO#......#...#...##.#..#O#OO#..O.OO..O.#.#.#...O#
....O.O.OO.#.O#.#.#....O##.....##..#OO....O#O..O.O.O#.O.#.O...#..O..O......#..O.O##.#.#O........#O.#
.O.#O#O.#.O.#..###...O.#.#O#....#O#....O..O.OO...O....##.......OO.......#........#....#..O...O.O....
#O.##.O....#O..O.....#...OO..O#..O..#...#.....O..#.OO.........#O#.O.#O#...O.##.O.....O.........#....
....OO#..O.O#.#.O..........O#........#.#O..O.OO.O..#O....#.O#O#..#.#.....O#...O.#.OOOOOO.#O.##.O...O
..#.OO.O.....#.....#O..##..OO....O#.O.#....##.OOO..#O....O..O.#...O.#...O##O....#..O....OO.#O..O..#.
....#O.O#.....O.....O.....O.O.##...O..O#OOOO..O..OO.O#.O#.O...O.OO.#O...#..O..O..O.#...O#......O.OO.
...O....O.....OO....O..OO#.O#...O....O.##..OOO.#....#OO...#.O...........OOO....OO..........#...#...#
......O.....OO#.##.O....#.O.....O.......O...O......#.O..O#.#..#.O#.#.O.##......#...##.#OO#O.O...##O.
...#O......##..O.OO......O.##OO..O..#.O......O.##.#O....O...........#O..O#.O##.#.O...##....#.OOO.OO.
.O#..OO...O.OO#O...#....O..O#OO....OO##.#.##O###O.##...O.O............OOO....#OOO..#.#..OO.#...#####
O.##O.OO.#......##.O..O...#...OO.....O..#........O....O#O#..O#OO##....O..O..#O.#.........#..O.....#.
.O....#.##...#O.O.OO...O#O#......#..O..#O#OO#.#.#O...#O##O#O.#...#..#...#.O...#.OO..OO....#O.#OO....
....#...#OO....OOO.........O.O....#O....#......O..O.OO.O....#..#..#.#...O.O.OO....O#.......#.OO.O#O#
..#O.#........OO.#...#...#.....#OO.......O.OO#.........##.........##.........#O..#.O#....O##......O.
#O#O.#.O..#O#..O..O...#....#.###..#O.O..O#.#........#....#O.O.OO.#.###O#.#.O#..#O...#......O..O#....
OO..#...............O.OOO...#.......O#.OO......O..O..O.#...OO.##.O........#..O#........##.#.#.O#..##
O...#O.#.....O...##.O..O..#.O..O..O#......OO.OO#OO..O..O...OO#.#....O.O...#.#.#.#O.#..O..O.O#....O.#
O...OO..O...O.O.O.O...#...#.....O.#O...........O...O......O.....#..O...OOO##..#.OO..OO...O.OO.##...#
..O....##O#..#..#..O#.O......##.....##O.....#OO##..OO...........O#......#....#.###.O..OO#.#.......#.
.O..#..O.....##....O...#.OO..#.OO..OOO#O..#..O....##O....OO....O.....#O.O..##O....#....OO..O...#O.O.
..#..#.O#.O...#O..O...#..O.............O#.###.O..O..#..........O.#..#..O#.#..OO....#.........O......
...OO..##O..#O#OO#O...##O#.....O...O.O....#...O..OOO..O..#.....O.O#.O.......O..O.#O...OO.#...O.##...
#O..O#....O..O...O..O....#..........O.O...#.O..O.O.....O...O.#O##.O..O##......#..O......#....O.....O
OO#OOO..O.#...OO.......OO......#.O......OO.O.O#.#....O#OOO#O.#.#O#.O..O..#.....##O.#....O..#.OOO.#.O
.#.O.......O...O...#O....O.OO.#.O#......#OO##.#.##..........O.O#...OO#.OO#..O...#...#.O...O.....#...
.O....OOO#..#..O#......O#..#O.#..#O.O#.O...##O..O..#..O...#O.OO...........O...#O.O.......O..#O......
..#....O...O.....O.O.O...O#.#.....#...#O.O.O#...#...O.O#O....O.OOO#OO...O.#O..O##....O.O.###...OO.OO
..#...#..O#..#OO#..O....O..O.#.O....O#.#......O..O.O###.O#.#.....O.#.##..OO#..O....#.O...#..#..#O...
.....#.O.....#.##...#O........#...O....O......O#...OO#.......OO#...O.#..##O.O...O#..O.#..O....O..##.
#.##.O#.......O.O......OO....O.#.#.O.O....#.O.O...O#..#...O..O##.O.O...#..O#.O..O.O...O..#...O.O.#..
.......O.#.O...#O.O.....O.###..#OO..OO.....OO#O.....O..O.O..##..#........O..#O.#..##..O..O..O..O....
.#...O....O#..O..O........O.O.O........OOO.#....O#...#.O....O...OOOO....O.....#..#.....#...#O.O.#.O.
#O#..O.#O........O#....#...OO#.......O....#O....#.#.....O##...O.O...OO..OO#O#.#....#.O#.......O.OO..
.###..#...#..#...#OOO#..#O...........#...#...O....O#..O#..O..O.#..#.#..O.#...OO.#.........OO.##.O.#.
.OO..#..O.OO.O.#O..O..#O##..O.####..O..OO.#.OO.......O.O#OO....OO#OOO..#.#OO........#..#.#.O.O.O..OO
.O.OO#.O.#..O..#O...#.#..O....##.O#.#O.O........O..#.OO....O...OOO#O.#...O................O.....O.O.
.O......#...O.......O.##.#...O...O..OOO....OO..O....#..O.O.O.O..OO..O......O...O#.##..O.....O.OO...O
..OO...O..O#.O.O.O.O..O.#.##.O..##.O......OO....O..O.O..O.....#..#..............OOO.#...#OO.O..O..##
#.....O...OOO#........#O#.#....#....OOOOO..#.#OOO..O.O#O#O.....#..O.O..............O.O#O..#O.OO#.O..
....O.O..O#..O.....#O#...O.#O.##.O..O.#.#.O.....#O...OOO....O....O......#..O.O.#......O...#O.O...O.#
.O.#.O...O.O#....O..#...O....OO.......O.OO.O##..O#..........OO#.O#O#.O.O...#...O.O......#...........
.#O.....O..#....#O............#..O..OO..O.O.OO.#O.....#....#O.#.....O....O..O..O..#...#...O......#..
....OOO.O......#.O..#O..O..#..O.O...O...#O#.O...O.O......OO...O...#..O#.O..#.#O.#O.#O.##OO..O.......
.O..O...#....O.O...O.OO.OO......OOOO...O#....#.O..#.#..#...O........#..#...###...#..........O....#.#
##.#O...O......O#OO....O.....O..OO.O#.OO...##.OO#..O..OO.......#.#.OO.#....O#O.O.O...#.O##.#.O...#..
..#O#..#.OO.O..#O.O...............#.#O...#....#...#..#..#O...........#......##.......O##..O.#...#..O
O.....#.OO##.O..O..###OO....O...............OO..#.....OOO#.O...#O...#.#..#..##...#O#.OO...O......#..
.##....#.O...O#O..O.##.##.O.#.O...#..#.##...#.......O.OOOOO#....#..O...............O.#O...O##.#....#
#.##.O..#.#...O.....OO#.....O.O.OO.OO#...O..O#.....O...#.......##......#.O.....O#.#O.....O..#.#.....
..#..O...O.O#...#O..O...O.O#.#OO...O...#......O.O.....#.O...O..OO....#...OO..O...#....#O..O.O#.....O
.....O.O.....O.OO#O.O....OO#......#.O.O....#.O..OO.O.......O..O.......###.O....#O..#....O.O##....OO#
#.#.O.##.....O....#.#.O.....O..O.O...##O#.O.#O.....#.#........O..O#...#......O#.#O#...#O........O.#.
..O..#..........#..O.O.#..OO.O.O..O..O.OO.#O..#.O..OO..OO.O#..O#OO#O.#.#.O...O.............O....O..O
.#...#O.#........O#..#.....O.##...#..O#..O..O..O.....O#.....OO..##..O..##O.#....O..#O.##.....O..OO..
....#..O.#..#.O...#.....O.O.O.......#.O..O..........O.#O.#.O#..#.....O.#.....O..#O...OO...O..#......
O...#...O........O.O.#O##O.....O....#...O....#....##...#.O.OO.....O.O##.OO#.#.O.OO.O.#O..O......O...
..OO.....O...O.O...O..#..O##OO...#..#.........#O.O#O.......O#OO.O..O..O..O.##O#O.#O..OOO..#.O.O.O.#.
O..O##...OO..#.#..O.#.O.O...#..O.....#....O#..O.O..O..OO.OO.........O..#.#.#...##..#.....O....O.#O..
.#.#......O....O#..O.##.#O.O..OO...#O#O.#..OO.O#....O.##O#....O......#...#O....O..........O.#O....O.
###...O....O...OO....O...O.O....#..#...#.O....O......O.O....#..##...O.#........OO.....#.O....O......
...#.#.O..O#...#.O#.O#.#O#...OO.O#.#O...#O.......O#.#O..#..##.##O##.....##.O.....O...#....#.....##..
OO.O..#.O...#....O#...#.##.#....OO..#..#..O....O#...O#..#..OO...#O.#....##O....#O.O....O.#..#.....O#
.#.O.O..O..#...O...O......O#O....##....O......#......O..#.#...........OOO.#.....O.#.#.............O.
O.....O...#OO.OOO..#....#....#O....O.O..........O...O...#.OO..O.O.##...O.OOOO..O...O....O..O.#......
#O........O..#O#.O..O#.......#OO.....#....#O##.O.O#.O.#O.O....O.O#O....O.O.OO....#.......O...#O..O..
#...O.#.#...#.O.O.#....O.OO...O..O....#...........O....#.OO.OO#.#OO.....OO..O.##....O..#O.....#O..#.
##..#.OO.#OO..OO..##.........O....#...OOO..##O#..O.O.#.##O.#.##O.O...O..#O.O..O.O......#.#OO...O#O..
.O....O#...O.....O#..O...#....O....O#......O..#.#O........#.O#..#..O.#.##..#..........#........O.#.O
.OO#.O.O.###.........O.O..#...#.O..O...OO..#.OO....#..#.........O#.....OO..O......#.......O....O.O#.
OO.OO.O.#.OO..#O..O.......##....O.O.#.##..##..#..O..O#...O...#...#...O.OOO.#O..O...#.O.O....OO......
#.#..O.O.......OO.#.#..O..OO#O.....O#.#......O....O..O##.O.O##..O#.........#OO..O....#.#....O.O..O..
#......#.O.#.....OO...#O.....#.O.........O.#..##O..OOO.##O....O...##...#..O#.O..#...O.OO...OO#....##
O......OO#..O#.#.#...OO.#O....#O#.O#..#..OO...#..#..O.#....#.O.#O.##O...#.....O....OO..........O.##.
.O...O..#O.OO...OOO.#..#..#.#..OO.O......#O#..O.........#........O.OO.O.###....#O#.#.#.#O..OOO....O.
O.....#O#....#....OO..OO...O.....##O.O#.##.O.#......O.#...O#.#O.OO##.........O#...#O##.O...#..O.#..#
.#.##...#O.#O..O#..#.#.#...#...O.O.O#..#.O..O.O#.#......OOO....#.O.O..O.O##..OOO..OO......O....OO#O.
O..##......O...O...O#OO#.......O..O..#....#.#..O....O..OO..O##O#O..#..O...O.O.O..##...#...###.....O.
.O..O...O...#...O...##...O#....O.....O.O.O#..#.....#....O..#.#...OO...OO.O..O..O##....O#O.#O..#....O
.#..O..O..#.#.O.O.#..#.O.#.#.#.#..O..O..O..O...#O....##..#.#.O...OO..#O....#..#.#..O.....O.O.....O.#
#...OO.#.....#.OOO#....O..O...O#O..#.OO..O.O.#...........O.....O.OO.#OO.O##O.......O....O...........
...#.......##.O..#O..O#.#O.....O.#.O.....#O#.#.......#....OO#.....#.#..O.OO#O..O...#..#.O#.#OOO..O..
.#.O............#OO.##O.O.O..#...O....O#O....O....OO..O..O.OO.#...OO#.#..##.OO..##..O.##..#...O.#O..
O#O...#...O#.#..OO.....O.OO..O#...O..#O#OO#..#O##..O.....#.O.#.O.OOOO...O..#.#..O..O...#O..#O#.O....
.O..##.#..O.O.O...O...O.O..#..O.#.O.O.O#.#.O...O.#.#.O##.#.O.O.##...O...O.O...#O#OOOO#...#.OO....#O.
O..O.O....O.O....O.O.O.O.......O.O...O..#O#.OOO#............#.........O..O#.OO#..O#..#.#....#.#.....
.##.O...O..........OO...#O..#.......#..#..##.#.O..O.OO.#..#...O..O#.#.#O..#.OOO#..O..O.OO.#..#..#...
..O.......O#.O...OO.....O.OO..OO#.........#...O#.#.O......O.#...#...........OO..O....##....#.O...O..
...#..O..#....#....##O...O.O....#....#O.....##.#.....OOOO..##.O##........#.O..O.....O...#....O....#O
...O#O...O....O...O...O..#......#..OO..O...#..#...#O......O.O..O.O.O...O..O..#...##.O#.O..O###..OOO#
...O.O.#OOOO.OO...O.......##.#O.#.O...#.....#..O........#.#.O#.#O#...O##.......O..O.....##..O....#.O
..O.O#.O.OO..#...O....O....O...#O..##.....OO.#.#.#.OO.#..OO.......O....##..O#.O.O.......#O#O#O..OO.#
OO#......OO.......O..O..#.OOOO#O......#.###.#O...#O#O...#..O..O....O#.#...#O.###O.#.OO....OO....#...
#.#.O..#....##....#..#................O.......#O.#O#O...##O.OO...O...#...O.##....O.O......##.O..#..O"""

import numpy as np
import copy

# Task one: 
# Tilt the platform so that the rounded rocks all roll north. Afterward, what is the total load on the north support beams?

def tiltNorth(string):
    sum = 0
    rows = string.split("\n")
    matrix = [list(row) for row in rows]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "O":
                count = i
                while (count-1 >= 0) and (matrix[count-1][j] != "#") and (matrix[count-1][j] != "O"):
                    tmp = matrix[count-1][j]
                    matrix[count-1][j] = matrix[count][j]
                    matrix[count][j] = tmp
                    count -= 1
    
    counter = len(matrix) 
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "O":
                sum += counter - i
    
    return sum

# Task two: 
# Each cycle tilts the platform four times so that the rounded rocks roll north, 
# then west, then south, then east. After each tilt, the rounded rocks roll as 
# far as they can before the platform tilts in the next direction. After one cycle, 
# the platform will have finished rolling the rounded rocks in those four directions 
# in that order. Run the spin cycle for 1000000000 cycles. Afterward, what is the 
# total load on the north support beams?

def tiltUp(matrix):  
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "O":
                count = i
                while (count-1 >= 0) and (matrix[count-1][j] != "#") and (matrix[count-1][j] != "O"):
                    tmp = matrix[count-1][j]
                    matrix[count-1][j] = matrix[count][j]
                    matrix[count][j] = tmp
                    count -= 1
    return matrix

def rotate(matrix):
    rotatedMatrix = [[None] * len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            rotatedMatrix[i][j] = matrix[j][len(matrix[0])-1-i]
    return rotatedMatrix

def cycle(matrix, i):
    cycledMatrix = copy.deepcopy(matrix)
    for _ in range(i % 4):
        cycledMatrix = rotate(cycledMatrix)
    return cycledMatrix

def createHash(matrix):
    return "\n".join(["".join(line) for line in matrix])

def doCycle(matrix):
    cycledmatrix = copy.deepcopy(matrix)
    for i in range(4):
        cycledmatrix = cycle(cycledmatrix, 4 - (i % 4))
        cycledmatrix = tiltUp(cycledmatrix)
        cycledmatrix = cycle(cycledmatrix, i % 4)
    return cycledmatrix

def calculateWeight(matrix):
    sum = 0  
    counter = len(matrix) 
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "O":
                sum += counter - i
    return sum

def tilt(string):
    sum = 0
    rows = string.split("\n")
    matrix = [list(row) for row in rows]

    hash = {}
    cycleGrid = {}

    for i in range(10**9):
        matrix = doCycle(matrix)
        newHash = createHash(matrix)

        if newHash in hash:
            onePeriod = i - hash[newHash]
            finalMatrix = cycleGrid[(10**9 - 1 - hash[newHash]) % onePeriod + hash[newHash]]
            return calculateWeight(finalMatrix)

        hash[createHash(matrix)] = i
        cycleGrid[i] = copy.deepcopy(matrix)


if __name__ == "__main__":
    print("Result with function tiltNorth:")
    print("Example 1:")
    print(tiltNorth(example1))
    print("Example 2:")
    print(tiltNorth(example2))
    print("Result with function tilt:")
    print("Example 1:")
    print(tilt(example1))
    print("Example 2:")
    print(tilt(example2))