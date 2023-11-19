from django.shortcuts import render
from django.http import JsonResponse
import serial

def homePage(request):
    # Set the port to the one your Arduino is connected to
    port = 'COM4'  # Change this to your actual port (e.g., COM3 for Windows)

    # Set the baud rate to match the Arduino's baud rate
    baud_rate = 9600

    # Create a serial object
    ser = serial.Serial(port, baud_rate, timeout=1)

    try:
        # Read a line from the serial port
        serial_data = ser.readline().decode('utf-8').strip()

        # Close the serial connection
        ser.close()

        # Print the received data
        print("Received data:", serial_data)

        # Pass the data to the template
        return render(request, "arduino/index.html", {'data': serial_data})

    except Exception as e:
        # Handle exceptions
        return JsonResponse({'error': str(e)})
