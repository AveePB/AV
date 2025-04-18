from vehicle.modules.motors import MotorSystem
from vehicle.modules.detection import DetectionSystem
from flask import Blueprint, Response

CONTROLS_BP = Blueprint('controls', __name__)
DETECTION_SYSTEM = DetectionSystem()
DRIVE_SYSTEM = MotorSystem()

@CONTROLS_BP.route('/forward', methods=['POST'])
def driveForward():
    try:
        DRIVE_SYSTEM.go_forward()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to forward!', status=200, mimetype='application/json')

@CONTROLS_BP.route('/backward', methods=['POST'])
def driveBackward():
    try:
        DRIVE_SYSTEM.go_backward()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to backward!', status=200, mimetype='application/json')

@CONTROLS_BP.route('/stop', methods=['POST'])
def stopDriving():
    try:
        DRIVE_SYSTEM.stop()
    except Exception:
        return Response('Failed to stop the car!', status=500, mimetype='application/json')
    
    return Response('Successfully stopped the car!', status=200, mimetype='application/json')

@CONTROLS_BP.route('/left', methods=['POST'])
def driveLeft():
    try:
        DRIVE_SYSTEM.go_left()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to Left!', status=200, mimetype='application/json')

@CONTROLS_BP.route('/right', methods=['POST'])
def driveRight():
    try:
        DRIVE_SYSTEM.go_right()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to right!', status=200, mimetype='application/json')

@CONTROLS_BP.route('/top-left', methods=['POST'])
def driveTopLeft():
    try:
        DRIVE_SYSTEM.go_top_left()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to top left!', status=200, mimetype='application/json')

@CONTROLS_BP.route('/top-right', methods=['POST'])
def driveTopRight():
    try:
        DRIVE_SYSTEM.go_top_right()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to top right!', status=200, mimetype='application/json')

@CONTROLS_BP.route('/bottom-left', methods=['POST'])
def driveBottomLeft():
    try:
        DRIVE_SYSTEM.go_bottom_left()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to bottom left!', status=200, mimetype='application/json')

@CONTROLS_BP.route('/bottom-right', methods=['POST'])
def driveBottomRight():
    try:
        DRIVE_SYSTEM.go_bottom_right()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to bottom right!', status=200, mimetype='application/json')

@CONTROLS_BP.route('/turn-left', methods=['POST'])
def turnLeft():
    try:
        DRIVE_SYSTEM.turn_left()
    except Exception:
        return Response('Failed to change the maneuver of the car to turn left!', status=500, mimetype='application/json')
    
    return Response('Successfully set maveuver of the car to turn left', status=200, mimetype='application/json')

@CONTROLS_BP.route('/turn-right', methods=['POST'])
def turnRight():
    try:
        DRIVE_SYSTEM.turn_right()
    except Exception:
        return Response('Failed to change the maneuver of the car to turn right!', status=500, mimetype='application/json')
    
    return Response('Successfully set maveuver of the car to turn right', status=200, mimetype='application/json')