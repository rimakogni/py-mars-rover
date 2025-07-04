import pytest
from src.utils.enums import CompassDirection, Instruction

# Tests CompassDirection

def test_compass_direction_values():
    assert CompassDirection.N.value == "N"
    assert CompassDirection.E.value == "E"
    assert CompassDirection.S.value == "S"
    assert CompassDirection.W.value == "W"

def test_compass_direction_names():
    assert CompassDirection.N.name == "N"
    assert CompassDirection.E.name == "E"
    assert CompassDirection.S.name == "S"
    assert CompassDirection.W.name == "W"

def test_compass_direction_comparisons():
    assert CompassDirection.N == CompassDirection.N
    assert CompassDirection.E != CompassDirection.S

def test_compass_direction_invalid_value():
    with pytest.raises(ValueError):
        CompassDirection("Z")

# Tests Instruction

def test_instruction_values():
    assert Instruction.LEFT.value == "L"
    assert Instruction.RIGHT.value == "R"
    assert Instruction.MOVE.value == "M"

def test_instruction_names():
    assert Instruction.LEFT.name == "LEFT"
    assert Instruction.RIGHT.name == "RIGHT"
    assert Instruction.MOVE.name == "MOVE"

def test_instruction_comparisons():
    assert Instruction.LEFT == Instruction.LEFT
    assert Instruction.RIGHT != Instruction.MOVE

def test_instruction_invalid_value():
    with pytest.raises(ValueError):
        Instruction("X")
