import math
from cell import (
  Cell, 
  DIRECTION_MAP,
  MiniCell
)

cells: [Cell] = []

def setup():
  maxRowIndex = 0
  maxColumnIndex = 0
  with open("./input.txt", "r") as fileOpen:
    for row, line in enumerate(fileOpen, 0):
      trimmedLine = line.strip()
      if maxRowIndex < row:
        maxRowIndex = row

      for column, char in enumerate(list(trimmedLine), 0):
        cells.append(Cell(char, row, column, DIRECTION_MAP[char]))
        if maxColumnIndex < column:
          maxColumnIndex = column
  
  starting_cell = next((c for c in cells if c.value == "S"), None)
  north_cell = getNorthCell(starting_cell)
  east_cell = getEastCell(starting_cell)
  south_cell = getSouthCell(starting_cell)
  west_cell = getWestCell(starting_cell)

  if north_cell is not None and north_cell.direction["south"]:
    starting_cell.direction["north"] = True
  if east_cell is not None and east_cell.direction["west"]:
    starting_cell.direction["east"] = True
  if south_cell is not None and south_cell.direction["north"]:
    starting_cell.direction["south"] = True
  if west_cell is not None and west_cell.direction["east"]:
    starting_cell.direction["west"] = True

  return maxRowIndex, maxColumnIndex

def getNorthCell(cell: Cell):
  return next((c for c in cells if c.row == (cell.row - 1) and c.column == cell.column), None)

def getEastCell(cell: Cell):
  return next((c for c in cells if c.row == cell.row and c.column == (cell.column + 1)), None)

def getSouthCell(cell: Cell):
  return next((c for c in cells if c.row == (cell.row + 1) and c.column == cell.column), None)

def getWestCell(cell: Cell):
  return next((c for c in cells if c.row == cell.row and c.column == (cell.column - 1)), None)

def getNextStartingCellAndDirectionFrom(starting_cell):
  if starting_cell.direction["north"]:
    return getNorthCell(starting_cell), "south"
  if starting_cell.direction["east"]:
    return getEastCell(starting_cell), "west"
  if starting_cell.direction["south"]:
    return getSouthCell(starting_cell), "north"
  if starting_cell.direction["west"]:
    return getWestCell(starting_cell), "east"
  
  return None, None

def part1Setup():
  starting_cell: Cell = next((c for c in cells if c.value == "S"), None)
  starting_cell.partOfMainLoop = True

  current_cell, direction_from = getNextStartingCellAndDirectionFrom(starting_cell)

  # python has no do-while loop :(
  while True:
    current_cell.partOfMainLoop = True

    if current_cell.direction["north"] and direction_from != "north":
      current_cell = getNorthCell(current_cell)
      direction_from = "south"
    elif current_cell.direction["east"] and direction_from != "east":
      current_cell = getEastCell(current_cell)
      direction_from = "west"
    elif current_cell.direction["south"] and direction_from != "south":
      current_cell = getSouthCell(current_cell)
      direction_from = "north"
    elif current_cell.direction["west"] and direction_from != "west":
      current_cell = getWestCell(current_cell)
      direction_from = "east"

    if current_cell.value == "S":
      break


part2Cells: [MiniCell] = []
part2OuterCells: [MiniCell] = []

def getNorthMiniCell(cell: MiniCell):
  return next((c for c in part2Cells if c.row == (cell.row - 1) and c.column == cell.column), None)

def getEastMiniCell(cell: MiniCell):
  return next((c for c in part2Cells if c.row == cell.row and c.column == (cell.column + 1)), None)

def getSouthMiniCell(cell: MiniCell):
  return next((c for c in part2Cells if c.row == (cell.row + 1) and c.column == cell.column), None)

def getWestMiniCell(cell: MiniCell):
  return next((c for c in part2Cells if c.row == cell.row and c.column == (cell.column - 1)), None)

def getOuterCell(cell: MiniCell):
  return next((c for c in part2OuterCells if c.id == cell.id), None)

def part2(maxRowIndex: int, maxColumnIndex: int):
  # we are going to convert the original grid cells into 3x3 mini cells
  part2maxRowIndex = (maxColumnIndex * 3) + 2
  part2maxColumnIndex = (maxRowIndex * 3) + 2

  cell: Cell
  for cell in cells:
    baseRow: int = cell.row * 3
    baseColumn: int = cell.column * 3
    solidNorth = True if cell.partOfMainLoop and cell.direction["north"] else False
    solidWest = True if cell.partOfMainLoop and cell.direction["west"] else False
    solidCenter = True if cell.partOfMainLoop else False
    solidEast = True if cell.partOfMainLoop and cell.direction["east"] else False
    solidSouth = True if cell.partOfMainLoop and cell.direction["south"] else False

    northwest_cell: MiniCell = MiniCell(parentId=cell.id, row=baseRow, column=baseColumn, solid=False, partOfMainLoop=cell.partOfMainLoop)
    north_cell: MiniCell = MiniCell(parentId=cell.id, row=baseRow, column=(baseColumn + 1), solid=solidNorth, partOfMainLoop=cell.partOfMainLoop)
    northeast_cell: MiniCell = MiniCell(parentId=cell.id, row=baseRow, column=(baseColumn + 2), solid=False, partOfMainLoop=cell.partOfMainLoop)

    west_cell: MiniCell = MiniCell(parentId=cell.id, row=(baseRow+1), column=baseColumn, solid=solidWest, partOfMainLoop=cell.partOfMainLoop)
    center_cell: MiniCell = MiniCell(parentId=cell.id, row=(baseRow+1), column=(baseColumn+1), solid=solidCenter, partOfMainLoop=cell.partOfMainLoop)
    east_cell: MiniCell = MiniCell(parentId=cell.id, row=(baseRow+1), column=(baseColumn+2), solid=solidEast, partOfMainLoop=cell.partOfMainLoop)

    southwest_cell: MiniCell = MiniCell(parentId=cell.id, row=(baseRow+2), column=baseColumn, solid=False, partOfMainLoop=cell.partOfMainLoop)
    south_cell: MiniCell = MiniCell(parentId=cell.id, row=(baseRow+2), column=(baseColumn + 1), solid=solidSouth, partOfMainLoop=cell.partOfMainLoop)
    southeast_cell: MiniCell = MiniCell(parentId=cell.id, row=(baseRow+2), column=(baseColumn + 2), solid=False, partOfMainLoop=cell.partOfMainLoop)

    part2Cells.append(northwest_cell)
    part2Cells.append(north_cell)
    part2Cells.append(northeast_cell)

    part2Cells.append(west_cell)
    part2Cells.append(center_cell)
    part2Cells.append(east_cell)

    part2Cells.append(southwest_cell)
    part2Cells.append(south_cell)
    part2Cells.append(southeast_cell)

  cellsToExplore: [MiniCell] = []
  firstRows = list(filter(lambda c: c.partOfMainLoop == False and c.row == 0, part2Cells))
  LastRows = list(filter(lambda c: c.partOfMainLoop == False and c.row == part2maxRowIndex, part2Cells))
  firstColumns = list(filter(lambda c: c.partOfMainLoop == False and c.column == 0, part2Cells))
  lastColumns = list(filter(lambda c: c.partOfMainLoop == False and c.column == part2maxColumnIndex, part2Cells))
  cellsToExplore.extend(firstRows)
  cellsToExplore.extend(LastRows)
  cellsToExplore.extend(firstColumns)
  cellsToExplore.extend(lastColumns)

  while len(cellsToExplore) > 0:
    cell: MiniCell = cellsToExplore.pop(0)
    if cell.processed:
      continue

    existingCell = getOuterCell(cell)
    if existingCell is None:
      part2OuterCells.append(cell)

    north_minicell: MiniCell = getNorthMiniCell(cell)
    east_minicell: MiniCell = getEastMiniCell(cell)
    south_minicell: MiniCell = getSouthMiniCell(cell)
    west_minicell: MiniCell = getWestMiniCell(cell)

    if north_minicell is not None and not north_minicell.solid and getOuterCell(north_minicell) is None:
      cellsToExplore.append(north_minicell)
    if east_minicell is not None and not east_minicell.solid and getOuterCell(east_minicell) is None:
      cellsToExplore.append(east_minicell)
    if south_minicell is not None and not south_minicell.solid and getOuterCell(south_minicell) is None:
      cellsToExplore.append(south_minicell)
    if west_minicell is not None and not west_minicell.solid and getOuterCell(west_minicell) is None:
      cellsToExplore.append(west_minicell)

    cell.processed = True

maxRowIndex, maxColumnIndex = setup()
part1Setup()

mainLoops = list(filter(lambda c: c.partOfMainLoop == True, cells))
print(f"part1: {math.ceil(len(mainLoops) / 2)}")

part2(maxRowIndex, maxColumnIndex)

outerLoopIds: [str] = []
withoutMainLoopCells: [MiniCell] = list(filter(lambda c: c.partOfMainLoop == False, part2OuterCells))
miniCell: MiniCell
for miniCell in withoutMainLoopCells:
  idExist = next((id for id in outerLoopIds if id == miniCell.parentId), None)
  if idExist is None:
    outerLoopIds.append(miniCell.parentId)

print(f"all cells: {len(cells)}")
print(f"mainLoops: {len(mainLoops)}")
print(f"outerLoopCells: {len(outerLoopIds)}")
print(f"remaining: {len(cells) - (len(mainLoops) + len(outerLoopIds))}")

from datetime import datetime
print(datetime.now())