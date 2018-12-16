#3 VCC muxes to loop through, first two on 4 pins , last one 2 pins
#3 GND muxes to loop through, first two on 4 pins , last one 2 pins
#3 Enable lines to (maybe) loop through, 3 pins total
#SPI ADC on 4 pins
#Total pins: 24 + (maybe) 3

import time
import os #Makes the prints to console pretty
import RPi.GPIO as GPIO #GPIO controls
#Hardware SPI librarys for our ADC
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


#Hypothetical Pinout (Hardware Labels)
#VCC 1 (PCB Label: )
S01 = 8
S11 = 8
S21 = 8
S31 = 8

#VCC 2 (PCB Label: )
S02 = 8
S12 = 8
S22 = 8
S32 = 8

#VCC 3 (PCB Label: )
S03 = 8
S13 = 8

#GND 1 (PCB Label: )
S0G1 = 8
S1G1 = 8
S2G1 = 8
S3G1 = 8

#GND 2 (PCB Label: )
S0G2 = 8
S1G2 = 8
S2G2 = 8
S3G2 = 8

#GND 3 (PCB Label: )
S0G3 = 8
S1G3 = 8

#Note: This is for comment consistency. Since library supports Hardware SPI it handles pin assigns for us
#SPI INTERFACE (PCB Label: )
#CLK - SCLK(GPIO 11)(HW 23)
#DOUT - MISO(GPIO 9)(HW 21)
#DIN - MOSI(GPIO 10)(HW 19)
#CS - CE0(GPIO8)(HW 24)

#ENABLES
EN_VCC1 = 0
EN_VCC2 = 0
EN_VCC3 = 0

#Basic program flow:
#Step 1: A VCC mux line is selected, pulling that line high (this also pulls the same line on the data muxes high)
#Step 2: A GND mux line is selected, pulling that line low
#Step 3: An ADC read is triggered
#Step 4: The GND mux line selection is incremented by one, loop to step 3
#Step 5: Once all 40 GND mux lines have been gone through increment VCC select line by one, loop to step 3

#Notes: Since we are using 3 muxes to select the 40 inputs/outputs things get a little weird
#After 16 increments we switch the pins we are using, then after 16 more we switch again but only increment 8
#If we have enough pins we want to keep the other two inactive vcc muxes disable while we are reading from the other

#The multiplexers need about max 60 nanoseconds to change their states. With a super optimized program written in C
#or assembly on a microcontroller this may be something to consider. For our uses (especially w/ Python) our code will
#execute plenty slow to allow the multiplexers the time they need

#GPIO Setup: Setting all 20 mux control pins to outputs
GPIO.setwarnings(False) #Mutes irrelevant warnings
GPIO.setmode(GPIO.BOARD) #Pin numbering in hardware mode
#VCC MUXES
GPIO.setup(S01, GPIO.OUT)
GPIO.setup(S11, GPIO.OUT)
GPIO.setup(S21, GPIO.OUT)
GPIO.setup(S31, GPIO.OUT)
GPIO.setup(S02, GPIO.OUT)
GPIO.setup(S12, GPIO.OUT)
GPIO.setup(S22, GPIO.OUT)
GPIO.setup(S32, GPIO.OUT)
GPIO.setup(S03, GPIO.OUT)
GPIO.setup(S13, GPIO.OUT)

#GND MUXES
GPIO.setup(S0G1, GPIO.OUT)
GPIO.setup(S1G1, GPIO.OUT)
GPIO.setup(S2G1, GPIO.OUT)
GPIO.setup(S3G1, GPIO.OUT)
GPIO.setup(S0G2, GPIO.OUT)
GPIO.setup(S1G2, GPIO.OUT)
GPIO.setup(S2G2, GPIO.OUT)
GPIO.setup(S3G2, GPIO.OUT)
GPIO.setup(S0G3, GPIO.OUT)
GPIO.setup(S1G3, GPIO.OUT)

#Enable Lines (RESERVED)

#Reset all GPIO outputs to 0
#VCC
GPIO.output(S01, 0)
GPIO.output(S11, 0)
GPIO.output(S21, 0)
GPIO.output(S31, 0)
GPIO.output(S02, 0)
GPIO.output(S12, 0)
GPIO.output(S22, 0)
GPIO.output(S32, 0)
GPIO.output(S03, 0)
GPIO.output(S13, 0)

#GND
GPIO.output(S0G1, 0)
GPIO.output(S1G1, 0)
GPIO.output(S2G1, 0)
GPIO.output(S3G1, 0)
GPIO.output(S0G2, 0)
GPIO.output(S1G2, 0)
GPIO.output(S2G2, 0)
GPIO.output(S3G2, 0)
GPIO.output(S0G3, 0)
GPIO.output(S1G3, 0)

#Maps out all 40 states the multiplexers need to step through, in order
pin_control = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000",
               "1001", "1010", "1011", "1100", "1101", "1110", "1111", "0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000",
               "1001", "1010", "1011", "1100", "1101", "1110", "1111", "0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111"]

#Our main program loop: iterate through the 40x40 array and read in values
while(1):
    start_time = time.time() #Start of scan
    #VCC ITERATION
    for i in range(40):
        if(i < 15): #First VCC mux
            test = 1
        elif(i < 32): #Second VCC mux
            test = 1
        elif(i < 40): #Third VCC mux
            test = 1
        else: #No idea how we would EVER get here, but can't hurt
            test = 1
        
        
        #GND ITERATION
        for j in range(40):
            if(j < 15): #The first GND mux
                test = 1
            elif (j < 32): #The second GND mux
                test = 1
            elif (j < 40): #The third GND mux
                test = 1
            else:
                test = 1
            #Read the ADC here
            #values[i][j] = adcread function
    #Print 2D array
    end_time = time.time() #End of matrix scan
    print('It took %s seconds to scan through the matrix 1 time' % (end_time - start_time))
#END WHILE