#MCP3008 PIN CONNECTIONS
#CH0 - PCB Signal Line
#VDD - 5V
#VREF - 5V
#AGND - GND
#CLK - SCLK(GPIO 11)(HW 23)
#DOUT - MISO(GPIO 9)(HW 21)
#DIN - MOSI(GPIO 10)(HW 19)
#CS - CE0(GPIO8)(HW 24)
#DGND - GND

#Test script to read values from the ADC
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#Allows us to test ADC read/SPI speed without much Python overhead
from itertools import repeat

#SPI Pin configuration
SPI_PORT = 0
SPI_DEVICE = 0

mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))



print("Ctrl-C to quit")
print("Channel 0: ")
start_t = time.time()
for unused in repeat(None, 3200):
    del unused
    print(mcp.read_adc(0))
end_t = time.time()
print("Execution time: %s seconds" % (end_t - start_t))