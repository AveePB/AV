from vehicle.modules.motors import MotorSystem
import unittest
import time

class TestMotorSystem(unittest.TestCase):

    MOVEMENT_TIME = 5 # seconds

    def test_go_forward(self):
        ms = MotorSystem()

        print("Move forward!")
        ms.go_forward()

        time.sleep(self.MOVEMENT_TIME)
        print("Maneuver completed.")
    
    def test_go_backward(self):
        ms = MotorSystem()

        print("Move backward!")
        ms.go_backward()
        
        time.sleep(self.MOVEMENT_TIME)
        print("Maneuver completed.")

    def test_go_left(self):
        ms = MotorSystem()

        print("Move left!")
        ms.go_left()
        
        time.sleep(self.MOVEMENT_TIME)
        print("Maneuver completed.")
    
    def test_go_right(self):
        ms = MotorSystem()

        print("Move right!")
        ms.go_right()
        
        time.sleep(self.MOVEMENT_TIME)
        print("Maneuver completed.")


if (__name__ == '__main__'):
    unittest.main()