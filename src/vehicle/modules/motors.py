from gpiozero import Device, Motor
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

class DCMotor(Motor):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

        self.__directon = MotorDirection.NONE

    def moveForward(self):
        if (self.__directon == MotorDirection.FORWARD): return

        self.forward(MOTOR_SPEED)
        self.__directon = MotorDirection.FORWARD

    def moveBackward(self):
        if (self.__directon == MotorDirection.BACKWARD): return

        self.backward(MOTOR_SPEED)
        self.__directon = MotorDirection.BACKWARD

    def stopMovement(self):
        if (self.__directon == MotorDirection.NONE): return

        self.stop()
        self.__directon = MotorDirection.NONE

class MotorSystem:

    def __init__(self):
        """
        Constructor responsible for initializing all motors.
        """
        self.__FL_motor = DCMotor(forward=F_IN3, backward=F_IN4, enable=F_ENB, pwm=True, pin_factory=Device.pin_factory)
        self.__FR_motor = DCMotor(forward=F_IN1, backward=F_IN2, enable=F_ENA, pwm=True, pin_factory=Device.pin_factory)
        self.__BL_motor = DCMotor(forward=B_IN1, backward=B_IN2, enable=B_ENA, pwm=True, pin_factory=Device.pin_factory)
        self.__BR_motor = DCMotor(forward=B_IN3, backward=B_IN4, enable=B_ENB, pwm=True, pin_factory=Device.pin_factory)

        self.__maneuver = Maneuver.STOP

    def go_forward(self):
        if (self.__maneuver == Maneuver.GO_FORWARD): return

        self.__FL_motor.moveForward()
        self.__FR_motor.moveForward()
        self.__BL_motor.moveForward()
        self.__BR_motor.moveForward()
        self.__maneuver = Maneuver.GO_FORWARD

