from car import VEHICLE
from flask import render_template, Blueprint, Response
import cv2

ROUTES_BP = Blueprint('routes', __name__)

@ROUTES_BP.route('/', methods=['GET'])
def index():
    """
        Endpoint function that return the page.
    """

    VEHICLE.set_manual_mode()
    return render_template('index.html')

@ROUTES_BP.route('/video_feed')
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

@ROUTES_BP.route('/autonomous-mode', methods=['POST'])
def setAutonomousMode():
    """
        Endpoint function responsible for switching the car's mode to the autonomous.
    """
    
    VEHICLE.set_autonomous_mode()
    
    return Response('Successfully set the autonomous mode!', status=200, mimetype='application/json')

@ROUTES_BP.route('/manual-mode', methods=['POST'])
def setManualMode():
    """
        Endpoint function responsible for switching the car's mode to the manual.
    """
    
    VEHICLE.set_manual_mode()

    return Response('Successfully set the manual mode!', status=200, mimetype='application/json')