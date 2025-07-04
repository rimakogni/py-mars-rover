from enum import Enum

# 5 5
# 1 2 N -> N CompassDirection
# LMLMMLLMMMR -> Instruction

class CompassDirection(Enum):
    N = "N"
    E = "E"
    S = "S"
    W = "W"

class Instruction(Enum):
    LEFT = "L"
    RIGHT = "R"
    MOVE = "M"