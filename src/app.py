from controls import CONTROLS_BP
from flask import Flask

app = Flask(__name__)
app.register_blueprint(CONTROLS_BP)

@app.route('/', methods=['GET'])
def home():
        return render_template('index.html')

if (__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0')