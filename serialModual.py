import serial
import fileIOModule
from seiralParser import *

try:
    # ser = serial.Serial(
    #     port='0',
    #     baudrate=9600,
    # )
    ser= serial.Serial('COM1', 9600)
except Exception as ex:
    print('error for connect', ex)

try:
    while True:
        if ser.readable():
            res = ser.readline()
            print(res.decode()[:len(res)-1])
        else:
            print("no signal")
except Exception as ex:
    print('error for serial', ex)