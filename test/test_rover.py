import pytest
from src.logic.rover import Rover
from src.logic.plateau import Plateau
from src.utils.models import Position, PlateauSize
from src.utils.enums import CompassDirection, Instruction

def test_turn_left_from_north():
    # Arrange
    start_pos = Position(0, 0, CompassDirection.N)
    rover = Rover(start_pos)
    
    # Act
    rover.turn_left()
    
    # Assert
    assert rover.position.direction == CompassDirection.W

def test_turn_right_from_north():
    start_pos = Position(0, 0, CompassDirection.N)
    rover = Rover(start_pos)
    
    rover.turn_right()
    
    assert rover.position.direction == CompassDirection.E

def test_move_forward_north_within_bounds():
    # Plateau is 5x5
    plateau = Plateau(PlateauSize(5, 5))
    start_pos = Position(2, 2, CompassDirection.N)
    rover = Rover(start_pos)
    
    rover.move_forward(plateau)
    
    assert rover.position.x == 2
    assert rover.position.y == 3
    assert rover.position.direction == CompassDirection.N

def test_move_forward_out_of_bounds_raises():
    plateau = Plateau(PlateauSize(5, 5))
    start_pos = Position(5, 5, CompassDirection.N)
    rover = Rover(start_pos)
    
    with pytest.raises(ValueError):
        rover.move_forward(plateau)

def test_execute_instructions_turns_and_moves():
    plateau = Plateau(PlateauSize(5, 5))
    start_pos = Position(1, 2, CompassDirection.N)
    rover = Rover(start_pos)
    
    instructions = [
        Instruction.LEFT,
        Instruction.MOVE,
        Instruction.LEFT,
        Instruction.MOVE
    ]
    
    rover.execute_instructions(instructions, plateau)
    
    assert rover.position.x == 0
    assert rover.position.y == 1
    assert rover.position.direction == CompassDirection.S
