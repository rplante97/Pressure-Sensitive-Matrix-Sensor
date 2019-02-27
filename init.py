###
###Initialization functions for the pressure sensitive matrix
###

import RPi.GPIO as GPIO #GPIO controls
#Hardware SPI librarys for our ADC
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008



def hardware_init(spi):
    #Define Pi pin mappings using HARDWARE PIN LABELS
    GPIO.setmode(GPIO.BOARD) #Pin numbering in hardware mode
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
    #Setup hardware SPI
    if(spi):
        SPI_PORT   = 0
        SPI_DEVICE = 0
        mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
    #Initialize pins to output mode and set to 0
    GPIO.setup(pinout.values(), GPIO.OUT)
    GPIO.output(pinout.values(), 0)
