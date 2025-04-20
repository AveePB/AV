from controls import CONTROLS_BP, VEHICLE
from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
app.register_blueprint(CONTROLS_BP)

@app.route('/', methods=['GET'])
def home():
        VEHICLE.set_manual_mode()
        return render_template('index.html')

@app.route('/camera', methods=['GET'])
def streamCamera():
        ret, buffer = cv2.imencode('.jpg', VEHICLE.detection_system().get_image(), [int(cv2.IMWRITE_JPEG_QUALITY), 70])
        frame = buffer.toBytes()

        return Response(
                b'--frame\r\n' 
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n',
                mimetype='multipart/x-mixed-replace; boundary=frame'
        )


if (__name__ == '__main__'):
    app.run(debug=True)