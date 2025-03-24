from gpiozero import Motor
from enum import Enum
from vehicle.consts import *

MOTOR_SPEED = 0.5

class MotorDirection(Enum):
    NONE = 0
    FORWARD = 1
    BACKWARD = -1

class Maneuver(Enum):
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

class MotorSystem:

    def __init__(self):
        """
        Constructor responsible for initializing all motors.
        """
        self.__FL_motor = Motor(forward=F_IN3, backward=F_IN4, enable=F_ENB)
        self.__FR_motor = Motor(forward=F_IN1, backward=F_IN2, enable=F_ENA)
        self.__BL_motor = Motor(forward=B_IN1, backward=B_IN2, enable=B_ENA)
        self.__BR_motor = Motor(forward=B_IN3, backward=B_IN4, enable=B_ENB)

        self.__FL_mdir = MotorDirection.NONE
        self.__FR_mdir = MotorDirection.NONE
        self.__BL_mdir = MotorDirection.NONE
        self.__BR_mdir = MotorDirection.NONE

        self.__maneuver = Maneuver.STOP

    def go_forward(self):
        self.__maneuver = Maneuver.GO_FORWARD

        self.__FL_motor.forward(MOTOR_SPEED)
        self.__FR_motor.forward(MOTOR_SPEED)
        self.__BL_motor.forward(MOTOR_SPEED)
        self.__BR_motor.forward(MOTOR_SPEED)
