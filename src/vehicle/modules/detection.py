from picamera2 import Picamera2
from vehicle.consts import IMG_FORMAT, IMG_SIZE
import cv2

class Camera(Picamera2):
    """
        Class used to control AV's camera to recored/take photos of the closest environment.
    """

    def __init__(self):
        super().__init__()

        self.av_config = self.create_still_configuration({
            "format": IMG_FORMAT,
            "size": IMG_SIZE
        })

        self.configure(self.av_config)
    
    def capture_array(self, stream='main'):
        """
            Function used to take a picture from camera.
        """

        img = super().capture_array(stream=stream)
        cv2.rotate(img, cv2.ROTATE_180) # Camera is flipped by 180 degrees
        
        return img
