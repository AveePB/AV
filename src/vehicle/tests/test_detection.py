from vehicle.modules.detection import Camera, DetectionSystem
from vehicle.consts import LIDAR_SCAN_SIZE
import unittest
import cv2

class TestMotorSystem(unittest.TestCase):

    TEST_TIME = 5 # seconds

    def test_detection_system_scan_env(self):
        # Initialize detection system
        ds = DetectionSystem()
        winname = 'Camera Test'
        
        # Turn on camera
        print("Take a picture!")
        
        img = ds.get_image()
        self.assertIsNotNone(img)

        # Create preview window
        cv2.namedWindow(winname)
        cv2.imshow(winname, img)
        cv2.moveWindow(winname, 0, 0)
        cv2.waitKey(self.TEST_TIME * 1000) # wait x seconds
        print("Camera test completed!")

        
        # Perform first scan
        print("Starts scanning!")
        points = ds.scan_env()

        # Check if total size of scan is equal
        print(points)
        self.assertEqual(len(points), LIDAR_SCAN_SIZE)

        # Turn off detection system
        ds.turn_off()
        print("Scan completed!")

if (__name__ == '__main__'):
    unittest.main()
