from rplidar import RPLidar
from picamera2 import Picamera2
from vehicle.consts import IMG_FORMAT, IMG_SIZE, LIDAR_USB_HEADER, LIDAR_SCAN_SIZE, LIDAR_N_SCANS
import random
import cv2

class Camera(Picamera2):
    """
        Class used to control AV's camera to record/take photos of the closest environment.
    """

    def __init__(self):
        """
            Constructor responsible for initializing camera with proper settings.
        """
        super().__init__()

        self.av_config = self.create_still_configuration(main={
            "format": IMG_FORMAT,
            "size": IMG_SIZE
        })

        self.configure(self.av_config)
    
    def capture_array(self):
        """
            Function used to take a picture from camera.
        """

        img = super().capture_array('main')
        img = cv2.rotate(img, cv2.ROTATE_180) # Camera is flipped by 180 degrees
        
        return img

class DetectionSystem:
    """
        Detection system is used to observe nearby environment.
    """

    def __init__(self):
        """
            Constructor responsible for initializing all sensors.
        """
        self.__camera = Camera()
        self.__camera.start()
        self.__lidar = RPLidar(LIDAR_USB_HEADER)

        # Show lidar info
        print(self.__lidar.get_info())
        print(self.__lidar.get_health())
    
    def get_image(self):
        """
            Getter function used to fetch an image from camera.
        """
        return self.__camera.capture_array()

    def scan_env(self):
        """
            Scans nearby environment, then returns a map of points. 
        """
        all_points = []

        for i, scan in enumerate(self.__lidar.iter_scans()):
            if (i > LIDAR_N_SCANS): 
                break
            
            all_points.extend(scan)
                
        return random.choices(all_points, k=LIDAR_N_SCANS*LIDAR_SCAN_SIZE)
    
    def turn_off(self):
        """
            Shuts down camera and lidar sensor.
        """
        self.__camera.stop()
        self.__lidar.stop_motor()
        self.__lidar.stop()
