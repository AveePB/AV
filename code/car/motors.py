"""
Motor class for controlling GPIO pins.

This module defines a class that is responsible for controlling 
the motors, while keeping additional information about their state.
"""

import RPi.GPIO as GPIO
from enum import Enum
from car.constants import MOTOR_PWM, MOTOR_SPEED

class Direction(Enum):
    """
    Enum representing the possible movement directions of the motor.
    - FORWARD: Moves the motor forward.
    - BACKWARD: Moves the motor backward.
    - NONE: Motor is stopped.
    """
    FORWARD = 1
    BACKWARD = -1
    NONE = 0

class Motor:
    """
    Class to control a motor using GPIO pins.
    
    Attributes:
        __direction (Direction): Current direction of the motor.
        __pwm (GPIO.PWM): Object controlling motor by PWM.
        __en (int): GPIO pin connected to the motor driver enable pin.
        __in1 (int): GPIO pin connected to the motor driver input 1.
        __in2 (int): GPIO pin connected to the motor driver input 2.
    """

    def __init__(self, en: int, in1: int, in2: int):
        """
        Initializes the motor with given GPIO pins.
        
        Args:
            en (int): The enable pin for controlling motor speed (PWM capable).
            in1 (int): The first control pin for direction.
            in2 (int): The second control pin for direction.
        """
        
        self.__direction = Direction.NONE  # Initially, the motor is stopped
        self.__pwm = GPIO.PWM(en, MOTOR_PWM)
        self.__pwm.start(0)

        self.__en = en
        self.__in1 = in1
        self.__in2 = in2

    def __del__(self):
        """
            Destroys and stops the motor.
        """

        self.__pwm.stop()

    def forward(self):
        """
        Function changes motor directory to forward.
        """

        if (self.__direction is Direction.FORWARD): return

        # Update input pins
        self.__direction = Direction.FORWARD
        GPIO.output(self.__in1, GPIO.HIGH)
        GPIO.output(self.__in2, GPIO.LOW)

        self.__pwm.ChangeDutyCycle(MOTOR_SPEED)

    def backward(self):
        """
        Function changes motor directory to backward.
        """

        if (self.__direction is Direction.BACKWARD): return

        # Update input pins
        self.__direction = Direction.BACKWARD
        GPIO.output(self.__in1, GPIO.LOW)
        GPIO.output(self.__in2, GPIO.HIGH)

        self.__pwm.ChangeDutyCycle(MOTOR_SPEED)


    def stop(self):
        """
        Function changes motor directory to none.
        """

        if (self.__direction is Direction.NONE): return

        # Update input pins
        self.__direction = Direction.NONE
        GPIO.output(self.__in1, GPIO.LOW)
        GPIO.output(self.__in2, GPIO.LOW)

        self.__pwm.ChangeDutyCycle(0)

    def getDirection(self) -> Direction:
        """
        Getter method that returns motor's direction.
        """

        return self.__direction