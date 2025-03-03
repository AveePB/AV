"""
Unit tests of MotorControl class.

This module has tests for all movements of car.
It shows how car handles the change of movements.
"""

import unittest
import time
from car.motor_control import MotorControl
from car.gpio import initializeGPIO, cleanUpGPIO

class TestMotorControlFunctions(unittest.TestCase):
    """
    Tests of motor control functions.

    Set of specific scenarios, that test movments of the car.
    It shows how well it performs during pressure.
    """

    TIME = 1 # Movement time (seconds)

    def test_move_forward(self):
        """
        Tests how car moves forwad.
        """
        time.sleep(self.TIME*4)
        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move forward
        driveSystem.moveForward()
        
        print("Car moves forward")
        time.sleep(self.TIME)

        driveSystem.cleanUpPWM()
        cleanUpGPIO()

    def test_move_backward(self):
        """
        Tests how car moves backwad.
        """
        time.sleep(self.TIME*4)
        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move backward
        driveSystem.moveBackward()
        
        print("Car moves backward")
        time.sleep(self.TIME)

        driveSystem.cleanUpPWM()
        cleanUpGPIO()

    def test_move_left(self):
        """
        Tests how car moves left.
        """
        time.sleep(self.TIME*4)
        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move left
        driveSystem.moveLeft()
        
        print("Car moves left")
        time.sleep(self.TIME)

        driveSystem.cleanUpPWM()
        cleanUpGPIO()

    def test_move_right(self):
        """
        Tests how car moves right.
        """
        time.sleep(self.TIME*4)
        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move right
        driveSystem.moveRight()
        
        print("Car moves right")
        time.sleep(self.TIME)

        driveSystem.cleanUpPWM()
        cleanUpGPIO()

    def test_move_top_left(self):
        """
        Tests how car moves top-left.
        """
        time.sleep(self.TIME*4)
        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move top-left
        driveSystem.moveTopLeft()
        
        print("Car moves top-left")
        time.sleep(self.TIME)

        driveSystem.cleanUpPWM()
        cleanUpGPIO()
    
    def test_move_top_right(self):
        """
        Tests how car moves top-right.
        """
        time.sleep(self.TIME*4)
        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move top-right
        driveSystem.moveTopRight()
        
        print("Car moves top-right")
        time.sleep(self.TIME)

        driveSystem.cleanUpPWM()
        cleanUpGPIO()

    def test_move_bottom_left(self):
        """
        Tests how car moves bottom-left.
        """
        time.sleep(self.TIME*4)
        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move bottom-left
        driveSystem.moveBottomLeft()
        
        print("Car moves bottom-left")
        time.sleep(self.TIME)

        driveSystem.cleanUpPWM()
        cleanUpGPIO()

    def test_move_bottom_right(self):
        """
        Tests how car moves bottom-right.
        """
        time.sleep(self.TIME*4)
        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move bottom-right
        driveSystem.moveBottomRight()
        
        print("Car moves bottom-right")
        time.sleep(self.TIME)

        driveSystem.cleanUpPWM()
        cleanUpGPIO()
    
    def test_turn_right(self):
        """
        Tests how car turns right.
        """
        time.sleep(self.TIME*4)
        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Turn right
        driveSystem.turnRight()
        
        print("Car turns right")
        time.sleep(self.TIME)

        driveSystem.cleanUpPWM()
        cleanUpGPIO()
    
    def test_turn_left(self):
        """
        Tests how car turns left.
        """
        time.sleep(self.TIME*4)
        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Turn left
        driveSystem.turnLeft()
        
        print("Car turns left")
        time.sleep(self.TIME)

        driveSystem.cleanUpPWM()
        cleanUpGPIO()

    def test_square(self):
        """
        Tests how car draws square.
        """
        time.sleep(self.TIME*4)
        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move right
        driveSystem.moveRight()
        
        print("Car moves right")
        time.sleep(self.TIME)

        # Move backward
        driveSystem.moveBackward()

        print("Car moves backward")
        time.sleep(self.TIME)

        # Move left
        driveSystem.moveLeft()
        
        print("Car moves left")
        time.sleep(self.TIME)

        # Move forward
        driveSystem.moveForward()

        print("Car moves forward")
        time.sleep(self.TIME)

        driveSystem.cleanUpPWM()
        cleanUpGPIO()

if (__name__ == '__main__'):
    unittest.main()