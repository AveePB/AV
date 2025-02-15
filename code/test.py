from car.gpio import *
from car.constants import *
from time import sleep

initializeGPIO()

GPIO.output(F_IN1,GPIO.HIGH)
GPIO.output(F_IN2,GPIO.LOW)

GPIO.output(F_IN3,GPIO.HIGH)
GPIO.output(F_IN4,GPIO.LOW)

p = GPIO.PWM(F_ENA, 4000)
p.start(25)

sleep(5)
p.stop()

cleanUpGPIO()