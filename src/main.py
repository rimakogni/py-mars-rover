from src.logic.mission_control import MissionControl
from src.logic.plateau import Plateau
from src.utils.models import PlateauSize, Position
from src.parsers.plateau_parser import PlateauParser
from src.parsers.position_parser import PositionParser
from src.parsers.instruction_parser import InstructionParser

def main():
    plateau_input = "5 5"
    position_input = "1 2 N"
    instructions_input = "LMLMMLLMMMR"

    # parse inputs
    plateau_size = PlateauParser.parse(plateau_input)
    position = PositionParser.parse(position_input)
    instructions = InstructionParser.parse(instructions_input)

    # create plateau and mission control
    plateau = Plateau(plateau_size)
    mission_control = MissionControl(plateau)

    # add rover
    rover = mission_control.add_rover(position)
    
    # execute instructions
    final_position = mission_control.execute_instructions(0, instructions)

    print(f"{final_position.x} {final_position.y} {final_position.direction.value}")


if __name__ == "__main__":
    main()