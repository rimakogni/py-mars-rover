import pytest
from src.logic.plateau import Plateau
from src.utils.models import PlateauSize, Position
from src.utils.enums import CompassDirection

def test_position_within_bounds():
    plateau = Plateau(PlateauSize(5, 5))
    pos = Position(3, 4, CompassDirection.N)
    
    assert plateau.is_within_bounds(pos) == True

def test_position_on_edge_is_within_bounds():
    plateau = Plateau(PlateauSize(5, 5))
    pos = Position(5, 5, CompassDirection.E)
    
    assert plateau.is_within_bounds(pos) == True
