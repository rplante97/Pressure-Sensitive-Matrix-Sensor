import time
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
active_sensor = c.create_rectangle(40, 40, 80, 80, fill='red')
#Delay between activations
delay = 0.5
#Distance to move activated sensor each update
x_mov = 80
y_mov = 80
while True:
    #VCC (x-axis) loop
    for i in range(8):
        #do the mux thing
        if (i > 0):
            c.move(active_sensor, x_mov, 0) #moves the sensor 1 to the left, with the mux
        gui.update()
        #GND (y-axis) loop
        for j in range(8):
            if (j > 0):
                c.move(active_sensor, 0, y_mov) #moves the sensor 1 to the left, with the mux
            gui.update()
            time.sleep(delay)
        #GND loop over, send sensor back to start
        c.move(active_sensor, 0, y_mov*-7)
    #VCC loop over, send sensor back to start
    c.move(active_sensor,x_mov*-7, 0)
gui.mainloop()
