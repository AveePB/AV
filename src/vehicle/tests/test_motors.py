from vehicle.modules.motors import MotorSystem
from vehicle.modules.flags import Maneuver
import unittest
import time

class TestMotorSystem(unittest.TestCase):

    MOVEMENT_TIME = 5 # seconds

    def test_go_forward(self):
        ms = MotorSystem()

        print("Move forward!")
        ms.go_forward()

        self.assertTrue(ms.get_maneuver() is Maneuver.GO_FORWARD)
        time.sleep(self.MOVEMENT_TIME)
        print("Maneuver completed.")
    
    def test_go_backward(self):
        ms = MotorSystem()

        print("Move backward!")
        ms.go_backward()
        
        self.assertTrue(ms.get_maneuver() is Maneuver.GO_BACKWARD)
        time.sleep(self.MOVEMENT_TIME)
        print("Maneuver completed.")

    def test_go_left(self):
        ms = MotorSystem()

        print("Move left!")
        ms.go_left()
        
        self.assertTrue(ms.get_maneuver() is Maneuver.GO_LEFT)
        time.sleep(self.MOVEMENT_TIME)
        print("Maneuver completed.")
    
    def test_go_right(self):
        ms = MotorSystem()

        print("Move right!")
        ms.go_right()
        
        self.assertTrue(ms.get_maneuver() is Maneuver.GO_RIGHT)
        time.sleep(self.MOVEMENT_TIME)
        print("Maneuver completed.")
    
    def test_go_top_left(self):
        ms = MotorSystem()

        print("Move top left!")
        ms.go_top_left()
        
        self.assertTrue(ms.get_maneuver() is Maneuver.GO_TOP_LEFT)
        time.sleep(self.MOVEMENT_TIME)
        print("Maneuver completed.")
    
    def test_go_top_right(self):
        ms = MotorSystem()

        print("Move top right!")
        ms.go_top_right()
        
        self.assertTrue(ms.get_maneuver() is Maneuver.GO_TOP_RIGHT)
        time.sleep(self.MOVEMENT_TIME)
        print("Maneuver completed.")
    
    def test_go_bottom_left(self):
        ms = MotorSystem()

        print("Move bottom left!")
        ms.go_bottom_left()
        
        self.assertTrue(ms.get_maneuver() is Maneuver.GO_BOTTOM_LEFT)
        time.sleep(self.MOVEMENT_TIME)
        print("Maneuver completed.")
    
    def test_go_bottom_right(self):
        ms = MotorSystem()

        print("Move bottom right!")
        ms.go_bottom_right()
        
        self.assertTrue(ms.get_maneuver() is Maneuver.GO_BOTTOM_RIGHT)
        time.sleep(self.MOVEMENT_TIME)
        print("Maneuver completed.")

    def test_turn_left(self):
        ms = MotorSystem()

        print("Turn left!")
        ms.turn_left()
        
        self.assertTrue(ms.get_maneuver() is Maneuver.TURN_LEFT)
        time.sleep(self.MOVEMENT_TIME)
        print("Maneuver completed.") 
    
    def test_turn_right(self):
        ms = MotorSystem()

        print("Turn right!")
        ms.turn_right()
        
        self.assertTrue(ms.get_maneuver() is Maneuver.TURN_RIGHT)
        time.sleep(self.MOVEMENT_TIME)
        print("Maneuver completed.") 

if (__name__ == '__main__'):
    unittest.main()
