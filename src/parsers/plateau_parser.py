from src.utils.models import PlateauSize

class PlateauParser:
    @staticmethod
    def parse(size_str:str) -> PlateauSize:
        try:
            width, height = map(int, size_str.strip().split())
            return PlateauSize(width, height)
        except Exception:
            raise ValueError(f"Invalid plateau size string: {size_str}")