import pytest
from src.parsers.instruction_parser import InstructionParser
from src.utils.enums import Instruction

def test_valid_instructions():
    instrs = InstructionParser.parse("LMR")
    assert instrs == [Instruction.LEFT, Instruction.MOVE, Instruction.RIGHT]

def test_invalid_instructions_are_skipped():
    instrs = InstructionParser.parse("LMRXZ")
    assert instrs == [Instruction.LEFT, Instruction.MOVE, Instruction.RIGHT]
