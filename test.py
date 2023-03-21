# Program to test serial communication between Python script and Arduino
# by Giovi
# Resources:
# https://forum.arduino.cc/t/demo-sending-binary-data-from-pc-to-arduino/254004

# NOTE : Serial.readBytes is SLOW
# this one is much faster, but has no timeout
# c = Serial.read();


# Importing Libraries
import serial
import time
from struct import *


def arduinoControl(name, value):
    arduino = serial.Serial(port='COM6', baudrate=115200, timeout=.1)

    # Packing all the datas into a string
    #   ?   _Bool       1 byte
    #   h   short int   2 bytes
    #   i   int         4 bytes
    dataToSend = pack('hh', name, value)
    arduino.write(dataToSend)
    time.sleep(0.05)

    if arduino.inWaiting():
        IN_Data = arduino.readline()
        return IN_Data


if __name__ == "__main__":

    """
    def write_read(x):
        arduino.write(x)
        time.sleep(0.05)
        data = arduino.readline()
        return data
    """

    while True:
        speed = int(input("Enter a number: "))  # Taking input from user

        # Each number is associated with an integer (short) value
        # 1     Motor B
        device = 0

        arduinoControl(device, speed)
