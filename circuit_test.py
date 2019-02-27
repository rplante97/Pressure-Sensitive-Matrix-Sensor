#This file provides robust circuit testing functionality in order to verify
#proper functioning of the electronic circuitry and pressure sensitive mat

from init import * #Import custom init script
import RPi.GPIO as GPIO #GPIO controls
import time
from string import maketrans
from array import *

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
pinout = {
            #VCC 1 (PCB Label: )
            "S0V1" : 3,
            "S1V1" : 5,
            "S2V1" : 7,
            "S3V1" : 11,
            #VCC 2 (PCB Label: )
            "S0V2" : 13,
            "S1V2" : 15,
            "S2V2" : 29,
            "S3V2" : 31,
            #VCC 3 (PCB Label: )
            "S0V3" : 33,
            "S1V3" : 35,
            "S2V3" : 37,
            #GND 1 (PCB Label: )
            "S0G1" : 40,
            "S1G1" : 38,
            "S2G1" : 36,
            "S3G1" : 32,
            #GND 2 (PCB Label: )
            "S0G2" : 26,
            "S1G2" : 22,
            "S2G2" : 18,
            "S3G2" : 16,
            #GND 3 (PCB Label: )
            "S0G3" : 12,
            "S1G3" : 10,
            "S2G3" : 8
            }
#activates a selected sensor for a given amount of time
def activate_sensor(gnd_x, vcc_y, length):
    print 'Activating sensor(',gnd_x,',',vcc_y,') for', length, 'seconds'
    #Determine which gnd mux to target
    pin_ctrl = to_binary(gnd_x)
    if(gnd_x < 16):
        #mux 1
        print 'GND mux 1'
        GPIO.output(pinout.get("S0G1"), int(pin_ctrl[0]))
        GPIO.output(pinout.get("S1G1"), int(pin_ctrl[1]))
        GPIO.output(pinout.get("S2G1"), int(pin_ctrl[2]))
        GPIO.output(pinout.get("S3G1"), int(pin_ctrl[3]))
    elif(gnd_x < 32):
        #mux 2
        pin_ctrl = to_binary(gnd_x-16)
        print 'GND mux 2'
        GPIO.output(pinout.get("S0G2"), int(pin_ctrl[0]))
        GPIO.output(pinout.get("S1G2"), int(pin_ctrl[1]))
        GPIO.output(pinout.get("S2G2"), int(pin_ctrl[2]))
        GPIO.output(pinout.get("S3G2"), int(pin_ctrl[3]))
    else:
        #mux 3, check this output might be weird
        print 'GND mux 3'
        pin_ctrl = to_binary(gnd_x-32)
        GPIO.output(pinout.get("S0G3"), int(pin_ctrl[1]))
        GPIO.output(pinout.get("S1G3"), int(pin_ctrl[2]))
        GPIO.output(pinout.get("S2G3"), int(pin_ctrl[3]))
    print 'Output: S0', pin_ctrl[0], 'S1', pin_ctrl[1], 'S2', pin_ctrl[2], 'S3', pin_ctrl[3]
 

    #vcc 0 corresponds to 15, 1 to 14, etc...
    #Determine which vcc mux to target
    pin_ctrl = to_binary(vcc_y)
    if(vcc_y < 16):
        #mux 1
        print 'VCC mux 1'
        GPIO.output(pinout.get("S0V1"), int(pin_ctrl[0]))
        GPIO.output(pinout.get("S1V1"), int(pin_ctrl[1]))
        GPIO.output(pinout.get("S2V1"), int(pin_ctrl[2]))
        GPIO.output(pinout.get("S3V1"), int(pin_ctrl[3]))
    elif(vcc_y < 32):
        #mux 2
        print 'VCC mux 2'
        pin_ctrl = to_binary(vcc_y-16)
        GPIO.output(pinout.get("S0V2"), int(pin_ctrl[0]))
        GPIO.output(pinout.get("S1V2"), int(pin_ctrl[1]))
        GPIO.output(pinout.get("S2V2"), int(pin_ctrl[2]))
        GPIO.output(pinout.get("S3V2"), int(pin_ctrl[3]))
    else:
        #mux 3, check this output might be weird
        print 'VCC mux 3'
        pin_ctrl = to_binary(vcc_y-32)
        GPIO.output(pinout.get("S0V3"), int(pin_ctrl[1]))
        GPIO.output(pinout.get("S1V3"), int(pin_ctrl[2]))
        GPIO.output(pinout.get("S2V3"), int(pin_ctrl[3]))
    print 'Output: S0', pin_ctrl[0], 'S1', pin_ctrl[1], 'S2', pin_ctrl[2], 'S3', pin_ctrl[3]
    
    #Activate for set amount of time
    time.sleep(length)
    reset_gpio()

def to_binary(integer):
    binary = '{0:04b}'.format(integer)
    binary = binary.translate(maketrans("10", "01"))
    return binary

def reset_gpio():
    GPIO.output(pinout.values(), 0)


hardware_init(0)
value = [[0 for x in range(40)] for y in range(40)]
for x in range(40):
    for y in range(40):
        activate_sensor(x, y, 0.001)
        if(y < 16):
            value[x][y] = mcp.read_adc(0)
        elif(y < 32):
            value[x][y] = mcp.read_adc(1)
        else:
            value[x][y] = mcp.read_adc(2)
print value
GPIO.cleanup()
##
    #1000 == 8
    #0111 == 7

#    1001 == 9
#    0110 == 6

#    15 14 13 12 11 10 9 8 7 6  5  4  3  2  1  0
#    0  1  2  3  4  5  6 7 8 9 10 11 12 13 14 15
