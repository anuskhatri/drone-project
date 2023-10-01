from dronekit import connect, VehicleMode

# Define the serial port and baud rate for MAVLink communication
serial_port = '/dev/serial0'  # Replace with the correct serial port for your Pixhawk connection
baud_rate = 57600  # Adjust this to match your Pixhawk's baud rate

# Connect to the Vehicle
print('Connecting to vehicle on: %s' % serial_port)
vehicle = connect(serial_port, baud=baud_rate, wait_ready=True)

try:
    print("Forcing arming...")
    
    # Set the force_arm parameter to True
    vehicle.parameters['ARMING_CHECK'] = 0
    vehicle.parameters['ARMING_REQUIRE'] = 0
    vehicle.parameters['FORCE_ARM'] = 1
    
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print("Waiting for arming...")
        time.sleep(1)

    print("Vehicle is armed.")

    # You can add your specific actions here

finally:
    # Close the vehicle object
    vehicle.close()
