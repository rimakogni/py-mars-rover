import pytest
from src.parsers.plateau_parser import PlateauParser
from src.utils.models import PlateauSize

def test_valid_plateau():
    plateau = PlateauParser.parse("5 5")
    assert plateau == PlateauSize(5, 5)

def test_invalid_plateau_raises():
    with pytest.raises(ValueError):
        PlateauParser.parse("five five")
def test_invalid_long_plateau_raises():
    with pytest.raises(ValueError):
        PlateauParser.parse("6 6 6")