# OBS-Camera-Slider Bill of Materials

This is a full list of material and tools required for the build that is running on https://twitch.tv/marla_latete stream. The actuator is a 1 meter C Beam kit with additions. You are able to use any of the kits and scale to size. 
It is strongly suggested that you use black if you are using this with a reflective surface like a fishtank to stop it being seen on camera.
If you are planning on adding a second axis, you will require the double wide gantery for the X axis to connect the second axis to it.

## Tools Rquired for the build **to be updated

|Designator|Description|Supplier|
|---|---|---|
|OpenBuilds 8mm Spanner Wrench|Wrench needed for gantery adjusting|MakerParts.ca|
|Balldriver Screw Driver Set|Or like metric allen Keys size #2, #2.5 and #3|Makerparts.ca|
|Micro Screwdrivers|Blade and Phillips drivers|  
|Wire Cutters|||
|Wire Strippers|||
|Soldering Iron|||

## Consumables and additional parts **to be updated

|Designator|Description|
|---|---|
|Solder|| 
|Wire|18 guage, in 4 colours IE Black, Red, Yellow and Blue|
|Masking tape|For making point on the actuator during setup| 
|Single Row Pin Headers|To solder to the GRBLSheild for pin out extensions|
|Wire to board Connector Housing|To connect the wire to pin headers|
|330 ohm resistor|required for limit switches|
|Shrink Tube|cover on wire connections and resistor|

## Camerea Slider Assembly
|Designator|Description|Manufacturer|Part Number|Quantity|Unit of Measure|Supplier|
|---|---|---|---|---|---|---|
|CAMSLIDER|C-Beam Tension XL Linear Actuator Bundle|OpenBuilds|3045-Bundle|1|EA|Makerparts.ca|
|Neema 32 Stepper Motor|Neema 32 Stepper Motor|OpenBuilds|NA|1|EA|Makerparts.ca|
|Xtension Limit Switch Kit|Xtension Limit Switch Kit|OpenBuilds|NA|2|EA|Makerparts.ca|
|Drag/Cable Chain|Drag/Cable Chain|OpenBuilds|NA|1|EA|Makerparts.ca|
|Xtension 4 Wire Without Connectors|Stepper motor controller wire|OpenBuilds|NA|1|EA|Makerparts.ca|
|Xtension 3 Wire Without Connectors|Limit switch wire|OpenBuilds|NA|1|EA|Makerparts.ca|
|Xtension Connectors|3 pin Limit switch connector|OpenBuilds|NA|1|EA|Makerparts.ca|
|Xtension Connectors|4 pin Stepper motor connector|OpenBuilds|NA|1|EA|makerparts.ca|
|Aluminum Spacers 13.2mm|10 Pack support for drag chain|OpenBuilds|NA|1|10 pack|Makerparts.ca|
|20mm Low Profile Screws M5|10 Pack Support for drag chain|OpenBuilds|NA|1|10 Pack|Makerparts.ca|
|Drop In Tee Nuts|10 Pack support for rag chain|OpenBuilds|NA|1|10 pack|Markerparts.ca|
|L Bracket|Single hole per arm for connecting the drag chain|OpenBuilds|NA|1|EA|Markerparts.ca|
|Double Tee Nut|Connector for gantry to drag chain|OpenBuilds|NA|1|EA|Markerparts.ca|
|Button Head Screws M3|6mm screw to attache the drag chain|OpenBuilds|NA|1|EA|Makerparts.ca|
|M3 Nylon Insert Hex Locknut|Drag chain attachment|OpenBuilds|NA|1|EA|Makerparts.ca|
|Slot Cover / Panel Holder|Wire protection and secure for limit switches|OpenBuilds|NA|1|EA|Makerparts.ca| 


## ARDUINO and STEPPERCONTROLLER Assembly
The assembly is comprised of a 3D Printed SCMount (see below) that holds an Arduino and stepper controller. Optionally you can also attach an ESP-01 and ESP8266 wifi module for wireless network abilities. The Arduino can connect to a streaming PC via USB cable if you do not want the WIFI option. The Arduino accepts communicatiosn from the PC and sends G-Code to the Grblsheild Stepper controller and handles moving the camera slider.

|Designator|Description|Manufacturer|Part Number|Quantity|Unit of Measure|Supplier|
|---|---|---|---|---|---|---|
|SCMOUNT1|3D-printed mount for STEPPERCONTROLLER (see below)|N/A|N/A|1|EA|Sub-Assembly|
|ARDUINO1|Arduino board|Arduino|Uno Rev3|1|EA|Digikey|
|STEPPERCONTROL1|Arduino-compatible stepper motor control board|Synthetos|gShield|1|EA|Digikey.ca|
|USB A/B|USB cable for connection from PC to Arduino|N/A|N/A|1|EA||
|5 volt dc Power|5 Volt power for Arduino|NA||1|EA||
|12 volt dc power|12 volt power for stepper motor|NA||1|EA||  

## Optional Wifi Network 

|Designator|Description|Manufacturer|Part Number|Quantity|Unit of Measure|Supplier|
|---|---|---|---|---|---|---|
|WIFI|ESP8266 Wifi module with ESP01 adapter|||1|EA||
|Esp-01S Programming Module|USB programmer for ESP8266 Module|||1|EA|| 

## SCMOUNT1 Assembly
3D printed platform to mount the stepper controller to a stepper motor.

|Designator|Description|Manufacturer|Part Number|Quantity|Unit of Measure|Supplier|
|---|---|---|---|---|---|---|
|MOUNTINGPLATE1|3D-printed mounting plate that accepts an Arduino Uno R3|N/A|N/A|1|EA|See hardware folder|
|INSERT1|M5 tapered heat-set brass inserts for plastics|McMaster-Carr|94180A363|4|EA|Makerparts.ca|
