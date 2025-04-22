from vehicle.consts import LIDAR_USB_HEADER, LIDAR_DATA_PATH
from joystick import JOYSTICK_BP
from routes import ROUTES_BP
from car import Robot
from multiprocessing import Process
from flask import Flask

APP_EXECUTION_TIME = 60 # seconds

app = Flask(__name__)
app.register_blueprint(JOYSTICK_BP)
app.register_blueprint(ROUTES_BP)

if (__name__ == '__main__'):
    flask_process = Process(target=app.run)
    flask_process.start()

    robot = Robot(LIDAR_DATA_PATH, LIDAR_USB_HEADER)
    robot_process = Process(target=robot.run)
    robot_process.start()

    robot_process.join(APP_EXECUTION_TIME)
    flask_process.join(1)
    
    robot_process.terminate()
    flask_process.terminate()

    robot.stop_lidar()