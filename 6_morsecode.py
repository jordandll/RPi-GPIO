#!/usr/bin/python3



import os

from time import sleep

import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)

GPIO.setup(22,GPIO.OUT)



loop_count = 0



# define a function called morsecode

def morsecode ():

    #Dot Dot Dot

    GPIO.output(22,GPIO.HIGH)

    sleep(.1)

    GPIO.output(22,GPIO.LOW)

    sleep(.1)

    GPIO.output(22,GPIO.HIGH)

    sleep(.1)

    GPIO.output(22,GPIO.LOW)

    sleep(.1)

    GPIO.output(22,GPIO.HIGH)

    sleep(.1)



    #Dash Dash Dash

    GPIO.output(22,GPIO.LOW)

    sleep(.2)

    GPIO.output(22,GPIO.HIGH)

    sleep(.2)

    GPIO.output(22,GPIO.LOW)

    sleep(.2)

    GPIO.output(22,GPIO.HIGH)

    sleep(.2)

    GPIO.output(22,GPIO.LOW)

    sleep(.2)

    GPIO.output(22,GPIO.HIGH)

    sleep(.2)

    GPIO.output(22,GPIO.LOW)

    sleep(.2)



    #Dot Dot Dot

    GPIO.output(22,GPIO.HIGH)

    sleep(.1)

    GPIO.output(22,GPIO.LOW)

    sleep(.1)

    GPIO.output(22,GPIO.HIGH)

    sleep(.1)

    GPIO.output(22,GPIO.LOW)

    sleep(.1)

    GPIO.output(22,GPIO.HIGH)

    sleep(.1)

    GPIO.output(22,GPIO.LOW)

    sleep(.7)



os.system('clear')

print "Morse Code"



loop_count = input("How many times would you like SOS to loop?: ")



while loop_count > 0:

    loop_count = loop_count - 1

    morsecode ()
