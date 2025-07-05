
from src.logic.plateau import Plateau
from src.utils.models import Position
from src.utils.enums import CompassDirection, Instruction

class Rover:

    # Maps each compass direction to the new direction when turning left
    LEFT_TURNS = {
        'N': 'W',
        'W': 'S',
        'S': 'E',
        'E': 'N'
    }

    # Maps each compass direction to the new direction when turning right
    RIGHT_TURNS = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }

    # Defines the (dx, dy) movement for moving forward in each compass direction
    FORWARD_MOVE = {
        'N': (0, 1),
        'S': (0, -1),
        'E': (1, 0),
        'W': (-1, 0)
    }

    def __init__(self, position: Position):
        """
        Initializes the Rover with a starting Position.
        
        :param position: Position object representing the rover's starting location and direction.
        """
        self.position = position

    def turn_left(self):
        """
        Rotates the rover 90 degrees to the left (counter-clockwise).
        Updates the rover's direction accordingly.
        """
        dir_value = self.position.direction.value
        new_dir = self.LEFT_TURNS[dir_value]
        self.position.direction = CompassDirection(new_dir)

    def turn_right(self):
        """
        Rotates the rover 90 degrees to the right (clockwise).
        Updates the rover's direction accordingly.
        """
        dir_value = self.position.direction.value
        new_dir = self.RIGHT_TURNS[dir_value]
        self.position.direction = CompassDirection(new_dir)

    def move_forward(self, plateau: Plateau):
        """
        Moves the rover one unit forward in the current direction.
        Checks if the new position is still within the plateau boundaries.
        Raises a ValueError if the move would go outside the plateau.
        
        :param plateau: Plateau object to validate movement boundaries.
        """
        dx, dy = self.FORWARD_MOVE[self.position.direction.value]
        new_x = self.position.x + dx
        new_y = self.position.y + dy
        new_pos = Position(new_x, new_y, self.position.direction)

        if plateau.is_within_bounds(new_pos):
            self.position = new_pos
        else:
            raise ValueError("Rover cannot move outside the plateau boundaries.")

    def execute_instructions(self, instructions, plateau):
        """
        Executes a list of instructions for the rover.
        Processes each instruction sequentially, modifying the rover's state.

        :param instructions: List of Instruction enums to execute.
        :param plateau: Plateau object for boundary checks during movement.
        """
        for instr in instructions:
            if instr == Instruction.LEFT:
                self.turn_left()
            elif instr == Instruction.RIGHT:
                self.turn_right()
            elif instr == Instruction.MOVE:
                self.move_forward(plateau)
