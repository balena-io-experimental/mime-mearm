#!/usr/bin/env python

from flask import Flask, render_template, Response
import piconzero as pz
from camera import Camera

app = Flask(__name__)
pz.init()

class Axis:
    def __init__(self, pin, value=90, min=0, max=180):
        self.pin = pin
        self.value = value
        self.min = min
        self.max = max
        pz.setOutputConfig(self.pin, 2)
        pz.setOutput(self.pin, self.value)

    def set(self, value):
        self.limit(value)
        pz.setOutput(self.pin, self.value)

    def inc(self, value):
        self.limit(self.value + value)
        pz.setOutput(self.pin, self.value)

    def limit(self, value):
        if value < self.min:
            self.value = self.min
        elif value > self.max:
            self.value = self.max
        else:
            self.value = value
        print self.value

class Arm:
    grip = Axis(0, 90, 90, 165)
    elbow = Axis(1, 90)
    shoulder = Axis(2, 40)
    hip = Axis(3, 75)
arm = Arm()

@app.route('/')
def index():
    return render_template('arm.html')

@app.route("/<direction>")
def move(direction):
    global arm
    if direction == 'gopen':
        arm.grip.inc(-5)

    elif direction == 'gclose':
        arm.grip.inc(5)

    elif direction == 'eup':
        arm.elbow.inc(5)

    elif direction == 'edown':
        arm.elbow.inc(-5)

    elif direction == 'sback':
        arm.shoulder.inc(-5)

    elif direction == 'sfwd':
        arm.shoulder.inc(5)

    elif direction == 'hright':
        arm.hip.inc(-5)

    elif direction == 'hleft':
        arm.hip.inc(5)

    return direction

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
