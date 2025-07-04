from src.parsers.compass_parser import CompassParser
from src.utils.models import Position

class PositionParser:
    @staticmethod
    def parse(position_str:str) -> Position:
        try:
            x_str,y_str, dir_str = position_str.strip().split()
            x = int(x_str)
            y = int(y_str)
            dir = CompassParser.parse(dir_str)
            return Position(x,y,dir)
        except Exception:
            raise ValueError(f"Invalid position string: {position_str}")