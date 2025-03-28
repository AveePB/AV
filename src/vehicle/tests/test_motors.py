from vehicle.modules.motors import MotorSystem
import unittest
import time

class TestMotorSystem(unittest.TestCase):

    def test_go_forward(self):

        ms = MotorSystem()

        ms.go_forward()
        time.sleep(4)       

        print("GO FORWARD")


if (__name__ == '__main__'):
    unittest.main()