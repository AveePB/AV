from vehicle.modules.detection import Camera
import unittest
import cv2

class TestMotorSystem(unittest.TestCase):

    TEST_TIME = 3 # seconds

    def test_capture_image(self):
        cam = Camera()
        winname = 'Camera Test'

        # Turn on camera
        print("Take a picture!")
        cam.start()
        
        img = cam.capture_array()
        self.assertIsNotNone(img)

        # Create preview window
        cv2.namedWindow(winname)
        cv2.imshow(winname, img)
        cv2.waitKey(self.TEST_TIME * 1000) # wait x seconds

        # Turn off camera
        cam.stop()
        cv2.destroyAllWindows()  
        print("Picture taken.")              

if (__name__ == '__main__'):
    unittest.main()
