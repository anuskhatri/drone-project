# Integration of raspberry pi with pixhawk- By Anus

## modules requires

- Dronekit
- Dronekit-sitl
- PyMavlink
- MavProxy

## Run script

#### Command to run file:-

- python3 test.py --master=/dev/serial0 --baudrate 921600 --aircra

#### Output:-
- ft MyCopter
- CRITICAL:autopilot:PreArm: RC not found
- CRITICAL:autopilot:PreArm: Hardware safety switch
- CRITICAL:autopilot:PreArm: Compass not calibrated
- Vehicle ID: 1.0
- GPS Fix: 0

# Autonomous flight
#### Documentation [https://dronekit-python.readthedocs.io/en/latest/guide/auto_mode.html]

#### Documentation [https://mavlink.io/en/messages/common.html#MAV_GOTO_HOLD_AT_SPECIFIED_POSITION]
- NAVigation commands (MAV_CMD_NAV_*) are used to control vehicle movement, including takeoff, moving to and around waypoints, changing altitude, and landing.
- DO commands (MAV_CMD_DO_*) are for auxiliary functions that do not affect the vehicle’s position (for example, setting the camera trigger distance, or setting a servo value).
- CONDITION commands (MAV_CMD_NAV_*) are used to delay DO commands until some condition is met. 
- For example MAV_CMD_CONDITION_DISTANCE will prevent DO commands executing until the vehicle reaches the specified distance from the waypoint.


#### 