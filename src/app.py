from controls import CONTROLS_BP, VEHICLE
from flask import Flask, render_template, Response
import time
import cv2

app = Flask(__name__)
app.register_blueprint(CONTROLS_BP)

@app.route('/', methods=['GET'])
def home():
        VEHICLE.set_manual_mode()
        return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    def generate():
        while True:
                frame = VEHICLE.detection_system().get_image()
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if (__name__ == '__main__'):
    app.run(debug=True)