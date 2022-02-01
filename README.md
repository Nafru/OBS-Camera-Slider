# OBS-Camera-Slider

Multiple axis Camera slider controllable via [OBS](https://github.com/obsproject/obs-studio) (Open Broadcaster Software) and local webhost via [Flask](https://flask.palletsprojects.com/) with multiple presets.

## Getting Started

You'll need the following hardware (see also the 'hardware' folder):
1. Stepper-motor driven linear actuator with a mount suitable for your camera
2. 12 - 24 volt DC power adequate for stepper motors
3. Stepper motor
4. Stepper controller that accepts g-code, for example an [Arduino Uno](https://docs.arduino.cc/hardware/uno-rev3) running GRBL with a [gShield](https://github.com/synthetos/grblShield)
5. A camera compatible with [OBS Studio ](https://obsproject.com/)

You'll need the following software:
1. [Arduino IDE](https://www.arduino.cc/en/software)
2. [OBS Studio ](https://obsproject.com/)
3. [Flask](https://flask.palletsprojects.com/)
4. Python compatible text editor

Python Libraries you will require:
1. [pySerial](https://pyserial.readthedocs.io/en/latest/)
2. [time](https://docs.python.org/3/library/time.html)

Arduino Sketch you will need:
1. [GRBLUpload](https://github.com/grbl/grbl)
