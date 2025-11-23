import serial
import time

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=1)
time.sleep(2)

while True:
    msg = input("Enter message to send: ")
    arduino.write(msg.encode())
    print("Sent:", msg)
