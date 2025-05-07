from vehicle.modules.v3hicle import Vehicle
from vehicle.modules.flags import Maneuver, CarMode
from flask import request, render_template, Blueprint, Response
import multiprocessing

ROUTES_BP = Blueprint('routes', __name__)
VEHICLE_DATA = Vehicle()
DATA_QUEUE = multiprocessing.Queue()

@ROUTES_BP.route('/', methods=['GET'])
def index():
    """
        Endpoint function that return the page.
    """
    VEHICLE_DATA.set_manual_mode()
    DATA_QUEUE.put((CarMode.MANUAL, True, VEHICLE_DATA.get_maneuver()))

    return render_template('index.html')


@ROUTES_BP.route('/set-mode', methods=['POST'])
def setMode():
    """
        Endpoint function that handles the change of the car's mode.
    """
    new_mode = request.json['mode']

    if (new_mode == 'Manual'):
        VEHICLE_DATA.set_manual_mode()
        DATA_QUEUE.put((CarMode.MANUAL, True, VEHICLE_DATA.get_maneuver()))

    elif (new_mode == 'Line Follower'):
        VEHICLE_DATA.set_line_follower_mode()
        DATA_QUEUE.put((CarMode.LINE_FOLLOWER, True, VEHICLE_DATA.get_maneuver()))

    elif (new_mode == 'Autonomous Vehicle'):
        VEHICLE_DATA.set_autonomous_mode()
        DATA_QUEUE.put((CarMode.AUTONOMOUS_VEHICLE, True, VEHICLE_DATA.get_maneuver()))

    else:
        return Response('Failed to update the mode', status=400, mimetype='application/json')

    return Response('Successfully changed the mode', status=200, mimetype='application/json')


@ROUTES_BP.route('/forward', methods=['POST'])
def driveForward():
    """
        Endpoint function responsible for correction of the maneuver to go forward.
    """
    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_FORWARD)
        DATA_QUEUE.put((CarMode.MANUAL, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to forward!', status=200, mimetype='application/json')


@ROUTES_BP.route('/backward', methods=['POST'])
def driveBackward():
    """
        Endpoint function responsible for correction of the maneuver to go backward.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_BACKWARD)
        DATA_QUEUE.put((CarMode.MANUAL, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to backward!', status=200, mimetype='application/json')


@ROUTES_BP.route('/stop', methods=['POST'])
def stopDriving():
    """
        Endpoint function responsible for correction of the maneuver to stop driving.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.STOP)
        DATA_QUEUE.put((CarMode.MANUAL, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to stop the car!', status=500, mimetype='application/json')
    
    return Response('Successfully stopped the car!', status=200, mimetype='application/json')


@ROUTES_BP.route('/left', methods=['POST'])
def driveLeft():
    """
        Endpoint function responsible for correction of the maneuver to go left.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_LEFT)
        DATA_QUEUE.put((CarMode.MANUAL, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to Left!', status=200, mimetype='application/json')


@ROUTES_BP.route('/right', methods=['POST'])
def driveRight():
    """
        Endpoint function responsible for correction of the maneuver to go right.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_RIGHT)
        DATA_QUEUE.put((CarMode.MANUAL, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to right!', status=200, mimetype='application/json')


@ROUTES_BP.route('/top-left', methods=['POST'])
def driveTopLeft():
    """
        Endpoint function responsible for correction of the maneuver to go top-left.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_TOP_LEFT)
        DATA_QUEUE.put((CarMode.MANUAL, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to top left!', status=200, mimetype='application/json')


@ROUTES_BP.route('/top-right', methods=['POST'])
def driveTopRight():
    """
        Endpoint function responsible for correction of the maneuver to go top-right.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_TOP_RIGHT)
        DATA_QUEUE.put((CarMode.MANUAL, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to top right!', status=200, mimetype='application/json')


@ROUTES_BP.route('/bottom-left', methods=['POST'])
def driveBottomLeft():
    """
        Endpoint function responsible for correction of the maneuver to go bottom-left.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_BOTTOM_LEFT)
        DATA_QUEUE.put((CarMode.MANUAL, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to bottom left!', status=200, mimetype='application/json')


@ROUTES_BP.route('/bottom-right', methods=['POST'])
def driveBottomRight():
    """
        Endpoint function responsible for correction of the maneuver to go bottom-right.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.GO_BOTTOM_RIGHT)
        DATA_QUEUE.put((CarMode.MANUAL, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the direction of the car!', status=500, mimetype='application/json')
    
    return Response('Successfully set direction of the car to bottom right!', status=200, mimetype='application/json')


@ROUTES_BP.route('/turn-left', methods=['POST'])
def turnLeft():
    """
        Endpoint function responsible for correction of the maneuver to turn left.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.TURN_LEFT)
        DATA_QUEUE.put((CarMode.MANUAL, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the maneuver of the car to turn left!', status=500, mimetype='application/json')
    
    return Response('Successfully set maveuver of the car to turn left', status=200, mimetype='application/json')


@ROUTES_BP.route('/turn-right', methods=['POST'])
def turnRight():
    """
        Endpoint function responsible for correction of the maneuver to turn right.
    """

    if (VEHICLE_DATA.is_autonomous()):
        return Response('The vehicle is in autonomous mode!', status=400, mimetype='application/json')
    
    try:
        VEHICLE_DATA.set_maneuver(Maneuver.TURN_RIGHT)
        DATA_QUEUE.put((CarMode.MANUAL, True, VEHICLE_DATA.get_maneuver()))
    except Exception as e:
        print(e)
        return Response('Failed to change the maneuver of the car to turn right!', status=500, mimetype='application/json')
    
    return Response('Successfully set maveuver of the car to turn right', status=200, mimetype='application/json')


@ROUTES_BP.route('/shutdown', methods=['POST'])
def shutdown():
    """
        Endpoint function responsible for safe shutdown of electronic components.
    """

    DATA_QUEUE.put((VEHICLE_DATA.get_mode(), False, VEHICLE_DATA.get_maneuver()))
    return Response('Successfully shutdown of electronic components', status=200, mimetype='application/json')
