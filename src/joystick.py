from vehicle.modules.flags import Maneuver
from vehicle.modules.v3hicle import Vehicle
from flask import Blueprint, Response
import multiprocessing

JOYSTICK_BP = Blueprint('joystick', __name__)
VEHICLE_DATA = Vehicle()
DATA_QUEUE = multiprocessing.Queue()

@JOYSTICK_BP.route('/forward', methods=['POST'])
def driveForward():
    """
        Endpoint function responsible for correction of the maneuver to go forward.
    """
    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_FORWARD)
        DATA_QUEUE.put((False, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to forward!', status=200, mimetype='application/json')


@JOYSTICK_BP.route('/backward', methods=['POST'])
def driveBackward():
    """
        Endpoint function responsible for correction of the maneuver to go backward.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_BACKWARD)
        DATA_QUEUE.put((False, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to backward!', status=200, mimetype='application/json')


@JOYSTICK_BP.route('/stop', methods=['POST'])
def stopDriving():
    """
        Endpoint function responsible for correction of the maneuver to stop driving.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.STOP)
        DATA_QUEUE.put((False, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to stop the car!', status=500, mimetype='application/json')
    
    return Response('Successfully stopped the car!', status=200, mimetype='application/json')


@JOYSTICK_BP.route('/left', methods=['POST'])
def driveLeft():
    """
        Endpoint function responsible for correction of the maneuver to go left.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_LEFT)
        DATA_QUEUE.put((False, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to Left!', status=200, mimetype='application/json')


@JOYSTICK_BP.route('/right', methods=['POST'])
def driveRight():
    """
        Endpoint function responsible for correction of the maneuver to go right.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_RIGHT)
        DATA_QUEUE.put((False, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to right!', status=200, mimetype='application/json')


@JOYSTICK_BP.route('/top-left', methods=['POST'])
def driveTopLeft():
    """
        Endpoint function responsible for correction of the maneuver to go top-left.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_TOP_LEFT)
        DATA_QUEUE.put((False, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to top left!', status=200, mimetype='application/json')


@JOYSTICK_BP.route('/top-right', methods=['POST'])
def driveTopRight():
    """
        Endpoint function responsible for correction of the maneuver to go top-right.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_TOP_RIGHT)
        DATA_QUEUE.put((False, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to top right!', status=200, mimetype='application/json')


@JOYSTICK_BP.route('/bottom-left', methods=['POST'])
def driveBottomLeft():
    """
        Endpoint function responsible for correction of the maneuver to go bottom-left.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_BOTTOM_LEFT)
        DATA_QUEUE.put((False, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to bottom left!', status=200, mimetype='application/json')


@JOYSTICK_BP.route('/bottom-right', methods=['POST'])
def driveBottomRight():
    """
        Endpoint function responsible for correction of the maneuver to go bottom-right.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_BOTTOM_RIGHT)
        DATA_QUEUE.put((False, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to bottom right!', status=200, mimetype='application/json')


@JOYSTICK_BP.route('/turn-left', methods=['POST'])
def turnLeft():
    """
        Endpoint function responsible for correction of the maneuver to turn left.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.TURN_LEFT)
        DATA_QUEUE.put((False, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the maneuver of the car to turn left!', status=500, mimetype='application/json')
    
    return Response('Successfully set maveuver of the car to turn left', status=200, mimetype='application/json')


@JOYSTICK_BP.route('/turn-right', methods=['POST'])
def turnRight():
    """
        Endpoint function responsible for correction of the maneuver to turn right.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.TURN_RIGHT)
        DATA_QUEUE.put((False, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the maneuver of the car to turn right!', status=500, mimetype='application/json')
    
    return Response('Successfully set maveuver of the car to turn right', status=200, mimetype='application/json')
