from joystick import JOYSTICK_BP, VEHICLE
from routes import ROUTES_BP
from flask import Flask

app = Flask(__name__)
app.register_blueprint(JOYSTICK_BP)
app.register_blueprint(ROUTES_BP)

if (__name__ == '__main__'):
    app.run(debug=True)