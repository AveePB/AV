from vehicle.consts import LIDAR_USB_HEADER, LIDAR_DATA_PATH
from joystick import JOYSTICK_BP
from routes import ROUTES_BP
from car import Robot, VEHICLE
from multiprocessing import Process
from flask import Flask, Response
import cv2

app = Flask(__name__)
app.register_blueprint(JOYSTICK_BP)
app.register_blueprint(ROUTES_BP)

@app.route('/video_feed', methods=['GET'])
def video_feed():
    """
        Endpoint function that continuously returns a captured image from the camera. 
    """

    def generate():
        while True:
                frame = VEHICLE.camera().capture_array()
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if (__name__ == '__main__'):
    flask_process = Process(target=app.run)
    flask_process.start()

    #robot = Robot(LIDAR_DATA_PATH, LIDAR_USB_HEADER)
    #robot_process = Process(target=robot.run)
    #robot_process.start()

    #robot_process.join(15)
    flask_process.join(15)
    
    #robot_process.terminate()
    flask_process.terminate()

    #robot.stop_lidar()
    VEHICLE.camera().stop()