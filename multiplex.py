import RPi.GPIO as GPIO
import time

EN = 8 #Enable pin
S0 = 10
S1 = 12
S2 = 16
S3 = 18

#Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(EN, GPIO.OUT)
GPIO.setup(S0, GPIO.OUT)
GPIO.setup(S1, GPIO.OUT)
GPIO.setup(S2, GPIO.OUT)
GPIO.setup(S3, GPIO.OUT)

#Enable the mux
GPIO.output(EN, 0)

#Reset the mux
GPIO.output(S0, 0)
GPIO.output(S1, 0)
GPIO.output(S2, 0)
GPIO.output(S3, 0)

pin_control = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000",
               "1001", "1010", "1011", "1100", "1101", "1110", "1111"]


while(1):
    for i in range(16):
        GPIO.output(S0, int(pin_control[i][3]))
        GPIO.output(S1, int(pin_control[i][2]))
        GPIO.output(S2, int(pin_control[i][1]))
        GPIO.output(S3, int(pin_control[i][0]))
        time.sleep(0.25)
