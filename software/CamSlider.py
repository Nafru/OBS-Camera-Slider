#
# This script is part of the "Camera Slider Project" which can be found at https://github.com/Nafru/OBS-Camera-Slider
# This Python Script uses FLASK to create a virtual host to control virtual actuators using GRBL commands via Serial connection.
# Adjust the serial com port and baud rate to suit your settings. 
# Flask must be installed for use. https://flask.palletsprojects.com/
# To send control via Local host web browser, enter the url http://127.0.0.1/5000/(preset name).
# To run from OBS, Set up a scene with a browser source using the local host URL call. (https://obsproject.com/)
# Script is able to run commands for X, Y and Z axis by defining the gcode variables 
# G-code commands can be found at https://www.thomasnet.com/articles/custom-manufacturing-fabricating/g-code-commands/
#


import serial
import time

from flask import Flask
app=Flask(__name__)

#open grbl serial port and start serial connection
s = serial.Serial('COM5',115200) # set port and baud rate

# Wake up grbl
s.write("\r\n\r\n".encode())
time.sleep(2) # Wait for GRBL to initialize
s.flushInput() # Flush start up text in serial input

@app.route('/preset1') # Get confirmation on the local host web page
def preset1():
    gcode = '$J=G21G90X0f1000' + '$J=G21G90Y0f1000' + '$J=G21G90Z0f1000' # define axis move. For No axis call, replace the command call with '\n'
    s.write(gcode.encode()) # Call Gcode variable and send it in bytes to the GRBL
    return 'Move completed' 

@app.route('/preset2') # Get confirmation on the local host web page
def preset2():
    gcode = '$J=G21G90X-150f1000' + '$J=G21G90Y-10f1000' + '$J=G21G90Z-10f1000' # define axis move. For No axis call, replace the command call with '\n'
    s.write(gcode.encode()) # Call Gcode variable and send it in bytes to the GRBL
    return 'Move completed' 

@app.route('/preset3') # Get confirmation on the local host web page
def preset3():
    gcode = '$J=G21G90X10f1000' + '$J=G21G90Y10f1000' + '$J=G21G90Z10f1000' # define axis move. For No axis call, replace the command call with '\n'
    s.write(gcode.encode()) # Call Gcode variable and send it in bytes to the GRBL
    return 'Move completed' 

# Preset showing single axis call.
@app.route('/preset4') # Get confirmation on the local host web page
def preset4():
    gcode = '$J=G21G90X10f1000' + '\n' + '\n' # define axis move. For No axis call, replace the command call with '\n'
    s.write(gcode.encode()) # Call Gcode variable and send it in bytes to the GRBL
    return 'Move completed' 