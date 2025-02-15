"""
GPIO Handler Module for Motor Control

This module provides functions to initialize and clean up GPIO pins used 
for motor control. It sets the necessary GPIO mode, configures pins as outputs, 
and ensures proper cleanup when the program terminates.    
"""

import RPi.GPIO as GPIO
from car.constants import *

def initializeGPIO():
    """
    Initializes the GPIO pins for motor control.

    This function sets the GPIO mode to BCM and configures both 
    forward and backward motor control pins as outputs. 
    It also ensures all pins start in a LOW state.
    """

    GPIO.setmode(GPIO.BOARD)  # Turn on GPIO

    # Set up forward motor pins
    GPIO.setup(F_IN1, GPIO.OUT); GPIO.output(F_IN1, GPIO.LOW)
    GPIO.setup(F_IN2, GPIO.OUT); GPIO.output(F_IN2, GPIO.LOW)
    GPIO.setup(F_IN3, GPIO.OUT); GPIO.output(F_IN3, GPIO.LOW)
    GPIO.setup(F_IN4, GPIO.OUT); GPIO.output(F_IN4, GPIO.LOW)
    GPIO.setup(F_ENA, GPIO.OUT); GPIO.output(F_ENA, GPIO.LOW)
    GPIO.setup(F_ENB, GPIO.OUT); GPIO.output(F_ENB, GPIO.LOW)

    # Set up backward motor pins
    GPIO.setup(B_IN1, GPIO.OUT); GPIO.output(B_IN1, GPIO.LOW)
    GPIO.setup(B_IN2, GPIO.OUT); GPIO.output(B_IN2, GPIO.LOW)
    GPIO.setup(B_IN3, GPIO.OUT); GPIO.output(B_IN3, GPIO.LOW)
    GPIO.setup(B_IN4, GPIO.OUT); GPIO.output(B_IN4, GPIO.LOW)
    GPIO.setup(B_ENA, GPIO.OUT); GPIO.output(B_ENA, GPIO.LOW)
    GPIO.setup(B_ENB, GPIO.OUT); GPIO.output(B_ENB, GPIO.LOW)

def cleanUpGPIO():
    """
    Cleans up GPIO settings.

    This function resets all GPIO pins and releases resources.
    """
    GPIO.cleanup()
    