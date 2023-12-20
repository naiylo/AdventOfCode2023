# AdventOfCode 06.12.2023

example1 = """Time:      7  15   30
Distance:  9  40  200"""

example2 = """Time:        57     72     69     92
Distance:   291   1172   1176   2026"""

example3 = """Time:      57726992
Distance:  291117211762026"""

# Task one:

def generateRange(time):
    dict = []
    for i in range(0,time+1):
        speed = i
        remainingTime = time - i
        subDict = [i,remainingTime*speed]
        dict.append(subDict)
    return dict

def calculateRange(string):
    races = [lines for lines in string.split() if lines.isdigit()]
    races = [races[:(len(races) // 2)],races[(len(races) // 2):]]
    numberOfWins = []
    for i in range(0,len(races[0])):
        race = races[0][i]
        toBeat = races[1][i]
        dictForRace = generateRange(int(race))
        count = 0
        for i in dictForRace:
            if i[1] > int(toBeat):
                count += 1
        if count > 0:
            numberOfWins.append(count)
        else:
            numberOfWins.append(1)
    sum = 1
    for i in numberOfWins:
        sum *= i
    return sum

# Task two:

def calculateRangeForOneLargeRace(string):
    races = [lines for lines in string.split() if lines.isdigit()]
    races = [races[:(len(races) // 2)],races[(len(races) // 2):]]
    sum = 0
    for hold in range(0,int(races[0][0])):
        if int(races[1][0]) < hold * (int(races[0][0])-hold):
            sum += 1
    return sum


if __name__ == "__main__":
    print("Result of function calculateRange:")
    print("Example1:")
    print(calculateRange(example1))
    print("Example 2:")
    print(calculateRange(example2))
    print("Example 3:")
    print(calculateRangeForOneLargeRace(example3))
    

