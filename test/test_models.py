import pytest
from src.utils.models import PlateauSize, Position
from src.utils.enums import CompassDirection

# Tests PlateauSize

def test_plateau_size_valid_creation():
    plateau = PlateauSize(width=55, height=55)
    assert plateau.width == 55
    assert plateau.height == 55

def test_plateau_size_negative_width():
    with pytest.raises(ValueError, match="width must be non-negative"):
        PlateauSize(width=-1, height=5)

def test_plateau_size_negative_height():
    with pytest.raises(ValueError, match="height must be non-negative"):
        PlateauSize(width=3, height=-2)

def test_plateau_size_width_exceeds_maximum():
    with pytest.raises(ValueError, match="width exceeds maximum"):
        PlateauSize(width=60, height=5)

def test_plateau_size_height_exceeds_maximum():
    with pytest.raises(ValueError, match="height exceeds maximum"):
        PlateauSize(width=3, height=60)

def test_plateau_size_equality():
    p1 = PlateauSize(5, 7)
    p2 = PlateauSize(5, 7)
    assert p1 == p2

# Tests Position

def test_position_valid_creation():
    pos = Position(x=10, y=20, direction=CompassDirection.N)
    assert pos.x == 10
    assert pos.y == 20
    assert pos.direction == CompassDirection.N

def test_position_negative_x():
    with pytest.raises(ValueError, match="x must be non-negative"):
        Position(x=-5, y=2, direction=CompassDirection.N)

def test_position_negative_y():
    with pytest.raises(ValueError, match="y must be non-negative"):
        Position(x=3, y=-4, direction=CompassDirection.W)

def test_position_x_exceeds_maximum():
    with pytest.raises(ValueError, match="x exceeds maximum"):
        Position(x=2000, y=5, direction=CompassDirection.S)

def test_position_y_exceeds_maximum():
    with pytest.raises(ValueError, match="y exceeds maximum"):
        Position(x=5, y=2000, direction=CompassDirection.E)

def test_position_invalid_direction_type():
    with pytest.raises(ValueError, match="Invalid direction"):
        Position(x=1, y=2, direction="Z")

def test_position_equality():
    pos1 = Position(3, 4, CompassDirection.N)
    pos2 = Position(3, 4, CompassDirection.N)
    assert pos1 == pos2

def test_position_direction_type():
    pos = Position(1, 2, direction=CompassDirection.W)
    assert isinstance(pos.direction, CompassDirection)
