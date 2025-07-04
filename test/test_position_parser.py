import pytest
from src.parsers.position_parser import PositionParser 
from src.utils.models import Position
from src.utils.enums import CompassDirection

def test_valid_position():
    pos = PositionParser.parse("3 4 N")
    assert pos == Position(3, 4, CompassDirection.N)

def test_invalid_position_raises():
    with pytest.raises(ValueError):
        PositionParser.parse("3 four N")