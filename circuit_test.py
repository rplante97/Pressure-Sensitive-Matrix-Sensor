#This file provides robust circuit testing functionality in order to verify
#proper functioning of the electronic circuitry and pressure sensitive mat

from init import * #Import custom init script
import RPi.GPIO as GPIO #GPIO controls

#activates a selected sensor for a given amount of time
def activate_sensor(gnd_x, vcc_y, time):
    #Determine which gnd mux to target
    if(gnd_x < 16):
        #mux one
    elif(gnd_x < 32):
        #mux two
    else:
        #mux three

    #vcc 0 corresponds to 15, 1 to 14, etc...
    #Determine which vcc mux to target
    pin_ctrl = to_binary(vcc_y)
    if(vcc_y < 16):
        #mux 1
        GPIO.output(pinout("S0V1"), pin_ctrl[0])
        GPIO.output(pinout("S1V1"), pin_ctrl[1])
        GPIO.output(pinout("S2V1"), pin_ctrl[2])
        GPIO.output(pinout("S3V1"), pin_ctrl[3])
    elif(vcc_y < 32):
        #mux 2
        GPIO.output(pinout("S0V2"), pin_ctrl[0])
        GPIO.output(pinout("S1V2"), pin_ctrl[1])
        GPIO.output(pinout("S2V2"), pin_ctrl[2])
        GPIO.output(pinout("S3V2"), pin_ctrl[3])
    else:
        #mux 3, check this output might be weird
        GPIO.output(pinout("S0V3"), pin_ctrl[1])
        GPIO.output(pinout("S1V3"), pin_ctrl[2])
        GPIO.output(pinout("S2V3"), pin_ctrl[3])


def to_binary(int):
    binary = '0:04b'.format(int)
    binary.replace('1', '2').replace('0', '1').replace('2', '0')
    return binary
    #1000 == 8
    #0111 == 7

#    1001 == 9
#    0110 == 6

#    15 14 13 12 11 10 9 8 7 6  5  4  3  2  1  0
#    0  1  2  3  4  5  6 7 8 9 10 11 12 13 14 15
