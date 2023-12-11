# AdventOfCode 10.12.2023

# Explanation: 

example1 = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

example2 = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

# Task one:
# 

# direction
#
#       0:N
#   1:W     2:E
#       3:S

def isMoveDoable(direction, nextElement, currentElement, position):
    if currentElement == "|" and direction == 0 and nextElement == "|" or "F" or "7" and position == 0:
        return True
    if currentElement == "|" and direction == 3 and nextElement == "|" or "F" or "7" and position == 3:
        return True
    if currentElement == "-" and direction == 2 and nextElement == "-" or "J" or "7" and position == 2:
        return True
    if currentElement == "-" and direction == 1 and nextElement == "-" or "L" or "F" and position == 1:
        return True
    if currentElement == "L" and direction == 3 and nextElement == "-" or "7" or "J" and position == 2:
        return True
    if currentElement == "L" and direction == 1 and nextElement == "|" or "F" or "7" and position == 0:
        return True
    if currentElement == "F" and direction == 0 and nextElement == "-" or "7" or "J" and position == 2:
        return True
    if currentElement == "F" and direction == 1 and nextElement == "|" or "L" or "7" and position == 3:
        return True
    if currentElement == "J" and direction == 2 and nextElement == "|" or "7" or "F" and position == 0:
        return True
    if currentElement == "J" and direction == 3 and nextElement == "-" or "L" or "F" and position == 1:
        return True
    if currentElement == "7" and direction == 2 and nextElement == "|" or "L" or "J" and position == 0:
        return True
    if currentElement == "7" and direction == 0 and nextElement == "-" or "L" or "F" and position == 1:
        return True

    return False

    return canMove
def getNextPossibleMoves(direction,aktX,aktY):
    if direction == 0:
        nextMoves = [[aktX+1,aktY,2], 
                      [aktX-1,aktY,1],
                      [aktX,aktY-1,0]]
    if direction == 1:
        nextMoves = [[aktX-1,aktY,1],
                     [aktX,aktY-1,0],
                      [aktX,aktY+1,3]]
    if direction == 2:
        nextMoves = [[aktX+1,aktY,2],
                      [aktX,aktY-1,0],
                      [aktX,aktY+1,3]]
    if direction == 3:
        nextMoves = [[aktX+1,aktY,2],
                     [aktX-1,aktY,1],
                     [aktX,aktY+1,3]]
    return nextMoves

def getNextDirection(nextElement, currentDirection):
    if currentDirection == 2:
        if nextElement == "-":
            return 2 
        if nextElement == "7":
            return 3
        if nextElement == "J":
            return 0
    if currentDirection == 0:
        if nextElement == "|":
            return 0
        if nextElement == "7":
            return 1
        if nextElement == "F":
            return 2
    if currentDirection == 1:
        if nextElement == "-":
            return 1 
        if nextElement == "L":
            return 0
        if nextElement == "F":
            return 3
    if currentDirection == 3:
        if nextElement == "|":
            return 3
        if nextElement == "L":
            return 2
        if nextElement == "J":
            return 1
        
def findFurthestPipe(string):
    matrix = []
    for line in string.split("\n"):
        lineMatrix = []
        for pipe in line:
            lineMatrix.append(pipe)
        matrix.append(lineMatrix)
    rowNumberOfStart = 0
    columnNumberOfStart = 0
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if matrix[i][j] == "S":
                rowNumberOfStart = i
                columnNumberOfStart = j
    # What is the start direction and what is our first move
    possibleStarts = [[rowNumberOfStart+1,columnNumberOfStart,2], 
                      [rowNumberOfStart-1,columnNumberOfStart,1],
                      [rowNumberOfStart,columnNumberOfStart+1,3],
                      [rowNumberOfStart,columnNumberOfStart-1,0]]
    for i in matrix:
        print(i)
    for i in possibleStarts:
        counter = 0
        aktX = i[0]
        aktY = i[1]
        aktDirection = i[2]
        aktPipe = matrix[aktY][aktX]
        print("i " + str(i))
        try:
            while aktPipe != "S":
                didMove = 0
                nextMove = getNextPossibleMoves(aktDirection, aktX, aktY)
                print("nextMove " + str(nextMove))
                
                for move in nextMove:
                    if isMoveDoable(aktDirection, matrix[aktX][aktY], aktPipe, move[2]):
                        nextMove = move

                print("move"+ str(move))
                print("aktPipe " + (aktPipe))

                aktX = move[0]
                aktY = move[1]
                aktPipe = matrix[aktY][aktX]
                direction = getNextDirection(aktPipe, aktDirection)
                aktDirection = direction
                        

                print("nextPipe " + (aktPipe) + "\n")
    
                counter += 1
                print("")
        except: print("error\n")
        print("")  
        if counter > 0:
            return counter // 2
    

if __name__ == "__main__":
    #print("Return with function findFurthestPipe:")
    #print("Example 1:")
    print(findFurthestPipe(example1))
    #print("Example 2:")
    #print(findFurthestPipe(example2))