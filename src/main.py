

from src.parsers.instruction_parser import InstructionParser
from src.parsers.position_parser import PositionParser
from src.parsers.plateau_parser import PlateauParser


def main():
# 5 5 ->PlateauSize
# 1 2 N -> Position
# LMLMMLLMMMR -> list(Instructions)

    plateau_size_input = '5 5'
    position_input = '1 2 N'
    moves_input = 'LMLMMLLMMMR'

    size = PlateauParser.parse(plateau_size_input)
    position = PositionParser.parse(position_input)
    instructions = InstructionParser.parse(moves_input)

    print('----------- RESULTS -----------')
    print()
    print(f'PlateauSize: {size}')
    print()
    print(f'Position: {position}')
    print()
    print(f'Instructions: {[i.name for i in instructions]}')
    print()
    print('-------------------------------')
 
if __name__ == "__main__":
    main()