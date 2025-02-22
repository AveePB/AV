"""
MotorControl class for controlling GPIO pins.

This module defines a class that is responsible for controlling 
the movements of car, while keeping additional information about their state.
"""

import RPi.GPIO as GPIO
from enum import Enum
from car.motors import Motor
from car.constants import *

class Movement(Enum):
    """
    Enum representing the possible movement of the car.
    - MOVE_TOP_LEFT: Moves the car top-left.
    - MOVE_TOP_RIGHT: Moves the car top-right.
    - MOVE_BOTTOM_LEFT: Moves the car bottom-left.
    - MOVE_BOTTOM_RIGHT: Moves the car bottom-right.

    - MOVE_FORWARD: Moves the car forward.
    - MOVE_BACKWARD: Moves the car backward.
    - MOVE_LEFT: Moves the car left.
    - MOVE_RIGHT: Moves the car right.

    - TURN_RIGHT: Turns the car to the right.
    - TURN_LEFT: Turns the car to the left.
    - NONE: Car is stopped.
    """

    MOVE_TOP_LEFT = 0
    MOVE_TOP_RIGHT = 1
    MOVE_BOTTOM_LEFT = 2
    MOVE_BOTTOM_RIGHT = 3

    MOVE_FORWARD = 4
    MOVE_BACKWARD = 5
    MOVE_LEFT = 6
    MOVE_RIGHT = 7

    TURN_RIGHT = 8
    TURN_LEFT = 9
    NONE = 10

class MotorControl:
    """
    Class to control a motor using GPIO pins.
    
    Attributes:
        __movement (Movement): Current movement of the car.
        __FL_motor (Motor): Front left motor.
        __FR_motor (Motor): Front right motor.
        __BL_motor (Motor): Back left motor.
        __BR_motor (Motor): Back right motor.
    """

    def __init__(self):
        """
        Initializes the motor control with constant GPIO pins.
        """

        self.__movement = Movement.NONE
        self.__FL_motor = Motor(F_ENB, F_IN3, F_IN4)
        self.__FR_motor = Motor(F_ENA, F_IN1, F_IN2)
        #self.__FR_motor = Motor()
        #self.__BL_motor = Motor()
        #self.__BR_motor = Motor()

    def moveForward(self):
        """
        Function changes movement of car to forward.
        """

        self.__FL_motor.forward()