from vehicle.modules.flags import Maneuver, CarMode

class Vehicle:
    """
        Vehicle model is used to manage flags that are responsible for control of all motors and sensor of the car.    
    """

    def __init__(self):
        """
            Constructor responsible for correct initialization of the vehicle model.
        """
        self.__current_maneuver = Maneuver.STOP
        self.__current_mode = CarMode.MANUAL

    def set_manual_mode(self):
        """
            Setter function of variable __is_current_mode.
        """
        self.__current_mode = CarMode.MANUAL

    def set_line_follower_mode(self):
        """
            Setter function of variable __is_current_mode.
        """
        self.__current_mode = CarMode.LINE_FOLLOWER
    
    def set_autonomous_mode(self):
        """
            Setter function of variable __current_mode.
        """
        self.__current_mode = CarMode.AUTONOMOUS_VEHICLE
    
    def get_mode(self):
        """
            Getter function of variable __current_mode
        """
        return self.__current_mode

    def is_autonomous(self):
        """
            Getter function of variable __current_mode.
        """
        return not(self.__current_mode is CarMode.MANUAL)
    
    def set_maneuver(self, new_maneuver):
        """
            Setter function of variable __current_maneuver.
        """
        if (type(new_maneuver) is Maneuver):
            self.__current_maneuver = new_maneuver
            #print(new_maneuver)
            return True
        else:
            return False

    def get_maneuver(self):
        """
            Getter function of variable __current_maneuver
        """
        return self.__current_maneuver
