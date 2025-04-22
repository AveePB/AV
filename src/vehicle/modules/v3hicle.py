from vehicle.modules.motors import Maneuver

class Vehicle:
    """
        Vehicle model is used to manage flags that are responsible for control of all motors and sensor of the car.    
    """

    def __init__(self):
        """
            Constructor responsible for correct initialization of the vehicle model.
        """
        self.__current_maneuver = Maneuver.STOP
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
    
    def set_maneuver(self, new_maneuver):
        """
            Setter function of variable __current_maneuver.
        """
        if (type(new_maneuver) is Maneuver):
            self.__current_maneuver = new_maneuver
            print("Successfully set new maneuver")
            print(new_maneuver)
            return True
        else:
            print("Failed to set maneuver")
            return False

    def get_maneuver(self):
        """
            Getter function of variable __current_maneuver
        """
        return self.__current_maneuver
