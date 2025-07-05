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
        # Adds the rover to the list of managed rovers if position is free if is not raise ValueError.
        # Returns the created Rover instance.
        if not self.is_position_free(position):
            raise ValueError(f"Cannot place rover at occupied position: ({position.x}, {position.y})")

        rover = Rover(position)
        self.rovers.append(rover)
        return rover

    def execute_instructions(self, rover_index: int, instructions):
        # Retrieves the rover by its index in the list.
        # Executes a list of instructions for this rover.
        # Ensures the rover operates within plateau boundaries.
        # Returns the rover's final Position after executing instructions.
        rover = self.rovers[rover_index]
        rover.execute_instructions(instructions, self)
        return rover.position
    
    def is_position_free(self, position: Position) -> bool:
    #Checks whether the given position is unoccupied by any rover.
        for rover in self.rovers:
            if (rover.position.x == position.x
                and rover.position.y == position.y):
                return False
        return True
    def move_rover(self, rover: Rover, new_position: Position):
    
    # Attempts to move the given rover to new_position.
    # Raises ValueError if the new position is occupied.
    
        if not self.plateau.is_within_bounds(new_position):
            raise ValueError("Rover cannot move outside the plateau boundaries.")

        # Allow rover to stay in its own position
        for other_rover in self.rovers:
            if other_rover is not rover:
                if (other_rover.position.x == new_position.x and other_rover.position.y == new_position.y):
                    raise ValueError(
                        f"Collision detected at ({new_position.x}, {new_position.y})"
                    )

        rover.position = new_position