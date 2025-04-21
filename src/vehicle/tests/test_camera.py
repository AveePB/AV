from vehicle.modules.camera import Camera
import unittest
import cv2

class TestCamera(unittest.TestCase):

    TEST_TIME = 5 # seconds

    def test_capture_array(self):
        # Initialize camera
        winname = 'Camera Test'
        camera = Camera()

        # Turn on camera
        print("Take a picture!")
        
        img = camera.capture_array()
        self.assertIsNotNone(img)
        print("Picture taken!")
        
        # Create preview window
        cv2.namedWindow(winname)
        cv2.imshow(winname, img)
        cv2.moveWindow(winname, 0, 0)
        cv2.waitKey(self.TEST_TIME * 1000) # wait x seconds
        
        print("Camera test completed!")

if (__name__ == '__main__'):
    unittest.main()
