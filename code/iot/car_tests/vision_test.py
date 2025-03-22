"""
Unit tests of camera class.

This module checks if camera works.
"""

import unittest
import time
import cv2
from car.vision import Camera

class TestCamera(unittest.TestCase):
    """
    Tests of Camera class.
    """

    TIME = 4 # Camera test time (seconds)

    def test_taking_picture(self):
        # Create camera object
        visionSystem = Camera()

        img = visionSystem.getImage()
        cv2.imshow("Test of taking a picture", img)
        
        # Close window
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if (__name__ == '__main__'):
    unittest.main()