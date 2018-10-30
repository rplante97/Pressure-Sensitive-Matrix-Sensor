/* Small program to test driving multiplexers in C, makes use of the bcm2835 library to configure GPIO pins.
    This is intended to be a first passthrough implementation to just make sure the hardware will work as intended
    speed/efficiency is not considered.
*/

#include <bcm2835.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define EN 14 //Enable pin
#define S0 2
#define S1 18
#define S2 23
#define S3 24

int main(void){
	
	//Define array to easily iterate through each output
	char pin_control[4][4] = {"0000", "0001", "0010", "0011"};

	if(!bcm2835_init()){
		printf("Init error. Exiting now.");
		return 1;
	}
	
	bcm2835_gpio_write(EN, LOW); 
	bcm2835_delay(500);
	int i;
	
	while(1){
/*
		for(i = 0; i<4; i++){
			printf("S0: %d \n", pin_control[i][0] - '0');
			printf("S1: %d \n", pin_control[i][1] - '0');
			printf("S2: %d \n", pin_control[i][2] - '0');
			printf("S3: %d \n", pin_control[i][3] - '0');
			printf ("\n \n");
			bcm2835_gpio_write(S0, pin_control[i][0] - '0');
			bcm2835_gpio_write(S1, pin_control[i][1] - '0');
			bcm2835_gpio_write(S2, pin_control[i][2] - '0');
			bcm2835_gpio_write(S3, pin_control[i][3] - '0');
			bcm2835_delay(500);
			
		}*/
		bcm2835_gpio_write(S0, LOW);
		bcm2835_delay(500);
		bcm2835_gpio_write(S0, HIGH);
		bcm2835_delay(500);
	}
		bcm2835_close();
		return 0;
}



