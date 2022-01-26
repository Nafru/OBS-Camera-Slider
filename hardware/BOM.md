# OBS-Camera-Slider Bill of Materials

The following is just for demonstration purposes and will be modified. Do not order these parts.

## Top Level Assembly
The top level assembly is comprised of off-the-shelf parts, as well as sub-assemblies with their own parts lists.

|Designator|Description|Manufacturer|Part Number|Quantity|Unit of Measure|Supplier|
|---|---|---|---|---|---|---|
|CAMSLIDER|C-Beam Tension XL Linear Actuator Bundle|OpenBuilds|3045-Bundle|1|EA|Makerparts.ca|
|CAMERA|OBS-Compatible camera|Logitech|C920|1|EA|Best Buy|
|STEPPERCONTROLLER|Stepper controller that accepts G-code|N/A|N/A|1|EA|Sub-Assembly, see below|
|SCMOUNT1|3D-printed mount for STEPPERCONTROLLER|N/A|N/A|1|EA|Sub-Assembly, see below|

## STEPPERCONTROLLER Assembly
The stepper controller accepts G-Code and handles moving the camera slider.

|Designator|Description|Manufacturer|Part Number|Quantity|Unit of Measure|Supplier|
|---|---|---|---|---|---|---|
|ARDUINO1|Arduino board|Arduino|Uno Rev3|1|EA|Digikey|
|STEPPERCONTROL1|Arduino-compatible stepper motor control board|Synthetos|gShield|1|EA|Digikey.ca|
|WIFI1|Arduino-compatible Wifi adapter|Adafruit|2471|1|EA|Digikey.ca|

## SCMOUNT1 Assembly
3D printed platform to mount the stepper controller to a stepper motor.

|Designator|Description|Manufacturer|Part Number|Quantity|Unit of Measure|Supplier|
|---|---|---|---|---|---|---|
|MOUNTINGPLATE1|3D-printed mounting plate that accepts an Arduino Uno R3|N/A|N/A|1|EA|See hardware folder|
|INSERT1|M5 tapered heat-set brass inserts for plastics|McMaster-Carr|94180A363|4|EA|Makerparts.ca|
