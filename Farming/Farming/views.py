from django.shortcuts import render
from django.http import JsonResponse
import serial
import serial.tools.list_ports

# Function to find the Arduino port
def find_arduino_port():
    arduino_ports = [
        p.device
        for p in serial.tools.list_ports.comports()
        if 'Arduino' in p.description
    ]
    if arduino_ports:
        return arduino_ports[0]
    else:
        raise Exception("Arduino not found. Check the connection.")

# Create a global serial object
arduino_serial = None

def homePage(request):
    return render(request, "index.html")

def arduino_data(request):
    global arduino_serial

    try:
        # Initialize the serial port if not already open
        if arduino_serial is None or not arduino_serial.is_open:
            arduino_port = find_arduino_port()
            arduino_serial = serial.Serial(arduino_port, 9600, timeout=1)

        # Read a line from the serial port
        serial_data = arduino_serial.readline().decode('utf-8').strip()

        # Print the received data
        print("Received data:", serial_data)

        # Return the data as JSON response
        return JsonResponse({'data': serial_data})

    except serial.SerialException as e:
        # Handle serial communication issues
        return JsonResponse({'error': f'Serial communication error: {str(e)}'})

    except Exception as e:
        # Handle other exceptions
        return JsonResponse({'error': str(e)})
