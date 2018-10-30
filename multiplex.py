import RPi.GPIO as GPIO
import time
import tkinter
from tkinter import *

#Canvas initialization and size
gui = Tk()
gui.geometry("700x700")
c = Canvas(gui ,width=700 ,height=700)
c.pack()

#Axis and title
gui.title("Sensor Activation Mapping")
c.create_text(350-10,20, text="VCC")
c.create_text(20, 350-10, text="GND", angle =90)

#Create our array of rectangles
for j in range(8):
    for i in range(8):
        c.create_rectangle(40+(i*80),40+(j*80),80+(i*80), 80+(j*80), fill='blue')

#Define our active_sensor object
active_sensor = c.create_rectangle(40+7*80, 40, 80+7*80, 80, fill='red')
#Distance to move activated sensor each update
x_mov = 80
y_mov = 80
#VCC MUX DEFINITIONS
EN = 8
S0 = 10
S1 = 12
S2 = 16
S3 = 18

#GND MUX DEFINITIONS
EN_G = 26
S0_G = 40
S1_G = 38
S2_G = 36
S3_G = 32

#DATA SELECTION MUX DEFINITIONS
#TODO

#Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(EN, GPIO.OUT)
GPIO.setup(S0, GPIO.OUT)
GPIO.setup(S1, GPIO.OUT)
GPIO.setup(S2, GPIO.OUT)
GPIO.setup(S3, GPIO.OUT)
#GND
GPIO.setup(EN_G, GPIO.OUT)
GPIO.setup(S0_G, GPIO.OUT)
GPIO.setup(S1_G, GPIO.OUT)
GPIO.setup(S2_G, GPIO.OUT)
GPIO.setup(S3_G, GPIO.OUT)

#Enable the mux
GPIO.output(EN, 0)
#GND
GPIO.output(EN_G, 0)

#Reset the mux
GPIO.output(S0, 0)
GPIO.output(S1, 0)
GPIO.output(S2, 0)
GPIO.output(S3, 0)
#GND
GPIO.output(S0_G, 0)
GPIO.output(S1_G, 0)
GPIO.output(S2_G, 0)
GPIO.output(S3_G, 0)

pin_control = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000",
               "1001", "1010", "1011", "1100", "1101", "1110", "1111"]

delay = 1
while(1):
    for i in range(8): #VCC
        GPIO.output(S0, int(pin_control[i][3]))
        GPIO.output(S1, int(pin_control[i][2]))
        GPIO.output(S2, int(pin_control[i][1]))
        GPIO.output(S3, int(pin_control[i][0]))
        if (i > 0):
            c.move(active_sensor, -x_mov, 0) #moves the sensor 1 to the left, with the mux
        gui.update()
        #time.sleep(delay)
        for j in range(8): #GND
            GPIO.output(S0_G, int(pin_control[j][3]))
            GPIO.output(S1_G, int(pin_control[j][2]))
            GPIO.output(S2_G, int(pin_control[j][1]))
            GPIO.output(S3_G, int(pin_control[j][0]))
            if (j > 0):
                c.move(active_sensor, 0, y_mov) #moves the sensor 1 to the left, with the mux
            gui.update()
            time.sleep(delay)
        #GND loop over, send sensor back to start
        c.move(active_sensor, 0, y_mov*-7)
    #VCC loop over, send sensor back to start
    c.move(active_sensor,x_mov*7, 0)
gui.mainloop()





        
