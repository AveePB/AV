from enum import Enum

class MotorDirection(Enum):
    """
        MotorDirection is an enum multichoice class. It is responsible for representing all possible states of the motor.
    """

    NONE = 0
    FORWARD = 1
    BACKWARD = -1

class Maneuver(Enum):
    """
        Maneuver is an enum multichoice class. It is responsible for representing all possible maneuvers of the car.
    """

    STOP = 0
    GO_FORWARD = 1
    GO_BACKWARD = 2
    GO_LEFT = 3
    GO_RIGHT = 4
    GO_TOP_LEFT = 5
    GO_TOP_RIGHT = 6
    GO_BOTTOM_LEFT = 7
    GO_BOTTOM_RIGHT = 8
    TURN_LEFT = 9
    TURN_RIGHT = 10