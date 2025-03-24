from vehicle.modules.motors import MotorSystem
import unittest

class TestMotorSystem(unittest.TestCase):

    def go_forward_test(self):

        ms = MotorSystem()

        ms.go_forward()


if (__name__ == '__main__'):
    unittest.main()