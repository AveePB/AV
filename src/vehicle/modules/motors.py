from gpiozero import Motor
from enum import Enum
from vehicle.consts import MOTOR_SPEED, F_ENA, F_ENB, F_IN1, F_IN2, F_IN3, F_IN4, B_ENA, B_ENB, B_IN1, B_IN2, B_IN3, B_IN4

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

class DCMotor(Motor):
    """
        Class used to control motor's spin direction and speed based on two input pins and one pwm pin. 
    """

    def __init__(self, forward, backward, enable):
        """
            Constructor responsible for correct initialization of motor.

            Args:
                forward (int): first input pin (in1)
                backward (int): second input pin (in2)
                enable (int): pwm input pin (en) 
        """
        super().__init__(forward=forward, backward=backward, enable=enable)

        self.__directon = MotorDirection.NONE

    def forward(self):
        """
            Updates motor's spin direction to forward.
        """
        if (self.__directon == MotorDirection.FORWARD): return

        super().forward(MOTOR_SPEED)
        self.__directon = MotorDirection.FORWARD

    def backward(self):
        """
            Updates motor's spin direction to backward.
        """
        if (self.__directon == MotorDirection.BACKWARD): return

        super().backward(MOTOR_SPEED)
        self.__directon = MotorDirection.BACKWARD

    def stop(self):
        """
            Updates motor's spin direction to none.
        """
        if (self.__directon == MotorDirection.NONE): return

        super().stop()
        self.__directon = MotorDirection.NONE

class MotorSystem:
    """
        Motor system is used to force the car to perform certain maneuvers.
    """

    def __init__(self):
        """
        Constructor responsible for initializing all motors.
        """
        self.__FL_motor = DCMotor(forward=F_IN3, backward=F_IN4, enable=F_ENB)
        self.__FR_motor = DCMotor(forward=F_IN1, backward=F_IN2, enable=F_ENA)
        self.__BL_motor = DCMotor(forward=B_IN1, backward=B_IN2, enable=B_ENA)
        self.__BR_motor = DCMotor(forward=B_IN3, backward=B_IN4, enable=B_ENB)

        self.__maneuver = Maneuver.STOP

    """
    Getter function, used to access private maneuver field value.
    """
    def get_maneuver(self):
        return self.__maneuver

    def stop(self):
        """
            Changes the motors maneuver to stop.
        """
        if (self.__maneuver == Maneuver.STOP): return

        self.__FL_motor.stop()
        self.__FR_motor.stop()
        self.__BL_motor.stop()
        self.__BR_motor.stop()
        self.__maneuver = Maneuver.STOP

    def go_forward(self):
        """
            Changes the motors maneuver to forward.
        """
        if (self.__maneuver == Maneuver.GO_FORWARD): return

        self.__FL_motor.forward()
        self.__FR_motor.forward()
        self.__BL_motor.forward()
        self.__BR_motor.forward()
        self.__maneuver = Maneuver.GO_FORWARD
    
    def go_backward(self):
        """
            Changes the motors maneuver to backward.
        """
        if (self.__maneuver == Maneuver.GO_BACKWARD): return

        self.__FL_motor.backward()
        self.__FR_motor.backward()
        self.__BL_motor.backward()
        self.__BR_motor.backward()
        self.__maneuver = Maneuver.GO_BACKWARD

    def go_left(self):
        """
            Changes the motors maneuver to left.
        """
        if (self.__maneuver == Maneuver.GO_LEFT): return

        self.__FL_motor.backward()
        self.__FR_motor.forward()
        self.__BL_motor.forward()
        self.__BR_motor.backward()

        self.__maneuver = Maneuver.GO_LEFT
    
    def go_right(self):
        """
            Changes the motors maneuver to right.
        """
        if (self.__maneuver == Maneuver.GO_RIGHT): return
        
        self.__FL_motor.forward()
        self.__FR_motor.backward()
        self.__BL_motor.backward()
        self.__BR_motor.forward()

        self.__maneuver = Maneuver.GO_RIGHT

    def go_top_left(self):
        """
            Changes the motors maneuver to top left.
        """
        if (self.__maneuver == Maneuver.GO_TOP_LEFT): return
        
        self.__FL_motor.stop()
        self.__FR_motor.forward()
        self.__BL_motor.forward()
        self.__BR_motor.stop()

        self.__maneuver = Maneuver.GO_TOP_LEFT
    
    def go_top_right(self):
        """
            Changes the motors maneuver to top right.
        """
        if (self.__maneuver == Maneuver.GO_TOP_RIGHT): return
        
        self.__FL_motor.forward()
        self.__FR_motor.stop()
        self.__BL_motor.stop()
        self.__BR_motor.forward()

        self.__maneuver = Maneuver.GO_TOP_RIGHT

    def go_bottom_left(self):
        """
            Changes the motors maneuver to bottom left.
        """
        if (self.__maneuver == Maneuver.GO_BOTTOM_LEFT): return
        
        self.__FL_motor.backward()
        self.__FR_motor.stop()
        self.__BL_motor.stop()
        self.__BR_motor.backward()

        self.__maneuver = Maneuver.GO_BOTTOM_LEFT

    def go_bottom_right(self):
        """
            Changes the motors maneuver to bottom right.
        """
        if (self.__maneuver == Maneuver.GO_BOTTOM_RIGHT): return
        
        self.__FL_motor.stop()
        self.__FR_motor.backward()
        self.__BL_motor.backward()
        self.__BR_motor.stop()

        self.__maneuver = Maneuver.GO_BOTTOM_RIGHT

    def turn_left(self):
        """
            Changes the motors maneuver to turn left.
        """
        if (self.__maneuver == Maneuver.TURN_LEFT): return
        
        self.__FL_motor.backward()
        self.__FR_motor.forward()
        self.__BL_motor.backward()
        self.__BR_motor.forward()

        self.__maneuver = Maneuver.TURN_LEFT
    
    def turn_right(self):
        """
            Changes the motors maneuver to turn right.
        """
        if (self.__maneuver == Maneuver.TURN_RIGHT): return
        
        self.__FL_motor.forward()
        self.__FR_motor.backward()
        self.__BL_motor.forward()
        self.__BR_motor.backward()

        self.__maneuver = Maneuver.TURN_RIGHT
