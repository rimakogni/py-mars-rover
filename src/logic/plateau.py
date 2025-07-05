from src.utils.models import PlateauSize, Position

class Plateau:
    def __init__(self, size: PlateauSize):
        self.size = size

    def is_within_bounds(self, position: Position) -> bool:
        return (
            0 <= position.x <= self.size.width and
            0 <= position.y <= self.size.height
        )