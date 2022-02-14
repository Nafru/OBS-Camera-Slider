# OBS-Camera-Slider

Multiple axis Camera slider controllable via [OBS](https://github.com/obsproject/obs-studio) (Open Broadcaster Software) and local webhost via [Flask](https://flask.palletsprojects.com/) with multiple presets.

You can see the slider in action at https://twitch.tv/marla_latete on the aquarium rotations as well use channel points to move the slider to set locations from chat.

## Getting Started

A full list of hardware required can be found in BOM document in the [Hardware Folder](https://github.com/Nafru/OBS-Camera-Slider/tree/main/hardware):

You will need the following software:
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


