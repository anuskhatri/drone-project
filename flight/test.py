from dronekit import connect
# server/controller/api_controller.py

from flask import request, jsonify

def get_resource():
    data = {"message": "This is a GET request to the API resource."}
    return jsonify(data)

def post_resource():
    data = request.get_json()
    try:
        # Connect to the Pixhawk using the USB serial connection
        vehicle = connect('/dev/serial0', baud=921600)

        # Print some vehicle information
        print(f"Vehicle ID: {vehicle.parameters['SYSID_THISMAV']}")
        print(f"GPS Fix: {vehicle.gps_0.fix_type}")

        # Close the connection
        vehicle.close()
        response = {"message": "Successful test"}
        return jsonify(response)
    except Exception as e:
        print(e)
        response = {"message": "Test failed"}
        return jsonify(response)



# Command to run file:-
# python3 test.py --master=/dev/serial0 --baudrate 921600 --aircra
# Output:-
# ft MyCopter
# CRITICAL:autopilot:PreArm: RC not found
# CRITICAL:autopilot:PreArm: Hardware safety switch
# CRITICAL:autopilot:PreArm: Compass not calibrated
# Vehicle ID: 1.0
# GPS Fix: 0