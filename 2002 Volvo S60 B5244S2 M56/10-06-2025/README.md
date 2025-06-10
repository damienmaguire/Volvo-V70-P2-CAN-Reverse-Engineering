# Log History and Notes: 10.06.2025

## 10-06-2025 15-09 --- car off, unlocked, press unlock on keyfob, car goes back to off.csv

Pressing the unlock button on the keyfob triggers some CAN activity, but the car
goes back to *Off Mode* quite quickly again.

## 10-06-2025 15-22 --- car off, start, drive mostly around 50, accelerate to 120, around 50, shutdown, wait till car is off.csv

This was a drive around and outside of town, the car reached operating temperature.

## 10-06-2025 15-41 --- Key to 2, turn steering wheel right, left, Key off.csv

The steering wheel was moved around several times with the car off, so some jitter
is to be expected.

## 10-06-2025 15-47 --- HVAC.csv

This log (potentially) has the CAN messages on the LOSPEED CAN bus for the HVAC system.
Note: There are potentially some messages on the HISPEED CAN bus as well when the AC
compressor cycles.

The order of the buttons pressed is the following:
- Initial State: Recirculation on Automatic
- Button Pressed: Recirculation off
- Button Pressed: Recirculation on Manual Override
- Button Pressed: Recirculation on Automatic

- Initial State: Blower Fan off
- Knob Turned: Step 1
- Knob Turned: Step 2
- Knob Turned: Step 3
- Knob Turned: Step 4
- Knob Turned: Step 5
- Knob Turned: Step 6
- Knob Turned: Step 7
- Knob Turned: Step 6
- Knob Turned: Step 5
- Knob Turned: Step 4
- Knob Turned: Step 3
- Knob Turned: Step 2
- Knob Turned: Step 1

- Initial State: AC is on
- Button Press: AC is off
- Button Press: AC is on

- Initial State: Left Temperature Control on 20°C
- Knob Turned: 19°C
- Knob Turned: 18°C
- Knob Turned: 17°C
- Knob Turned: 16°C (minimum)
- Knob Turned: 17°C
- Knob Turned: 18°C
- Knob Turned: 19°C
- Knob Turned: 20°C
- Knob Turned: 21°C
- Knob Turned: 22°C
- Knob Turned: 23°C
- Knob Turned: 24°C
- Knob Turned: 25°C
- Knob Turned: 26°C
- Knob Turned: 27°C
- Knob Turned: 28°C (maximum)
- Knob Turned: 27°C
- Knob Turned: 26°C
- Knob Turned: 25°C
- Knob Turned: 24°C
- Knob Turned: 23°C
- Knob Turned: 22°C
- Knob Turned: 21°C
- Knob Turned: 20°C

- Initial State: Right Temperature Control on 20°C
- Knob Turned: 19°C
- Knob Turned: 18°C
- Knob Turned: 17°C
- Knob Turned: 16°C (minimum)
- Knob Turned: 17°C
- Knob Turned: 18°C
- Knob Turned: 19°C
- Knob Turned: 20°C
- Knob Turned: 21°C
- Knob Turned: 22°C
- Knob Turned: 23°C
- Knob Turned: 24°C
- Knob Turned: 25°C
- Knob Turned: 26°C
- Knob Turned: 27°C
- Knob Turned: 28°C (maximum)
- Knob Turned: 27°C
- Knob Turned: 26°C
- Knob Turned: 25°C
- Knob Turned: 24°C
- Knob Turned: 23°C
- Knob Turned: 22°C
- Knob Turned: 21°C
- Knob Turned: 20°C

- Initial State: Rear Window Heater off
- Button Press: No reaction (car is not in Igition 2)

- Initial State: Windshield Defrost off
- Button Press: on (Fan turned off?)
- Button Press: off

- Initial State: Ventilation Outlets on Auto
- Button Press: Top Vents on
- Button Press: Top Vents off (back to Auto)
- Button Press: Mid Vents on
- Button Press: Mid Vents off (back to Auto)
- Button Press: Foot Vents on
- Button Press: Foot Vents off (back to Auto)
- Button Press: Top Vents on
- Button Press: Mid Vents on
- Button Press: Foot Vents on
- Button Press: Top Vents off
- Button Press: Mid Vents off
- Button Press: Foot Vents off

- Ignition off

## 10-06-2025 15-50 --- Driver Door Module.csv

This log (potentially) has the CAN messages on the LOSPEED CAN bus for
the driver door module (DDM).
The car was in *Sleepy Mode* when starting the log and the key was turned from
Off to 1 during the log and then turned back off at the end of the log.

For the rear windows, there is no second stage in the buttons, so they don't
wind down or up automatically.

The order of the button presses:
- Initial State: Driver Window up
- Button Press: Lower Front Driver Window, Stage 1, hold until window is down
- Button Press: Raise Front Driver Window, Stage 1, hold until window is up
- Button Press: Lower Front Driver Window, Stage 2 (Automatic)
- Button Press: Raise Front Driver Window, Stage 2
- Button Press: Lower Front Passenger Window, Stage 1, hold until window is down
- Button Press: Raise Front Passenger Window, Stage 1, hold until window is up
- Button Press: Lower Front Passenger Window, Stage 2 (Automatic)
- Button Press: Raise Front Passenger Window, Stage 2
- Button Press: Lower Rear Driver Window, Stage 1, hold until window is down
- Button Press: Raise Rear Driver Window, Stage 1, hold until window is up
- Button Press: Lower Rear Passenger Window, Stage 1, hold until window is down
- Button Press: Raise Rear Passenger Window, Stage 1, hold until window is up

- Initial State: Side Mirror somewhere in the middle
- Button Press: Select Left Mirror
- Joystick Move: Left
- Joystick Move: Right
- Joystick Move: Up
- Joystick Move: Down
- Button Press: Select Right Mirror
- Joystick Move: Left
- Joystick Move: Right
- Joystick Move: Up
- Joystick Move: Down
- Button Press: Deselect Mirrors

- Initial State: Car is unlocked
- Button Press: Lock car
- Button Press: Car does not unlock
- Button Press: Enable Child Protection for the rear doors (disable door handles)
- Button Press: Disable Child Protection for the rear doors (enable door handles)

- Initial State: All doors locked
- Pull Lever: Driver Front Door, open door, close door
- Pull Lever: Passenger Front Door, open door, close door
- Pull Lever: Driver Rear Door, open door, close door
- Pull Lever: Passenger Rear Door, open door, close door


## 10-06-2025 15-53 --- Lights.csv

The ignition was set from off to 2 at the start of the recording and back to off
at the end of the recording.

- Initial State: Light is off
- Turn Knob: Position Lights
- Turn Knob: Driving Light
- Button Press: Front Fog Lights on
- Button Press: Front Fog Lights off
- Button Press: Rear Fog Light on
- Button Press: Rear Fog Light off

- Initial State: Headlight Height Adjustment on 0
- Move adjustment to lowest
- Move adjustment to highest

- Initial State: Instrument Cluster Brightness on Max
- Move adjustment to darkest
- Move adjustment to brightest

- Move stalk: Indicator Left
- Move stalk: Indicator Right
- Move stalk: Inicators off
- Button Press: Hazards on
- Button Press: Hazards off

- Move stalk: Momentary high beam (2 or 3 times)
- Move stalk: High Beam on
- Move stalk: High Beam off
- Move stalk: High Beam on
- Move stalk: High Beam off