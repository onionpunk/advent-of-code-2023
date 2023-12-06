import math

def solveEquationFormula(a, b, c):
    x1 = ( (b * -1) + math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)
    x2 = ( (b * -1) - math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)

    return x1, x2

def setup(file):
    with open(file, "r") as fileOpen:
        lines = [line.rstrip() for line in fileOpen]
        times = [eval(i) for i in (' '.join(lines[0].replace("Time:", "").split()).split(' '))]
        distances = [eval(i) for i in (' '.join(lines[1].replace("Distance:", "").split()).split(' '))]

        return list(zip(times, distances))

def solve(races):
    total = 1
    for race in races:
        time = race[0]
        distance = race[1]
        min, max = solveEquationFormula(-1, time, distance * -1)
        numberOfWaysToBeatDistance = math.ceil(max - 1) - math.floor(min)
        total *= numberOfWaysToBeatDistance
    return total

dataset1 = setup("./input.txt")
dataset2 = setup("./input2.txt")

part1 = solve(dataset1)
print(part1)

part2 = solve(dataset2)
print(part2)