from src.logic.mission_control import MissionControl
from src.logic.plateau import Plateau
from src.utils.models import PlateauSize, Position
from src.parsers.plateau_parser import PlateauParser
from src.parsers.position_parser import PositionParser
from src.parsers.instruction_parser import InstructionParser

def test_mars_rover_integration():
    plateau_input = "5 5"
    position_input = "1 2 N"
    instructions_input = "LMLMMLLMMMR"

    # parse inputs
    plateau_size = PlateauParser.parse(plateau_input)
    position = PositionParser.parse(position_input)
    instructions = InstructionParser.parse(instructions_input)

    # run logic
    plateau = Plateau(plateau_size)
    mission_control = MissionControl(plateau)
    mission_control.add_rover(position)
    final_pos = mission_control.execute_instructions(0, instructions)

    assert (final_pos.x, final_pos.y, final_pos.direction.value) == (0, 3, "E")