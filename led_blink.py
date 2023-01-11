from gpiozero import LED
from time import sleep

led = LED(4)

for i in range (5):
	led.on()
	sleep(0.5)
	led.off()
	sleep(0.5)

