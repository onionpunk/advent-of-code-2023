gridNumbers = []
gridSymbols = []

def getGridNumber(row, column):
    target = list(filter(lambda gridnum: gridnum["row"] == row and gridnum["column"] == column, gridNumbers))
    if len(target) > 0:
        return target[0]
    return None

def getAdjacentCells(row, column):
    return [
        (row - 1, column -1), # top left
        (row -1, column), # top
        (row - 1, column + 1), # top right
        (row, column - 1), # left
        (row, column + 1), # right
        (row + 1, column - 1), # bottom left
        (row + 1, column), # bottom
        (row + 1, column + 1), # bottom right
    ]

def setup():
    with open("./input.txt", "r") as fileOpen:
        for row, line in enumerate(fileOpen, 0):
            trimmedLine = line.strip()

            for column, char in enumerate(list(trimmedLine), 0):
                if(char == "."): # ignore dot
                    continue
                elif (char.isnumeric()):
                    gridNumbers.append({
                        "row": row,
                        "column": column,
                        "value": char
                    })
                else:
                    gridSymbols.append({
                        "row": row,
                        "column": column,
                        "value": char
                    })

    currentNumberSet = []
    currentIndex = 0
    while currentIndex < len(gridNumbers):
        evaluate = False
        lastItem = False
        currentNumber = gridNumbers[currentIndex]
        currentNumberSet.append(currentNumber)

        if currentIndex == len(gridNumbers) - 1: # last item
            lastItem = True
            evaluate = True

        if not lastItem:
            nextNumber = gridNumbers[currentIndex + 1]
            if(currentNumber["row"] != nextNumber["row"] or currentNumber["column"] != (nextNumber["column"] - 1)):
                evaluate = True

        if evaluate:
            stringValue = ""
            for gridNumber in currentNumberSet:
                stringValue += gridNumber["value"]
            
            numericValue = int(stringValue)
            firstNumberSet = currentNumberSet[0]
            internalId = f"r{firstNumberSet["row"]}c{firstNumberSet["column"]}"

            for gridNumber in currentNumberSet:
                gridNumber["numeric"] = numericValue
                gridNumber["id"] = internalId

            currentNumberSet = []

        currentIndex += 1

def part1():
    usedNumbers = []
    for symbol in gridSymbols:
        adjacentCells = getAdjacentCells(symbol["row"], symbol["column"])

        for cell in adjacentCells:
            gridNumber = getGridNumber(cell[0], cell[1])
            if gridNumber:
                exist = list(filter(lambda used: used["id"] == gridNumber["id"], usedNumbers))
                if len(exist) == 0:
                    usedNumbers.append(gridNumber)
    total = 0
    for num in usedNumbers:
        total += num["numeric"]

    print(total)

def part2():
    total = 0
    starSymbols = list(filter(lambda symbol: symbol["value"] == "*", gridSymbols))
    for symbol in starSymbols:
        adjacentCells = getAdjacentCells(symbol["row"], symbol["column"])
        cellsWithValues = []

        for cell in adjacentCells:
            gridNumber = getGridNumber(cell[0], cell[1])
            if gridNumber:
                exist = list(filter(lambda used: used["id"] == gridNumber["id"], cellsWithValues))
                if len(exist) == 0:
                    cellsWithValues.append(gridNumber)
        
        if(len(cellsWithValues) == 2):
            total += cellsWithValues[0]["numeric"] * cellsWithValues[1]["numeric"]
    
    print(total)

setup()
part1()
part2()