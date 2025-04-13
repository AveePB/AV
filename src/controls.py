from vehicle.modules.motors import MotorSystem
from flask import Blueprint, Response

CONTROLS_BP = Blueprint('controls', __name__)
DRIVE_SYSTEM = MotorSystem()

@CONTROLS_BP.route('/forward')
def driveForward():
    try:
        DRIVE_SYSTEM.go_forward()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to forward!', status=200, mimetype='application/json')

@CONTROLS_BP.route('/backward')
def driveBackward():
    try:
        DRIVE_SYSTEM.go_backward()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to backward!', status=200, mimetype='application/json')

@CONTROLS_BP.route('/stop')
def stopDriving():
    try:
        DRIVE_SYSTEM.stop()
    except Exception:
        return Response('Failed to stop the car!', status=500, mimetype='application/json')
    
    return Response('Successfully stopped the car!', status=200, mimetype='application/json')
