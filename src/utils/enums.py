from enum import Enum

class CompassDirection(Enum):
    N = "N"
    E = "E"
    S = "S"
    W = "W"

class Instruction(Enum):
    LEFT = "L"
    RIGHT = "R"
    MOVE = "M"