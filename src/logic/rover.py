
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
       
        # Initializes the Rover with a starting Position.
        #
        # :param position: Position object representing the rover's starting location and direction.
        
        self.position = position

    def turn_left(self):
        
        # Rotates the rover to the left .
        # Updates the rover's direction accordingly.
        
        dir_value = self.position.direction.value
        new_dir = self.LEFT_TURNS[dir_value]
        self.position.direction = CompassDirection(new_dir)

    def turn_right(self):
        
        # Rotates the rover to the right.
        # Updates the rover's direction accordingly.
        
        dir_value = self.position.direction.value
        new_dir = self.RIGHT_TURNS[dir_value]
        self.position.direction = CompassDirection(new_dir)

    def move_forward(self, mission_control):
        
        # Requests MissionControl to move the rover forward by one unit.
        # MissionControl handles boundary checks and collision detection.
        #
        # :param mission_control: MissionControl instance that manages the plateau and rovers.
        
        dx, dy = self.FORWARD_MOVE[self.position.direction.value]
        new_x = self.position.x + dx
        new_y = self.position.y + dy
        new_pos = Position(new_x, new_y, self.position.direction)

        # Delegate movement and collision check to MissionControl
        mission_control.move_rover(self, new_pos)

    def execute_instructions(self, instructions, mission_control):
        
        # Executes a list of instructions for the rover.
        # Processes each instruction sequentially, modifying the rover's state.
        #
        # :param instructions: List of Instruction enums to execute.
        # :param mission_control: MissionControl instance that manages movement and collisions.
        
        for instr in instructions:
            if instr == Instruction.LEFT:
                self.turn_left()
            elif instr == Instruction.RIGHT:
                self.turn_right()
            elif instr == Instruction.MOVE:
                self.move_forward(mission_control)
