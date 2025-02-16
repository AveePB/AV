"""
Unit tests of motor class.

This module has tests for all situations possible for a motor.
It shows how motors handle the change of direction.
"""

import unittest
import time
from car.motors import Motor, Direction
from car.constants import F_ENA, F_IN1, F_IN2

class TestMotorFunctions(unittest.TestCase):
    """
    Tests of motor functions.

    Set of specific scenarios, that test functions of motors.
    It shows how well it performs during pressure.
    """

    def test_forward(self):
        """
        Tests how change (to forward directory) impacts the motor.
        """

        # Intitialize motor
        motor = Motor(F_ENA, F_IN1, F_IN2)
        self.assertIs(motor.__direction, Direction.NONE)

        # Motor spins forward
        motor.forward()
        self.assertIs(motor.__direction, Direction.FORWARD)

        time.sleep(2)

        # Motor spins backward
        motor.backward()
        self.assertIs(motor.__direction, Direction.BACKWARD)

        time.sleep(2)

        # Motor stops spining
        motor.stop()
        self.assertIs(motor.__direction, Direction.NONE)

    def test_backward(self):
        """
        Tests how change (to backward directory) impacts the motor.
        """

        # Intitialize motor
        motor = Motor(F_ENA, F_IN1, F_IN2)
        self.assertIs(motor.__direction, Direction.NONE)

        # Motor spins backward
        motor.backward()
        self.assertIs(motor.__direction, Direction.BACKWARD)

        time.sleep(2)

        # Motor spins forward
        motor.forward()
        self.assertIs(motor.__direction, Direction.FORWARD)

        time.sleep(2)

        # Motor spins backward
        motor.backward()
        self.assertIs(motor.__direction, Direction.BACKWARD)

        time.sleep(2)

        # Motor stops spining
        motor.stop()
        self.assertIs(motor.__direction, Direction.NONE)

    def test_stop(self):
        """
        Tests how change (to stop) impacts the motor.
        """

        # Intitialize motor
        motor = Motor(F_ENA, F_IN1, F_IN2)
        self.assertIs(motor.__direction, Direction.NONE)

        # Motor spins forward
        motor.forward()
        self.assertIs(motor.__direction, Direction.FORWARD)

        time.sleep(2)

        # Motor stops spining
        motor.stop()
        self.assertIs(motor.__direction, Direction.NONE)

        time.sleep(2)

        # Motor spins backward
        motor.backward()
        self.assertIs(motor.__direction, Direction.BACKWARD)

        time.sleep(2)

        # Motor stops spining
        motor.stop()
        self.assertIs(motor.__direction, Direction.NONE)

if (__name__ == '__main__'):
    unittest.main()