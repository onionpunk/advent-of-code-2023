from typing import TypedDict

class Direction(TypedDict):
  north: bool
  east: bool
  south: bool
  west: bool

class Cell:
  id: str
  value: str
  row: int
  column: int
  direction: Direction
  costFromStarting: int
  partOfMainLoop: bool
  
  def __init__(self, value: str, row: int, column: int, dir: Direction):
    self.id = f"{str(row)},{str(column)}"
    self.value = value
    self.row = row
    self.column = column
    self.direction = dir
    self.costFromStarting = 0
    self.partOfMainLoop = False

DIRECTION_MAP = {
  "|": Direction({"north": True, "east": False, "south": True, "west": False}),
  "-": Direction({"north": False, "east": True, "south": False, "west": True}),
  "L": Direction({"north": True, "east": True, "south": False, "west": False}),
  "J": Direction({"north": True, "east": False, "south": False, "west": True}),
  "7": Direction({"north": False, "east": False, "south": True, "west": True}),
  "F": Direction({"north": False, "east": True, "south": True, "west": False}),
  ".": Direction({"north": False, "east": False, "south": False, "west": False}),
  "S": Direction({"north": False, "east": False, "south": False, "west": False})
}

class MiniCell:
  id: str
  parentId: str
  row: int
  column: int
  solid: bool
  partOfMainLoop: bool
  processed: bool

  def __init__(self, parentId: str, row: int, column: int, solid: bool, partOfMainLoop: bool):
    self.id = f"{parentId}|{str(row)},{str(column)}"
    self.parentId = parentId
    self.row = row
    self.column = column
    self.solid = solid
    self.partOfMainLoop = partOfMainLoop
    self.processed = False