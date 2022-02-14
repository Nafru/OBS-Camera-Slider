# OBS-Camera-Slider

Multiple axis Camera slider controllable via [OBS](https://github.com/obsproject/obs-studio) (Open Broadcaster Software) and local webhost via [Flask](https://flask.palletsprojects.com/) with multiple presets.

## Getting Started

You'll need the following hardware (see also the 'hardware' folder):
1. Stepper-motor driven linear actuator with a mount suitable for your camera
2. 12 - 24 volt DC power adequate for stepper motors
3. Stepper motor
4. Stepper controller that accepts g-code, for example an [Arduino Uno](https://docs.arduino.cc/hardware/uno-rev3) running GRBL with a [gShield](https://github.com/synthetos/grblShield)
5. A camera compatible with [OBS Studio ](https://obsproject.com/)
6. ESP8266 - 01 (adapter and programming board) optional for WIFI connectivity

You'll need the following software:
1. [Arduino IDE](https://www.arduino.cc/en/software)
2. [Universal G-Code Sender](https://winder.github.io/ugs_website/)
3. [Flask](https://flask.palletsprojects.com/)
4. [Camslider.py](https://github.com/Nafru/OBS-Camera-Slider/tree/main/software)
4. Python compatible text editor
5. [Tibbo Device Server Toolkit (TDST)](https://tibbo.com/soi/software.html)  Virtual Port to send Com to TCP_IP.
6. [OBS Studio ](https://obsproject.com/)
7. [TriggerFyre](https://overlays.thefyrewire.com/widgets/triggerfyre/) For scene changing via channel points for chat on stream.
8. [Advanced Scene Switcher](https://obsproject.com/forum/resources/advanced-scene-switcher.395/) For automated rotation and movement in OBS.

Python Libraries you will require:
1. [pySerial](https://pyserial.readthedocs.io/en/latest/)
2. [time](https://docs.python.org/3/library/time.html)

Arduino Sketch you will need:
1. [GRBLUpload](https://github.com/grbl/grbl)

ESP8266 Libraries and SKetch
1. [WifiManager](https://github.com/tzapu/WiFiManager#install-through-library-manager)


