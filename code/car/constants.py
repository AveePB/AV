"""
Module for motor control GPIO pin assignments.

This module defines constants for motor control, including forward and
backward input and enable pins.
"""

# Forward motor control pins
F_IN1 = 38  # Forward input 1
F_IN2 = 36  # Forward input 2
F_IN3 = 37  # Forward input 3
F_IN4 = 35  # Forward input 4
F_ENA = 40  # Forward Enable pin A
F_ENB = 33  # Forward Enable pin B

# Backward motor control pins
B_IN1 = 29  # Backward input 1
B_IN2 = 23  # Backward input 2
B_IN3 = 26  # Backward input 3
B_IN4 = 24  # Backward input 4
B_ENA = 31  # Backward Enable pin A
B_ENB = 22  # Backward Enable pin B

# Default motor duty cycle
MOTOR_PWM = 250

# Deafult motor speed
MOTOR_SPEED = 40