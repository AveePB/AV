from vehicle.modules.camera import Camera
from vehicle.modules.motors import MotorSystem

class Vehicle:
    """
        Vehicle model is used to control all motors and sensor of the car. It also stores information about the mode of the car.    
    """

    def __init__(self):
        """
            Constructor responsible for correct initialization of the vehicle model.
        """

        #self.__camera = Camera()
        #self.__camera.start()
        self.__motor_system = MotorSystem()
        self.__is_autonomous = False

    def set_autonomous_mode(self):
        """
            Setter function of variable __is_autonomous.
        """
        self.__is_autonomous = True

    def set_manual_mode(self):
        """
            Setter function of variable __is_autonomous.
        """
        self.__is_autonomous = False

    def is_autonomous(self):
        """
            Getter function of variable __is_autonomous.
        """
        return self.__is_autonomous
    
    #def camera(self):
    #    """
    #        Access function of object __detection_system.
    #    """
    #    return self.__camera
    
    def drive_system(self):
        """
            Access function of object __motor_system.
        """
        return self.__motor_system
