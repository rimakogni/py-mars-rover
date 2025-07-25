from dataclasses import dataclass
from src.utils.enums import CompassDirection

MAX_WIDTH = 55
MAX_HEIGHT = 55
MAX_X = 55
MAX_Y = 55

# 5 5 ->PlateauSize
# 1 2 N -> Position
# LMLMMLLMMMR

@dataclass
class PlateauSize:
    width: int
    height: int
#extra internal proteccion
    def __post_init__(self):
        if self.width < 0:
            raise ValueError("width must be non-negative")
        if self.height < 0:
            raise ValueError("height must be non-negative")
        if self.width > MAX_WIDTH:
            raise ValueError("width exceeds maximum")
        if self.height > MAX_HEIGHT:
            raise ValueError("height exceeds maximum")

@dataclass
class Position:
    x: int
    y: int
    direction: CompassDirection

    def __post_init__(self):
        if self.x < 0:
            raise ValueError("x must be non-negative")
        if self.y < 0:
            raise ValueError("y must be non-negative")
        if self.x > MAX_X:
            raise ValueError("x exceeds maximum")
        if self.y > MAX_Y:
            raise ValueError("y exceeds maximum")
        if not isinstance(self.direction, CompassDirection):
            raise ValueError("Invalid direction")
