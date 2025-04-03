from vehicle.modules.detection import Camera, DetectionSystem
from vehicle.consts import LIDAR_N_SCANS, LIDAR_SCAN_SIZE
import unittest
import cv2

class TestMotorSystem(unittest.TestCase):

    TEST_TIME = 5 # seconds

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
        cv2.moveWindow(winname, 0, 0)
        cv2.waitKey(self.TEST_TIME * 1000) # wait x seconds

        # Turn off camera
        cam.stop()
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
