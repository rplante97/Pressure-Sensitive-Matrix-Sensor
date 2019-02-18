import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

def data_gen():
    while(1):
        time.sleep(1)
        data = np.random.rand(40,40)
        return data
        #interrupt

#Code structure
#Script drives/reads from sensor
#Driving script collects and writes data to file or data structure
#Interupt is triggered when a frame is ready
#Data animation is running off of is updated by interrupt
data = np.random.rand(40,40)

harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])

fig, axis = plt.subplots()
image = axis.imshow(harvest)
plt.show()





#Our animation interval is set much faster than we are actually receiving data
#from the mat. Setting it so fast allows us to display new data "on the fly" 
#more or less as soon as it is available from the sensor. This allow us to avoid
#abritrarily limiting the update speed
