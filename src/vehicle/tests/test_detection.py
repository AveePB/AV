from vehicle.modules.detection import Camera, DetectionSystem
from vehicle.consts import LIDAR_N_SCANS, LIDAR_SCAN_SIZE
import unittest
import cv2

class TestMotorSystem(unittest.TestCase):

    TEST_TIME = 5 # seconds
    ds = DetectionSystem()

    def test_capture_image(self):
        winname = 'Camera Test'
        
        # Turn on camera
        print("Take a picture!")
        
        img = self.ds.get_image()
        self.assertIsNotNone(img)

        # Create preview window
        cv2.namedWindow(winname)
        cv2.imshow(winname, img)
        cv2.moveWindow(winname, 0, 0)
        cv2.waitKey(self.TEST_TIME * 1000) # wait x seconds

        # Turn off camera
        cv2.destroyAllWindows()  
        print("Picture taken.")              

    def test_detection_system_scan_env(self):
        # Perform first scan
        ds = DetectionSystem()
        points = ds.scan_env()

        # Check if total size of scan is equal
        print(points)
        self.assertEqual(len(points), LIDAR_N_SCANS*LIDAR_SCAN_SIZE)

        # Turn off elements
        ds.turn_off()

if (__name__ == '__main__'):
    unittest.main()
