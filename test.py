import serial
import time

# Define the serial port and baud rate
serial_port = '/dev/serial0'  # Adjust this to match your setup
baud_rate = 57600  # Adjust this to match your Pixhawk's baud rate

# Create a serial connection
ser = serial.Serial(serial_port, baud_rate, timeout=1)

try:
    # Send a test command
    ser.write(b"test_command\n")

    # Wait for a response
    response = ser.readline().decode('utf-8')

    # Print the response
    print(f"Received response from Pixhawk: {response}")

except serial.SerialException as e:
    print(f"Serial connection error: {e}")

finally:
    # Close the serial connection
    ser.close()
