from vehicle.modules.motors import MotorSystem
from vehicle.modules.csvdata import CSVManager
from vehicle.lib.rplidar import RPLidar
from joystick import VEHICLE

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
        
        print(self.__lidar.get_info())
        print(self.__lidar.get_health())

    def run(self):
        """
            Starts the application of the car.
        """
        ms = MotorSystem()
        ms.go_forward()

        self.__lidar.connect()
        self.__lidar.start_motor()
        self.__lidar.start()

        while True:
            scan = self.__lidar.read_single_measure()
            self.__csv_manager.create_record(VEHICLE.drive_system().get_maneuver(), scan)
            
    
    def stop_lidar(self):
        """
            Safely closes lidar.
        """

        self.__lidar.stop()
        self.__lidar.stop_motor()
        self.__lidar.disconnect()
