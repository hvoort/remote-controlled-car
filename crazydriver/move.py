import RPi.GPIO as GPIO
from time import sleep
import sys
import logging as log

log.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', filename='/home/pi/crazydriver/main.log', filemode='a',level=log.DEBUG)


log.info('Move; direction: {}, speed: {}, duration: {}s'.format(sys.argv[1],sys.argv[2], sys.argv[3]))

#set up pin 11,12 as an output
GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
GPIO.setup (12, GPIO.OUT)

frequencyHertz = 50
right = GPIO.PWM (11, frequencyHertz)
left = GPIO.PWM (12, frequencyHertz)

msPerCycle = 1000/frequencyHertz
speed = max(min(float(sys.argv[2]), 99), -99)
time = max(min(float(sys.argv[3]), 3.0), 0.0)
direction = sys.argv[1]

positionRight = speed / (100/1.5) + 1.5

if direction == "FW":
	positionLeft = positionRight
	positionRight = 3 - positionRight
elif direction == "BW":
	positionLeft = 3 - positionRight
	positionRight = positionRight
elif direction == "LEFT":
	positionLeft = 1.5
	positionRight = 3 - positionRight
elif direction == "RIGHT":
	positionLeft = positionRight
	positionRight = 1.5
        
log.debug("position R is %.2f", positionRight)        
log.debug("position L is %.2f", positionLeft)

# duty cycle percentage
dcpRight = positionRight * 100 / msPerCycle
dcpLeft = positionLeft * 100 / msPerCycle

log.debug("dcp R is %.2f", dcpRight)        
log.debug("dcp L is %.2f", dcpLeft)

if positionRight != 1.5:
	right.start(dcpRight)
if positionLeft != 1.5:
	left.start(dcpLeft)

sleep(time)

left.stop ()
right.stop()
GPIO.cleanup ()
