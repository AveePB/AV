from vehicle.vehicle import Vehicle
from flask import Blueprint, Response

CONTROLS_BP = Blueprint('controls', __name__)
VEHICLE = Vehicle()

@CONTROLS_BP.route('/forward', methods=['POST'])
def driveForward():
    """
        Endpoint function responsible for correction of the maneuver to go forward.
    """
    
    if (VEHICLE.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE.drive_system().go_forward()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to forward!', status=200, mimetype='application/json')


@CONTROLS_BP.route('/backward', methods=['POST'])
def driveBackward():
    """
        Endpoint function responsible for correction of the maneuver to go backward.
    """

    if (VEHICLE.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE.drive_system().go_backward()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to backward!', status=200, mimetype='application/json')


@CONTROLS_BP.route('/stop', methods=['POST'])
def stopDriving():
    """
        Endpoint function responsible for correction of the maneuver to stop driving.
    """

    if (VEHICLE.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE.drive_system().stop()
    except Exception:
        return Response('Failed to stop the car!', status=500, mimetype='application/json')
    
    return Response('Successfully stopped the car!', status=200, mimetype='application/json')


@CONTROLS_BP.route('/left', methods=['POST'])
def driveLeft():
    """
        Endpoint function responsible for correction of the maneuver to go left.
    """

    if (VEHICLE.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE.drive_system().go_left()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to Left!', status=200, mimetype='application/json')


@CONTROLS_BP.route('/right', methods=['POST'])
def driveRight():
    """
        Endpoint function responsible for correction of the maneuver to go right.
    """

    if (VEHICLE.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE.drive_system().go_right()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to right!', status=200, mimetype='application/json')


@CONTROLS_BP.route('/top-left', methods=['POST'])
def driveTopLeft():
    """
        Endpoint function responsible for correction of the maneuver to go top-left.
    """

    if (VEHICLE.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE.drive_system().go_top_left()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to top left!', status=200, mimetype='application/json')


@CONTROLS_BP.route('/top-right', methods=['POST'])
def driveTopRight():
    """
        Endpoint function responsible for correction of the maneuver to go top-right.
    """

    if (VEHICLE.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE.drive_system().go_top_right()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to top right!', status=200, mimetype='application/json')


@CONTROLS_BP.route('/bottom-left', methods=['POST'])
def driveBottomLeft():
    """
        Endpoint function responsible for correction of the maneuver to go bottom-left.
    """

    if (VEHICLE.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE.drive_system().go_bottom_left()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to bottom left!', status=200, mimetype='application/json')


@CONTROLS_BP.route('/bottom-right', methods=['POST'])
def driveBottomRight():
    """
        Endpoint function responsible for correction of the maneuver to go bottom-right.
    """

    if (VEHICLE.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE.drive_system().go_bottom_right()
    except Exception:
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to bottom right!', status=200, mimetype='application/json')


@CONTROLS_BP.route('/turn-left', methods=['POST'])
def turnLeft():
    """
        Endpoint function responsible for correction of the maneuver to turn left.
    """

    if (VEHICLE.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE.drive_system().turn_left()
    except Exception:
        return Response('Failed to change the maneuver of the car to turn left!', status=500, mimetype='application/json')
    
    return Response('Successfully set maveuver of the car to turn left', status=200, mimetype='application/json')


@CONTROLS_BP.route('/turn-right', methods=['POST'])
def turnRight():
    """
        Endpoint function responsible for correction of the maneuver to turn right.
    """

    if (VEHICLE.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE.drive_system().turn_right()
    except Exception:
        return Response('Failed to change the maneuver of the car to turn right!', status=500, mimetype='application/json')
    
    return Response('Successfully set maveuver of the car to turn right', status=200, mimetype='application/json')