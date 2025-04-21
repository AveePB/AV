from joystick import JOYSTICK_BP
from routes import ROUTES_BP
from car import Robot
from multiprocessing import Process
from flask import Flask

app = Flask(__name__)
app.register_blueprint(JOYSTICK_BP)
app.register_blueprint(ROUTES_BP)

if (__name__ == '__main__'):
    flask_process = Process(target=app.run)
    flask_process.start()

    robot = Robot('test.csv', '/dev/ttyUSB0')
    robot_process = Process(target=robot.run)
    robot_process.start()

    robot_process.join(5)
    flask_process.join(5)
    
    robot_process.terminate()
    flask_process.terminate()

    robot.stop_lidar()
