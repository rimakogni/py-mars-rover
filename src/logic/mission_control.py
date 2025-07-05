from src.logic.plateau import Plateau
from src.logic.rover import Rover
from src.utils.models import Position

class MissionControl:
    def __init__(self, plateau: Plateau):
        # Initializes MissionControl with a Plateau instance.
        # Keeps track of all rovers deployed on this plateau.
        self.plateau = plateau
        self.rovers = []

    def add_rover(self, position: Position):
        # Creates a new Rover at the specified position.
        # Adds the rover to the list of managed rovers.
        # Returns the created Rover instance.
        rover = Rover(position)
        self.rovers.append(rover)
        return rover

    def execute_instructions(self, rover_index: int, instructions):
        # Retrieves the rover by its index in the list.
        # Executes a list of instructions for this rover.
        # Ensures the rover operates within plateau boundaries.
        # Returns the rover's final Position after executing instructions.
        rover = self.rovers[rover_index]
        rover.execute_instructions(instructions, self.plateau)
        return rover.position