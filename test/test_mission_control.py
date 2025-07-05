import pytest
from src.logic.mission_control import MissionControl
from src.logic.plateau import Plateau
from src.utils.models import Position, PlateauSize
from src.utils.enums import CompassDirection, Instruction

def test_add_rover_adds_rover_to_list():
    plateau = Plateau(PlateauSize(5, 5))
    mission_control = MissionControl(plateau)
    
    initial_count = len(mission_control.rovers)
    
    pos = Position(1, 2, CompassDirection.N)
    rover = mission_control.add_rover(pos)
    
    assert len(mission_control.rovers) == initial_count + 1
    assert mission_control.rovers[0] == rover
    assert rover.position == pos

def test_execute_instructions_changes_rover_position():
    plateau = Plateau(PlateauSize(5, 5))
    mission_control = MissionControl(plateau)
    
    pos = Position(1, 2, CompassDirection.N)
    mission_control.add_rover(pos)
    
    instructions = [
        Instruction.LEFT,     # N → W
        Instruction.MOVE,     # (1,2) → (0,2)
        Instruction.LEFT,     # W → S
        Instruction.MOVE      # (0,2) → (0,1)
    ]
    
    final_pos = mission_control.execute_instructions(0, instructions)
    
    assert final_pos.x == 0
    assert final_pos.y == 1
    assert final_pos.direction == CompassDirection.S

def test_add_rover_to_occupied_position_raises():
    plateau = Plateau(PlateauSize(5, 5))
    mission_control = MissionControl(plateau)

    pos1 = Position(2, 2, CompassDirection.N)
    pos2 = Position(2, 2, CompassDirection.E)

    mission_control.add_rover(pos1)

    # Adding another rover in same position should fail
    with pytest.raises(ValueError):
        mission_control.add_rover(pos2)

def test_move_rover_into_occupied_position_raises():
    plateau = Plateau(PlateauSize(5, 5))
    mission_control = MissionControl(plateau)

    # Rover 1 starts at (1,1) facing east
    pos1 = Position(1, 1, CompassDirection.E)
    mission_control.add_rover(pos1)

    # Rover 2 starts at (2,1) facing north
    pos2 = Position(2, 1, CompassDirection.N)
    mission_control.add_rover(pos2)

    # Rover 1 moves east into (2,1)
    instructions = [
        Instruction.MOVE
    ]

    with pytest.raises(ValueError):
        mission_control.execute_instructions(0, instructions)

