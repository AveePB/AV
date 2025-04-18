from controls import CONTROLS_BP, VEHICLE
from flask import Flask, render_template

app = Flask(__name__)
app.register_blueprint(CONTROLS_BP)

@app.route('/', methods=['GET'])
def home():
        VEHICLE.set_manual_mode()
        return render_template('index.html')

if (__name__ == '__main__'):
    app.run(debug=True)