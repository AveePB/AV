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

class DCMotor(Motor):

    def __init__(self, forward, backward, enable):
        """
        Constructor responsible for correct initialization of motor.
        """
        super().__init__(forward=forward, backward=backward, enable=enable)

        self.__directon = MotorDirection.NONE

    def moveForward(self):
        """
            Updates motor's spin direction to forward.
        """
        if (self.__directon == MotorDirection.FORWARD): return

        self.forward(MOTOR_SPEED)
        self.__directon = MotorDirection.FORWARD

    def moveBackward(self):
        """
            Updates motor's spin direction to backward.
        """
        if (self.__directon == MotorDirection.BACKWARD): return

        self.backward(MOTOR_SPEED)
        self.__directon = MotorDirection.BACKWARD

    def stopMovement(self):
        """
            Updates motor's spin direction to none.
        """
        if (self.__directon == MotorDirection.NONE): return

        self.stop()
        self.__directon = MotorDirection.NONE

class MotorSystem:

    def __init__(self):
        """
        Constructor responsible for initializing all motors.
        """
        self.__FL_motor = DCMotor(forward=F_IN3, backward=F_IN4, enable=F_ENB)
        self.__FR_motor = DCMotor(forward=F_IN1, backward=F_IN2, enable=F_ENA)
        self.__BL_motor = DCMotor(forward=B_IN1, backward=B_IN2, enable=B_ENA)
        self.__BR_motor = DCMotor(forward=B_IN3, backward=B_IN4, enable=B_ENB)

        self.__maneuver = Maneuver.STOP

    def stop(self):
        """
            Changes the motors maneuver to stop.
        """
        if (self.__maneuver == Maneuver.STOP): return

        self.__FL_motor.stopMovement()
        self.__FR_motor.stopMovement()
        self.__BL_motor.stopMovement()
        self.__BR_motor.stopMovement()
        self.__maneuver = Maneuver.STOP

    def go_forward(self):
        """
            Changes the motors maneuver to forward.
        """
        if (self.__maneuver == Maneuver.GO_FORWARD): return

        self.__FL_motor.moveForward()
        self.__FR_motor.moveForward()
        self.__BL_motor.moveForward()
        self.__BR_motor.moveForward()
        self.__maneuver = Maneuver.GO_FORWARD
    
    def go_backward(self):
        """
            Changes the motors maneuver to backward.
        """
        if (self.__maneuver == Maneuver.GO_BACKWARD): return

        self.__FL_motor.moveBackward()
        self.__FR_motor.moveBackward()
        self.__BL_motor.moveBackward()
        self.__BR_motor.moveBackward()
        self.__maneuver = Maneuver.GO_BACKWARD

    def go_left(self):
        """
            Changes the motors maneuver to left.
        """
        if (self.__maneuver == Maneuver.GO_LEFT): return

        self.__FL_motor.moveForward()
        self.__FR_motor.moveBackward()
        self.__BL_motor.moveBackward()
        self.__BR_motor.moveForward()
        self.__maneuver = Maneuver.GO_LEFT
    
    def go_right(self):
        """
            Changes the motors maneuver to right.
        """
        if (self.__maneuver == Maneuver.GO_RIGHT): return

        self.__FL_motor.moveBackward()
        self.__FR_motor.moveForward()
        self.__BL_motor.moveForward()
        self.__BR_motor.moveBackward()
        self.__maneuver = Maneuver.GO_RIGHT

    

