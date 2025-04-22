from vehicle.modules.flags import Maneuver
from vehicle.modules.csvdata import CSVManager
from vehicle.lib.rplidar import RPLidar

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

    def run(self, data_queue):
        """
            Starts the application of the car.
        """
        from vehicle.modules.motors import MotorSystem

        # Start the robot
        ms = MotorSystem()
        self.__lidar.connect()
        self.__lidar.start_motor()
        self.__lidar.start()

        # Prepare the car
        curr_maneuver = Maneuver.STOP
        is_autonumous = False
        ms.stop()
        
        # Analyze environemnt
        while True:
            # Try to access shared memory
            if (not(is_autonumous) and not(data_queue.empty())):
                is_autonumous, is_running, curr_maneuver = data_queue.get() 
                if (not is_running): break
            
            # Ask ML model
            else: pass 

            # Read/write data
            scan = self.__lidar.read_single_measure()
            self.__csv_manager.create_record(curr_maneuver, scan)
            print("CURRENT MANEUVER:", curr_maneuver)
            """    
            # Perform the maneuver
            if (curr_maneuver is Maneuver.GO_FORWARD): ms.go_forward()
            elif (curr_maneuver is Maneuver.GO_BACKWARD): ms.go_backward()
            elif (curr_maneuver is Maneuver.STOP): ms.stop()
            elif (curr_maneuver is Maneuver.GO_LEFT): ms.go_left()
            elif (curr_maneuver is Maneuver.GO_RIGHT): ms.go_right()
            elif (curr_maneuver is Maneuver.GO_TOP_LEFT): ms.go_top_left()
            elif (curr_maneuver is Maneuver.GO_TOP_RIGHT): ms.go_top_right()
            elif (curr_maneuver is Maneuver.GO_BOTTOM_LEFT): ms.go_bottom_left()
            elif (curr_maneuver is Maneuver.GO_BOTTOM_RIGHT): ms.go_bottom_right()
            elif (curr_maneuver is Maneuver.TURN_LEFT): ms.turn_left()
            elif (curr_maneuver is Maneuver.TURN_RIGHT): ms.turn_right()
        """
        # Safely shutdown everything
        ms.stop()
        self.__lidar.stop()
        self.__lidar.stop_motor()
        self.__lidar.disconnect()
