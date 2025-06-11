from vehicle.consts import LIDAR_USB_HEADER, LIDAR_DATA_PATH
from routes import ROUTES_BP, DATA_QUEUE
from car import Robot
from flask import Flask
import multiprocessing

# Configure flask application
app = Flask(__name__)
app.register_blueprint(ROUTES_BP)

# Configure robot application
robot = Robot(LIDAR_DATA_PATH, LIDAR_USB_HEADER)

# Run program if executable
if (__name__ == '__main__'):
    # Initialize robot application
    robot_process = multiprocessing.Process(target=robot.run, args=(DATA_QUEUE,))
    robot_process.start()

    # Initialize flask application
    app.run(host='0.0.0.0', port=5000, debug=False)