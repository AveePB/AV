from vehicle.modules.motors import MotorSystem, Maneuver
from vehicle.modules.csvdata import CSVManager
from vehicle.modules.v3hicle import Vehicle
from vehicle.lib.rplidar import RPLidar

VEHICLE = Vehicle()

class Robot:
    """
        Robot object is responsible for data collecting and autonomous driving
    """

    def __init__(self, file_path, lidar_header):
        """
            Constructor that creates objects for the data collection & autonomous driving.

            Args:
                file_path (str): source path to the csv file.
                lidar_header (str): system path to the usb header.
        """

        self.__csv_manager = CSVManager(file_path)
        self.__lidar = RPLidar(lidar_header)
        self.is_running = True
        
        print(self.__lidar.get_info())
        print(self.__lidar.get_health())

    def run(self):
        """
            Starts the application of the car.
        """
        ms = MotorSystem()
        self.__lidar.connect()
        self.__lidar.start_motor()
        self.__lidar.start()

        while self.is_running:
            scan = self.__lidar.read_single_measure()
            self.__csv_manager.create_record(VEHICLE.get_maneuver(), scan)
            
            if (VEHICLE.get_maneuver() is Maneuver.GO_FORWARD): ms.go_forward()
            elif (VEHICLE.get_maneuver() is Maneuver.GO_BACKWARD): ms.go_backward()
            elif (VEHICLE.get_maneuver() is Maneuver.STOP): ms.stop()
            elif (VEHICLE.get_maneuver() is Maneuver.GO_LEFT): ms.go_left()
            elif (VEHICLE.get_maneuver() is Maneuver.GO_RIGHT): ms.go_right()
            elif (VEHICLE.get_maneuver() is Maneuver.GO_TOP_LEFT): ms.go_top_left()
            elif (VEHICLE.get_maneuver() is Maneuver.GO_TOP_RIGHT): ms.go_top_right()
            elif (VEHICLE.get_maneuver() is Maneuver.GO_BOTTOM_LEFT): ms.go_bottom_left()
            elif (VEHICLE.get_maneuver() is Maneuver.GO_BOTTOM_RIGHT): ms.go_bottom_right()
            elif (VEHICLE.get_maneuver() is Maneuver.TURN_LEFT): ms.turn_left()
            elif (VEHICLE.get_maneuver() is Maneuver.TURN_RIGHT): ms.turn_right()
        
        ms.stop()
            
    
    def stop_lidar(self):
        """
            Safely closes lidar.
        """

        self.__lidar.stop()
        self.__lidar.stop_motor()
        self.__lidar.disconnect()
