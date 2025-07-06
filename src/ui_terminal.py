from src.parsers.plateau_parser import PlateauParser
from src.parsers.position_parser import PositionParser
from src.parsers.instruction_parser import InstructionParser
from src.logic.plateau import Plateau
from src.logic.mission_control import MissionControl

def run_terminal_ui():
    print("=== Mars Rover Terminal UI ===")

    # Prompt user for inputs
    plateau_input = input("Enter plateau size (e.g. 5 5): ")
    position_input = input("Enter rover position (e.g. 1 2 N): ")
    instructions_input = input("Enter instructions (e.g. LMLMLMLMM): ")

    # Parse inputs
    plateau_size = PlateauParser.parse(plateau_input)
    position = PositionParser.parse(position_input)
    instructions = InstructionParser.parse(instructions_input)

    # Create plateau and mission control
    plateau = Plateau(plateau_size)
    mission_control = MissionControl(plateau)

    # Add rover and execute instructions
    mission_control.add_rover(position)
    final_pos = mission_control.execute_instructions(0, instructions)

    # Show result
    print(f"Rover final position: {final_pos.x} {final_pos.y} {final_pos.direction.value}")

if __name__ == "__main__":
    run_terminal_ui()