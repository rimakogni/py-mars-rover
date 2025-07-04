from src.utils.enums import Instruction

class InstructionParser:
    @staticmethod
    def parse(instructions_str:str) -> list[Instruction]:
        result = []

        for char in instructions_str:
            try:
                if char in Instruction:
                 result.append(Instruction(char))
            except ValueError:
               # ignore wrong values
               pass
        return result

