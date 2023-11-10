from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")
from django.http import JsonResponse
import serial

def arduino_data(request):
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

        # Return the data as JSON response
        return JsonResponse({'data': serial_data})

    except Exception as e:
        # Handle exceptions
        return JsonResponse({'error': str(e)})
