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

    TIME = 4 # Movement time (seconds)

    def test_move_forward(self):
        """
        Tests how car moves forwad.
        """

        initializeGPIO()

        # Initialize rhe motor controll
        driveSystem = MotorControl()
        
        # Move forward
        driveSystem.moveForward()
        
        print("Car moves forward")
        time.sleep(self.TIME)

        cleanUpGPIO()
