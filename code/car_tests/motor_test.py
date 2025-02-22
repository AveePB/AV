"""
Unit tests of motor class.

This module has tests for all situations possible for a motor.
It shows how motors handle the change of direction.
"""

import unittest
import time
from car.motors import Motor, Direction
from car.constants import F_ENA, F_IN1, F_IN2
from car.gpio import initializeGPIO, cleanUpGPIO

class TestMotorFunctions(unittest.TestCase):
    """
    Tests of motor functions.

    Set of specific scenarios, that test functions of motors.
    It shows how well it performs during pressure.
    """

    TIME = 4 # Motor spining time (seconds)

    def test_forward(self):
        """
        Tests how change (to forward directory) impacts the motor.
        """

        initializeGPIO()

        # Intitialize motor
        motor = Motor(F_ENA, F_IN1, F_IN2)
        self.assertIs(motor.getDirection(), Direction.NONE)
        
        print("Motor initialized")
        time.sleep(self.TIME)

        # Motor spins forward
        motor.forward()
        self.assertIs(motor.getDirection(), Direction.FORWARD)

        print("Motor spins forward")
        time.sleep(self.TIME)

        # Motor spins backward
        motor.backward()
        self.assertIs(motor.getDirection(), Direction.BACKWARD)

        print("Motor spins backward")
        time.sleep(self.TIME)

        # Motor stops spining
        motor.stop()
        self.assertIs(motor.getDirection(), Direction.NONE)

        cleanUpGPIO()

    def test_backward(self):
        """
        Tests how change (to backward directory) impacts the motor.
        """

        initializeGPIO()

        # Intitialize motor
        motor = Motor(F_ENA, F_IN1, F_IN2)
        self.assertIs(motor.getDirection(), Direction.NONE)

        print("Motor initialized")
        time.sleep(self.TIME)

        # Motor spins backward
        motor.backward()
        self.assertIs(motor.getDirection(), Direction.BACKWARD)

        print("Motor spins backward")
        time.sleep(self.TIME)

        # Motor spins forward
        motor.forward()
        self.assertIs(motor.getDirection(), Direction.FORWARD)

        print("Motor spins forward")
        time.sleep(self.TIME)

        # Motor spins backward
        motor.backward()
        self.assertIs(motor.getDirection(), Direction.BACKWARD)

        print("Motor spins backward")
        time.sleep(self.TIME)

        # Motor stops spining
        motor.stop()
        self.assertIs(motor.getDirection(), Direction.NONE)
        
        cleanUpGPIO()

    def test_stop(self):
        """
        Tests how change (to stop) impacts the motor.
        """

        initializeGPIO()

        # Intitialize motor
        motor = Motor(F_ENA, F_IN1, F_IN2)
        self.assertIs(motor.getDirection(), Direction.NONE)

        print("Motor initialized")
        time.sleep(self.TIME)

        # Motor spins forward
        motor.forward()
        self.assertIs(motor.getDirection(), Direction.FORWARD)

        print("Motor spins forward")
        time.sleep(self.TIME)

        # Motor stops spining
        motor.stop()
        self.assertIs(motor.getDirection(), Direction.NONE)

        print("Motor stops spining")
        time.sleep(self.TIME)

        # Motor spins backward
        motor.backward()
        self.assertIs(motor.getDirection(), Direction.BACKWARD)

        print("Motor spins backward")
        time.sleep(self.TIME)

        # Motor stops spining
        motor.stop()
        self.assertIs(motor.getDirection(), Direction.NONE)

        cleanUpGPIO()

if (__name__ == '__main__'):
    unittest.main()