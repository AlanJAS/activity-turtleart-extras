# -*- coding: utf-8 -*-
# Copyright (c) 2011-15 Walter Bender
# Copyright (c) 2011-15 Alan Aguiar

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

from gettext import gettext as _

'''
Note: this file contains string from plugins and related projects that
are not included in the default packaaging of Turtle Art. The reason
for gathering these strings here is to enable us to use one common POT
file across all of these projects.

TODO: build some automated way of maintaining this file.
'''

# ACTIVITIES

TURTLEBLOCK_STRINGS = [
    _('Turtle Blocks'),
    _('Turtle Art')
    ]

TURTLEARTMINI_STRINGS = [
    _('Turtle Art Mini')
    ]

TURTLECONFUSION_STRINGS = [
    _('Turtle Confusion'),
    _('Select a challenge')
    ]

TURTLEAMAZONAS_STRINGS = [
    _('Amazonas Tortuga'),
    _('Select a challenge')
    ]

TURTLEFLAGS_STRINGS = [
    _('Turtle Flags'),
    _('Use the turtle to draw country flags')
]

# PLUGINS

AX12_STRINGS = [
    #TRANS: AX12 is a special servo-motor of Dynamixel
    _('ERROR: The degrees must be between 0 and 300'),
    _('ERROR: The speed must be a value between 0 and 1023'),
    _('ERROR: The value must be 0 or 1, LOW or HIGH'),
    _('ERROR: The board is disconected or the ID is out of range'),
    _('ERROR: The especified ID is not available'),
    _('AX-12 Motors functions'),
    _('ax12'),
    _('refresh AX12'),
    _('refresh the state of the Ax palette and blocks'),
    _('getID'),
    _('return a random ID of the conected AX-motors'),
    _('get position'),
    _('get the position of the AX-12 motors'),
    _('set position'),
    _('idMotor'),
    _('degrees'),
    _('set the position of the AX-12 motors'),
    _('set speed'),
    _('speed'),
    _('set the speed of the AX-12 motors'),
    _('stop'),
    _('stop the AX-12 motors '),
    _('get temperature'),
    _('get the temperature of the AX-12 motors'),
    _('get voltage'),
    _('get the voltage of the AX-12 motors'),
    _('set led'),
    _('action'),
    _('turns the AX led motor with id idMotor when action = 1, turn off if action = 0')
]

ATYARANDU_STRINGS = [
    _('Palette of Renewable Energy'),
    _('refresh Energy'),
    _('updates the status of the pallet and the Energy blocks'),
    _('energy generated'),
    _('Estimated value of renewable energy (MW) to generate in the next hour in Uruguay'),
    _('max energy'),
    _('Nominal value of renewable energy (MW) that can be generated in Uruguay'),
    _('recommended energy'),
    _('The preferred value of renewable energy (MW) for use'),
    _('ON'),
    _('Power on'),
    _('OFF'),
    _('Power off'),
    _('relay'),
    _('power on/off the relay'),
    _('ERROR: Use 0 or 1, not %s')
]

CURRENCY_STRINGS = [
    _('Palette of Mexican pesos'),
    _('Palette of Colombian pesos'),
    _('Palette of Rwandan francs'),
    _('Palette of US dollars'),
    _('Palette of Australian dollars'),
    _('Palette of Paraguayan Guaranies'),
    _('Palette of Peruvian Nuevo Soles'),
    _('Palette of Uruguayan Pesos')
    ]

BUTIA_STRINGS = [
    #TRANS: Butia is a Robot Project from Uruguay
    #(http://www.fing.edu.uy/inco/proyectos/butia/)
    _('TurtleBots'),
    #TRANS: summary of TurtleBots activity
    _('TurtleBlocks with robotic plugins'),
    _('ERROR: The speed must be a value between 0 and 1023'),
    _('ERROR: The speed must be a value between -1023 and 1023'),
    _('ERROR: The pin must be between 1 and 8'),
    _('ERROR: The value must be 0 or 1, LOW or HIGH'),
    _('ERROR: The mode must be INPUT or OUTPUT.'),
    _('turns LED on and off: 1 means on, 0 means off'),
    _('returns the gray level as a value between 0 and 65535'),
    _('returns 1 when the button is pressed and 0 otherwise'),
    _('returns the light level as a value between 0 and 65535'),
    _('returns the distance as a value between 0 and 65535'),
    _('returns the resistance value (ohms)'),
    _('returns the voltage value (volts)'),
    _('returns the temperature value (celsius degree)'),
    _('custom module %s'),
    _('sensor a'),
    _('sensor b'),
    _('sensor c'),
    _('actuator a'),
    _('actuator b'),
    _('actuator c'),
    _('LED'),
    _('button'),
    _('gray'),
    _('light'),
    _('distance'),
    _('resistance'),
    _('voltage'),
    _('temperature'),
    _('Butia Robot'),
    _('butia'),
    _('refresh Butia'),
    _('refresh the state of the Butia palette and blocks'),
    #TRANS: This string is shorthand for "battery charge of Butia"
    _('battery charge Butia'),
    _('returns the battery charge in volts. If no motors present, it returns 255'),
    #TRANS: This string is shorthand for "speed of Butia"
    _('speed Butia'),
    _('set the speed of the Butia motors'),
    _('move Butia'),
    _('left'),
    _('right'),
    _('moves the Butia motors at the specified speed'),
    _('stop Butia'),
    _('stop the Butia robot'),
    #TRANS: This string is shorthand for "move Butia forward"
    _('forward Butia'),
    _('move the Butia robot forward'),
    #TRANS: This string is shorthand for "turn Butia left"
    _('left Butia'),
    _('turn the Butia robot at left'),
    #TRANS: This string is shorthand for "turn Butia right"
    _('right Butia'),
    _('turn the Butia robot at right'),
    #TRANS: This string is shorthand for "move Butia backward"
    _('backward Butia'),
    _('move the Butia robot backward'),
    _('Butia Robot extra blocks'),
    _('butia-extra'),
    # TRANS: cast means data type conversion
    _('CAST\nsensor'),
    _('name'),
    _('original'),
    _('f(x)='),
    # TRANS: cast means data type conversion
    _('Cast a new sensor block'),
    # TRANS: cast means data type conversion
    _('CAST sensor'),
    # TRANS: cast means data type conversion
    _('Cast a new actuator block'),
    # TRANS: cast means data type conversion
    _('CAST\nactuator'),
    # TRANS: cast means data type conversion
    _('CAST actuator'),
    # TRANS: cast means data type conversion
    _('Butia Robot cast blocks'),
    # TRANS: cast means data type conversion
    _('butia-cast'),
    _('Butia'),
    _('pin mode Butia'),
    _('pin'),
    _('mode'),
    _('Select the pin function (INPUT, OUTPUT).'),
    _('read pin Butia'),
    _('read the value of a pin'),
    _('write pin Butia'),
    _('value'),
    _('set a hack pin to 0 or 1'),
    _('INPUT'),
    _('Configure hack pin for digital input.'),
    _('HIGH'),
    _('Set HIGH value for digital pin.'),
    _('LOW'),
    _('Set LOW value for digital port.'),
    _('OUTPUT'),
    _('Configure hack port for digital output.'),
    _('firmware Butia'),
    _('returns the Firmware version of Butia robot'),
    _('get IP'),
    _('returns the current IP of the computer'),
    _('Butia IP'),
    _('changes the IP of Butia robot'),
    _('wireless'),
    _('wireless network'),
    _('wired'),
    _('wired network'),
    _('set current Butia robot'),
    _('ERROR: The pin %s must be in OUTPUT mode.'),
    _('ERROR: The pin %s must be in INPUT mode.'),
    _('The device must be an integer'),
    _('Not found Butia %s'),
    _("ERROR: Something wrong with function '%s'"),
    _('ERROR: cannot init GCONF client: %s'),
    _('ERROR: You must cast Sensor or Actuator: A, B or C'),
    _("ERROR: Invalid IP '%s'"),
    _('Creating PyBot server'),
    _('ERROR creating PyBot server'),
    _('PyBot is alive!'),
    _('Ending Butia polling')
]

FOLLOWME_STRINGS = [
    _('Error importing Pygame. This plugin require Pygame 1.9'),
    _('Error on initialization of the camera'),
    _('No camera was found'),
    _('Error stopping camera'),
    _('Error starting camera'),
    #TRANS: The "mask" is used to restrict processing to a region in the image
    _('Error in get mask'),
    _('FollowMe'),
    _('followme'),
    _('refresh FollowMe'),
    _('Search for a connected camera.'),
    #TRANS: the calibration is used to match an RGB color to a target
    _('calibration'),
    _('store a personalized calibration'),
    _('return a personalized calibration'),
    _('follow'),
    _('follow a color or calibration'),
    _('brightness'),
    _('set the camera brightness as a value between 0 to 255.'),
    _('threshold'),
    # TRANS: RGB color space (red, green, blue)
    _('set a threshold for a RGB color'),
    _('camera mode'),
    # TRANS: RGB, YUV, and HSV are color spaces
    _('set the color mode of the camera: RGB; YUV or HSV'),
    _('get brightness'),
    _('get the brightness of the ambient light'),
    _('average color'),
    _('if set to 0 then color averaging is off during calibration; for other values it is on'),
    _('x position'),
    _('return x position'),
    _('y position'),
    _('return y position'),
    _('pixels'),
    _('return the number of pixels of the biggest blob'),
    # TRANS: RGB color space (red, green, blue)
    _('RGB'),
    _('set the color mode of the camera to RGB'),
    # TRANS: YUV color space (luminance, chrominance)
    _('YUV'),
    _('set the color mode of the camera to YUV'),
    # TRANS: HSV color space (hue, saturation, value)
    _('HSV'),
    _('set the color mode of the camera to HSV'),
    _('get color'),
    _('get the color of an object'),
    _('color distance'),
    _('set the distance to identify a color'),
    _('minimum pixels'),
    _('set the minimal number of pixels to follow'),
    _('empty calibration'),
    _('error in string conversion')
]


COLOR_STRINGS = [
    _('Error importing Pygame. This plugin requires Pygame 1.9'),
    _('Error on initialization of the camera'),
    _('No camera was found'),
    _('Error stopping camera'),
    _('Error starting camera'),
    _('colorview'),
    _('color detector'),
    _('color compare'),
    _('compares a color with the palette'),
    _('set tolerance'),
    _('sets the tolerance between colors'),
    _('set brightness'),
    _('sets the brightness of the camera'),
    _('view camera'),
    _('shows the camera')
]

PATTERN_DETECTION_STRINGS = [
    #TRANS: Pattern detection is a plugin that allow detect signals
    #with the camera
    _('Pattern detection'),
    _('pattern_detection'),
    _('Seeing signal'),
    _('Returns True if the signal is in front of the camera'),
    _('Distance to signal'),
    _('Returns the distance of the signal to the camera in millimeters')
]

SUMO_STRINGS = [
    #TRANS: SumBot is a robot programmed for "Sumo wrestling"
    _('SumBot'),
    _('sumtia'),
    _('speed SumBot'),
    _('submit the speed to the SumBot'),
    _('set the default speed for the movement commands'),
    #TRANS: This string is shorthand for "move SumBot forward"
    _('forward SumBot'),
    _('move SumBot forward'),
    #TRANS: This string is shorthand for "move SumBot backward"
    _('backward SumBot'),
    _('move SumBot backward'),
    _('stop SumBot'),
    _('stop the SumBot'),
    #TRANS: This string is shorthand for "turn SumBot left"
    _('left SumBot'),
    _('turn left the SumBot'),
    #TRANS: This string is shorthand for "move SumBot right"
    _('right SumBot'),
    _('turn right the SumBot'),
    #TRANS: The angle to the center is the angle SumBot must turn to
    #face the center of the playing field
    _('angle to center'),
    #TRANS: dohyo is the playing field
    _('get the angle to the center of the dohyo'),
    #TRANS: The angle to the center is the angle SumBot must turn to
    #face the Enemy (opponent)
    _('angle to Enemy'),
    _('get the angle to the Enemy'),
    #TRANS: This string is shorthand for "x coordinate of SumBot"
    _('x coor. SumBot'),
    _('get the x coordinate of the SumBot'),
    #TRANS: This string is shorthand for "y coordinate of SumBot"
    _('y coor. SumBot'),
    _('get the y coordinate of the SumBot'),
    #TRANS: This string is shorthand for "x coordinate of SumBot's enemy"
    _('x coor. Enemy'),
    _('get the x coordinate of the Enemy'),
    #TRANS: This string is shorthand for "y coordinate of SumBot's enemy"
    _('y coor. Enemy'),
    _('get the y coordinate of the Enemy'),
    #TRANS: This string is shorthand for "rotation of SumBot"
    _('rotation SumBot'),
    _('get the rotation of the Sumbot'),
    #TRANS: This string is shorthand for "rotation of SumBot's enemy"
    _('rotation Enemy'),
    _('get the rotation of the Enemy'),
    _('distance to center'),
    #TRANS: dohyo is the playing field
    _('get the distance to the center of the dohyo'),
    _('distance to Enemy'),
    _('get the distance to the Enemy'),
    _('update information'),
    _('update information from the server')
]

PHYSICS_STRINGS = [
    # TRANS: Please use similar terms to those used in the Physics Activity
    _('Palette of physics blocks'),
    _('start polygon'),
    _('Begin defining a new polygon based \
on the current Turtle xy position.'),
    _('add point'),
    _('Add a new point to the current \
polygon based on the current Turtle xy position.'),
    _('end polygon'),
    _('Define a new polygon.'),
    _('end filled polygon'),
    _('Not a simple polygon'),
    _('Define a new filled polygon.'),
    _('triangle'),
    # TRANS: base of a triangle
    _('base'),
    _('height'),
    _('Add a triangle object to the project.'),
    _('circle'),
    _('Add a circle object to the project.'),
    _('rectangle'),
    _('width'),
    _('height'),
    _('Add a rectangle object to the project.'),
    _('reset'),
    _('Reset the project; clear the object list.'),
    _('motor'),
    #TRANS: torque as in engine torque
    _('torque'),
    _('speed'),
    _('Motor torque and speed range from 0 (off) to positive numbers; \
motor is placed on the most recent object created.'),
    _('pin'),
    _('Pin an object down so that it cannot fall.'),
    _('pen'),
    _('Add a pen to an object so that its \
movements are traced.'),
    _('joint'),
    _('x'),
    _('y'),
    _('Join two objects together (the \
object at the current location and the object at point x, y).'),
    _('save as Physics activity'),
    _('Save the project to the Journal as a Physics activity.'),
    # TRANS: Here, gear means a toothed wheel, as in a clock-works
    _('gear'),
    _('Add a gear object to the project.'),
    _('density'),
    _('Set the density property for objects \
(density can be any positive number).'),
    _('friction'),
    _('Set the friction property for objects (value from 0 to 1, \
where 0 turns friction off and 1 is strong friction).'),
    # TRANS: bounciness is coefficient of restitution
    _('bounciness'),
    _('Set the bounciness property for \
objects (a value from 0 to 1, where 0 means no bounce and 1 is very bouncy).'),
    # TRANS: dynamic here means moving vs in a fixed position
    _('dynamic'),
    _('If dynamic = 1, the object can move; \
if dynamic = 0, it is fixed in position.')
]

WEDO_STRINGS = [
    # TRANS: WeDo is a robotics product of the LEGO company
    _("The parameter must be a integer, not '%s'"),
    _('Motor speed must be an integer between -100 and 100'),
    _('WeDo found %s bricks'),
    _('WeDo not found'),
    _('WeDo number %s was not found'),
    _('Palette of WeDo blocks'),
    _('wedo'),
    _('refresh WeDo'),
    _('Search for a connected WeDo.'),
    _('WeDo'),
    _('set current WeDo device'),
    _('number of WeDos'),
    _('number of WeDo devices'),
    _('tilt'),
    _("tilt sensor output: (-1 == no tilt,0 == tilt forward, 3 == tilt back, 1 == tilt left, 2 == tilt right)"),
    _('distance'),
    #TRANS: This string is shorthand for "output of the distance sensor"
    _('distance sensor output'),
    _('Motor A'),
    _('returns the current speed of Motor A'),
    _('Motor B'),
    _('returns the current speed of Motor B'),
    _('set the speed for Motor A'),
    _('set the speed for Motor B')
]

LEGO_STRINGS = [
    # TRANS: Lego NXT is a robotics product of the LEGO company
    _('button'),
    _('distance'),
    _('color'),
    _('light'),
    _('sound'),
    _('gray'),
    # TRANS: The brick is the NXT controller
    _('Please check the connection with the brick'),
    _("Invalid port '%s'. Port must be: PORT A, B or C"),
    _("Invalid port '%s'. Port must be: PORT 1, 2, 3 or 4"),
    _('The value of power must be between -127 to 127'),
    _("The parameter must be a integer, not '%s'"),
    _('An error has occurred: check all connections and try to reconnect'),
    _('NXT found %s bricks'),
    _('NXT not found'),
    _('Brick number %s was not found'),
    _('Palette of LEGO NXT blocks of motors'),
    _('nxt-motors'),
    _('refresh NXT'),
    _('Search for a connected NXT brick.'),
    _('NXT'),
    _('set current NXT device'),
    _('number of NXTs'),
    _('number of NXT devices'),
    _('brick name'),
    _('Get the name of a brick.'),
    _('play tone'),
    _('frequency'),
    _('time'),
    _('Play a tone at frequency for time.'),
    # TRANS: turn is the action
    _('turn motor %s'),
    _('port'),
    # TRANS: rotations is quantity of turns
    _('rotations'),
    _('power'),
    _('turn a motor'),
    _('synchronize %s motors'),
    _('synchronize two motors connected in PORT B and PORT C'),
    _('PORT %s'),
    _('PORT %s of the brick'),
    _('start motor'),
    _('Run a motor forever.'),
    _('brake motor'),
    _('Stop a specified motor.'),
    # TRANS: reset is used to reset the counter associated with the motor
    _('reset motor'),
    _('Reset the motor counter.'),
    _('motor position'),
    _('Get the motor position.'),
    _('Palette of LEGO NXT blocks of sensors'),
    _('nxt-sensors'),
    _('light sensor'),
    _('gray sensor'),
    _('button sensor'),
    _('distance sensor'),
    _('sound sensor'),
    _('color sensor'),
    # TRANS: the battery level is the charge level of the brick
    _('battery level'),
    _('Get the battery level of the brick in millivolts'),
    _('color as light'),
    _('use color sensor as light sensor'),
    # TRANS: set light is used to set the light level associated with
    # the color sensor (which can emit light as well as sense it)
    _('set light'),
    _('Set color sensor light.'),
    _('compass'),
    _('compass sensor')
]

ARDUINO_STRINGS = [
    #TRANS: Arduino plugin to control an Arduino board
    _('Palette of Arduino blocks'),
    _('HIGH'),
    _('LOW'),
    _('INPUT'),
    _('OUTPUT'),
    #TRANS: PWM is pulse-width modulation
    _('PWM'),
    _('SERVO'),
    _('ERROR: Check the Arduino and the number of port.'),
    _('ERROR: Value must be a number from 0 to 1.'),
    _('ERROR: Value must be a number from 0 to 180.'),
    _('ERROR: Value must be either HIGH or LOW, 0 or 1'),
    _('ERROR: The mode must be either INPUT, OUTPUT, PWM or SERVO.'),
    _('ERROR: The value must be an integer.'),
    _('ERROR: The pin must be an integer.'),
    _('ERROR: You must configure the mode for the pin.'),
    _('arduino'),
    _('refresh Arduino'),
    _('Search for connected Arduinos.'),
    _('Arduino'),
    _('set current Arduino board'),
    _('number of Arduinos'),
    _('number of Arduino boards'),
    _('Arduino name'),
    _('Get the name of an Arduino.'),
    #TRANS: pin mode is used to specify the mode (INPUT, OUTPUT, etc)
    #in which an I/O pin is being used.
    _('pin mode'),
    _('pin'),
    _('mode'),
    _('Select the pin function (INPUT, OUTPUT, PWM, SERVO).'),
    _('analog write'),
    _('value'),
    _('Write analog value in specified port.'),
    _('analog read'),
    _('Read value from analog port. Value may be between 0 and 1.'),
    _('digital write'),
    _('Write digital value to specified port.'),
    _('digital read'),
    _('Read value from digital port.'),
    _('Set HIGH value for digital port.'),
    _('Configure Arduino port for digital input.'),
    _('Configure Arduino port to drive a servo.'),
    _('Set LOW value for digital port.'),
    _('Configure Arduino port for digital output.'),
    _('Configure Arduino port for PWM (pulse-width modulation).'),
    _('Not found Arduino %s'),
    _('The pin must be an integer'),
    _('The device must be an integer'),
    _('Error loading %s board')
]

RODI_STRINGS = [
    #TRANS: Rodi is the name of Paraguayan robot based on Arduino
    _('HIGH'),
    _('LOW'),
    _('INPUT'),
    _('OUTPUT'),
    #TRANS: PWM is pulse-width modulation
    _('PWM'),
    _('SERVO'),
    _('ERROR: Check the connection with the robot.'),
    _('ERROR: The speed must be a value between 0 and %d'),
    _('ERROR: The speed must be a value between -%(max)d and %(max)d'),
    _('Palette for Rodi bots using Arduino'),
    _('refresh Rodi'),
    _('refresh the state of the Rodi palette and blocks'),
    _('Rodi'),
    _('set current Rodi robot'),
    _('number of Rodis'),
    _('number of Rodi robots'),
    _('Rodi name'),
    _('Get the name of a Rodi robot'),
    _('move Rodi'),
    _('left'),
    _('right'),
    _('moves the Rodi motors at the specified speed'),
    _('stop Rodi'),
    _('stop the Rodi robot'),
    _('forward Rodi'),
    _('move the Rodi robot forward'),
    _('left Rodi'),
    _('turn the Rodi robot at left'),
    _('right Rodi'),
    _('turn the Rodi robot at right'),
    _('backward Rodi'),
    _('move the Rodi robot backward'),
    _('distance Rodi'),
    _('returns the distance as a value between 0 and 1'),
    _('left sensor Rodi'),
    _('returns the left line sensor as a value between 0 and 1'),
    _('right sensor Rodi'),
    _('returns the right line sensor as a value between 0 and 1'),
    _('The device must be an integer'),
    _('Not found Rodi %s'),
    _('Error loading %s board')
]

FISCHER_STRINGS = [
    # TRANS: Fischer is a shortest of fischertechnik robot
    _('Please check the connection with the fischer'),
    _("Invalid port '%s'. Port must be: PORT 1 or 2"),
    _("Invalid port '%s'. Port must be: PORT 1, 2 or 3"),
    _('The value of power must be an integer between -100 to 100'),
    _("The parameter must be a integer, not '%s'"),
    _('An error has occurred: check all connections and try to reconnect'),
    _('Found %s Fischers'),
    _('Fischer not found'),
    _('Fischer number %s was not found'),
    _('Palette of Fischertechnik robot'),
    _('fischer'),
    _('refresh Fischer'),
    _('Search for a connected Fischer brick.'),
    _('Fischer'),
    _('set current Fischer device'),
    _('number of Fischers'),
    _('number of Fischer devices'),
    _('light'),
    _('light sensor'),
    _('button'),
    _('button sensor'),
    _('actuator'),
    _('port'),
    _('power'),
    _('turn an actuator')
]

XEVENTS_STRINGS = [
    # Palette to control X11 events
    _('Palette of X11 event blocks'),
    _('setXY'),
    _('set the mouse pointer tox y coordinates'),
    _('getMouseX'),
    _('get the mouse pointer x coordinate'),
    _('getMouseY'),
    _('get the mouse pointer y coordinate'),
    _('leftClick'),
    _('click left click'),
    _('rightClick'),
    _('click right click'),
    _('true'),
    _('false'),
    _('click'),
    _('simulate a mouse click'),
    _('getScreenWidth'),
    _('get the screen width'),
    _('getScreenHeight'),
    _('get the screen height'),
    _('pressButton'),
    _('keeps button pressed'),
    _('releaseButton'),
    _('releases button'),
    _('freeze bar'),
    _('freeze the bar'),
    _('setLineColorRGB'),
    _('set line color from rgb value'),
    _('setLineColor'),
    _('set line color'),
    _('setLineOpacity'),
    _('set line opacity'),
    _('showLine'),
    _('show vertical line over mouse'),
    _('setLineWidth'),
    _('width of vertical line over mouse'),
    _('setLineHeight'),
    _('height of vertical line over mouse'),
    _('setLineWidthAndHeigth'),
    _('set width and height of line over mouse')
]

EXPEYES_STRINGS = [
    #TRANS: plugin to control an ExpEyes device
    _('Palette of Expeyes blocks'),
    # TRANS: Programmable voltage output
    _('set PVS'),
    _('set programmable voltage output'),
    # TRANS: Square wave 1 voltage output
    _('set SQR1 voltage'),
    _('set square wave 1 voltage output'),
    # TRANS: Square wave 2 voltage output
    _('set SQR2 voltage'),
    _('set square wave 2 voltage output'),
    # TRANS: Digital output level
    _('set OD1'),
    _('set digital output level (OD1) low (0) or high (1)'),
    # TRANS: Input 1 voltage level
    _('IN1 level'),
    _('returns 1 if IN1 voltage level >2.5 volts, 0 if IN1 voltage level \
<= 2.5 volts'),
    # TRANS: Input 2 voltage level
    _('IN2 level'),
    _('returns 1 if IN2 voltage level >2.5 volts, 0 if IN2 voltage level \
<= 2.5 volts'),
    # TRANS: Resistive sensor voltage level
    _('SEN level'),
    _('returns 1 if resistive sensor (SEN) voltage level > 2.5 volts, \
0 if SEN voltage level <= 2.5 volts'),
    _('capture'),
    _('input'),
    _('samples'),
    _('interval'),
    # TRANS: MS is microseconds
    _('capture multiple samples from input at interval (MS); results pushed \
to FIFO'),
    # TRANS: Analog input 1 voltage level
    _('A1'),
    _('read analog input 1 voltage'),
    # TRANS: Analog input 2 voltage level
    _('A2'),
    _('read analog input 2 voltage'),
    # TRANS: Read input 1 voltage
    _('IN1'),
    _('read input 1 voltage'),
    # TRANS: Read input 2 voltage
    _('IN2'),
    _('read input 2 voltage'),
    # TRANS: Read analog sensor input voltage
    _('SEN'),
    _('read analog sensor input voltage'),
    # TRANS: Read square wave 1 input voltage
    _('SQR1'),
    _('read square wave 1 voltage'),
    # TRANS: Read square wave 2 input voltage
    _('SQR2'),
    _('read square wave 2 voltage'),
    # TRANS: Read programmable voltage
    _('PVS'),
    _('read programmable voltage'),
    _('Expeyes device not found')
]
