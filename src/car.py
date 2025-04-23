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

        self.__file_path = file_path
        self.__lidar_header = lidar_header

    def run(self, data_queue):
        """
            Starts the application of the car.
        """
        from vehicle.modules.motors import MotorSystem

        # Start the robot
        ms = MotorSystem()
        lidar = RPLidar(self.__lidar_header)
        csv_manager = CSVManager(self.__file_path)

        # Show lidar info
        print(lidar.get_info())
        print(lidar.get_health())

        # Prepare the car
        curr_maneuver = Maneuver.STOP
        is_autonumous = False

        # Analyze environemnt
        for i, scan in enumerate(lidar.iter_scans()):
            # Show the scan
            print(scan)

            # Try to access shared memory
            if (not(data_queue.empty())):
                is_autonumous, is_running, curr_maneuver = data_queue.get() 
                if (not is_running): break
            
            # Ask ML model
            if (is_autonumous):
                pass 
            
            # Save scan info
            csv_manager.create_record(curr_maneuver, scan)

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

        # Safely shutdown everything
        ms.stop()
        lidar.stop()
        lidar.stop_motor()
        lidar.disconnect()
