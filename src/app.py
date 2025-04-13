from controls import CONTROLS_BP
from flask import Flask

app = Flask(__name__)
app.register_blueprint(CONTROLS_BP)

if (__name__ == '__main__'):
    app.run(debug=True)