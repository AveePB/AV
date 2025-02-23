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

        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move forward
        driveSystem.moveForward()
        
        print("Car moves forward")
        time.sleep(self.TIME)

        cleanUpGPIO()

    def test_move_backward(self):
        """
        Tests how car moves backwad.
        """

        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move backward
        driveSystem.moveBackward()
        
        print("Car moves backward")
        time.sleep(self.TIME)

        cleanUpGPIO()

    def test_move_left(self):
        """
        Tests how car moves left.
        """

        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move forward
        driveSystem.moveLeft()
        
        print("Car moves left")
        time.sleep(self.TIME)

        cleanUpGPIO()

    def test_move_right(self):
        """
        Tests how car moves right.
        """

        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move forward
        driveSystem.moveRight()
        
        print("Car moves right")
        time.sleep(self.TIME)

        cleanUpGPIO()

    def test_move_top_left(self):
        """
        Tests how car moves top-left.
        """

        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move forward
        driveSystem.moveTopLeft()
        
        print("Car moves top-left")
        time.sleep(self.TIME)

        cleanUpGPIO()
    
    def test_move_top_right(self):
        """
        Tests how car moves top-right.
        """

        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move forward
        driveSystem.moveTopRight()
        
        print("Car moves top-right")
        time.sleep(self.TIME)

        cleanUpGPIO()

    def test_move_bottom_left(self):
        """
        Tests how car moves bottom-left.
        """

        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move forward
        driveSystem.moveBottomLeft()
        
        print("Car moves bottom-left")
        time.sleep(self.TIME)

        cleanUpGPIO()

    def test_move_bottom_right(self):
        """
        Tests how car moves bottom-right.
        """

        initializeGPIO()

        # Initialize the motor control
        driveSystem = MotorControl()
        
        # Move forward
        driveSystem.moveBottomRight()
        
        print("Car moves bottom-right")
        time.sleep(self.TIME)

        cleanUpGPIO()

if (__name__ == '__main__'):
    unittest.main()