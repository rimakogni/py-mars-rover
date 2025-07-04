from src.utils.enums import CompassDirection

class CompassParser:
    @staticmethod
    def parse(direction_str: str) -> CompassDirection:
        """
        Convierte un string como "N" en CompassDirection.N.
        Lanza ValueError si el string no es válido.
        """
        try:
            return CompassDirection(direction_str)
        except ValueError:
            raise ValueError(f"Invalid compass direction: {direction_str}")