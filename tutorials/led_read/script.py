import webiopi
import datetime

GPIO = webiopi.GPIO

LIGHT = 3 # GPIO pin using BCM numbering
LED = 15

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(LIGHT, GPIO.IN, GPIO.PUD_DOWN)
    GPIO.setFunction(LED, GPIO.OUT)

# loop function is repeatedly called by WebIOPi 
def loop():
    # gives CPU some time before looping again
    #print "\n LIGHT_value = %d\n" %(GPIO.digitalRead(LIGHT))
    if (GPIO.digitalRead(LIGHT) == GPIO.LOW):
        GPIO.digitalWrite(LED, GPIO.LOW)
		
    if (GPIO.digitalRead(LIGHT) == GPIO.HIGH):
        GPIO.digitalWrite(LED, GPIO.HIGH)
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(LED, GPIO.LOW)
