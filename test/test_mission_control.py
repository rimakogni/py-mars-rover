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
        Instruction.LEFT,
        Instruction.MOVE,
        Instruction.LEFT,
        Instruction.MOVE
    ]
    
    final_pos = mission_control.execute_instructions(0, instructions)
    
    assert final_pos.x == 0
    assert final_pos.y == 1
    assert final_pos.direction == CompassDirection.S
