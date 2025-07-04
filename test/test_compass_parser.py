import pytest
from src.parsers.compass_parser import CompassParser
from src.utils.enums import CompassDirection

def test_valid_direction():
    assert CompassParser.parse("N") == CompassDirection.N
    
def test_invalid_direction():
    with pytest.raises(ValueError):
        CompassParser.parse("Q")