"""
Module for observing the environment around the car.

This module provides two important classes LiDAR and Camera.
Those elements are responsible for providing information about
what's happening around the car.
"""

from car.constants import RAW_IMG_SIZE, IMG_SIZE, IMG_FORMAT
from picamera2 import Picamera2

class Camera:
    """
    Class to controll car's camera. It takes pictures of what's
    happening at the moment and converts it to forced format.
    """

    def __init__(self):
        """
        Initializes the Camera object with the default arguments (constants).
        """

        self.__picam = Picamera2()
        self.__picam.configure(
            self.__picam.create_video_configuration(
                raw={'size': RAW_IMG_SIZE}, 
                main={'format': IMG_FORMAT, 'size': IMG_SIZE}
            ))
        self.__picam.start()

    def getImage(self):
        """
        Camera takes a picture of current situation. The image gets formated
        and is returned.
        """

        return self.__picam.capture_array()
    
    