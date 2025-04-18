from pyrplidar import PyRPlidar
from picamera2 import Picamera2
from vehicle.consts import IMG_FORMAT, IMG_SIZE, LIDAR_USB_HEADER, LIDAR_SCAN_SIZE, LIADR_N_SCANS
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
        self.__lidar = PyRPlidar()
        self.__lidar.connect(LIDAR_USB_HEADER, baudrate=256000, timeout=3)
        self.__lidar.set_motor_pwm(500)
        
        self.__camera = Camera()
        self.__camera.start()
    
    def get_image(self):
        """
            Getter function used to fetch an image from camera.
        """
        return self.__camera.capture_array()

    def scan_env(self):
        """
            Scans nearby environment, then returns a map of points. 
        """
        EMPTY = -1
        scan_data = [EMPTY] * LIDAR_SCAN_SIZE
        scan_generator = self.__lidar.force_scan()
        
        # Scan until you find all 360 angle-points
        for i, scan in enumerate(scan_generator):
            
            # Done with scanning
            if (LIADR_N_SCANS == i): break
            print(scan)
            # Analyze each point
            #for (quality, angle, distance) in scan:
                #angle = int(angle)
                
                # If angle is in the range    
                #if (0 <= angle and angle < LIDAR_SCAN_SIZE):
                    
                    # Choose the closest point
                 #   if (scan_data[angle] == EMPTY or distance < scan_data[angle]):
                  #      scan_data[angle] = distance

        return scan_data
    
    def turn_off(self):
        """
            Shuts down camera and lidar sensor.
        """
        self.__lidar.stop()
        self.__lidar.set_motor_pwm(0)
        self.__lidar.disconnect()

        self.__camera.stop()