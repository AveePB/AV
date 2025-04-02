from picamera2 import Picamera2
from vehicle.consts import IMG_FORMAT, IMG_SIZE
import cv2

class Camera(Picamera2):
    """
        Class used to control AV's camera to record/take photos of the closest environment.
    """

    def __init__(self):
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
        return img
