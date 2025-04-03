"""
    Module responsible for storing constants used for communication with electronic components e.g. leds, motors etc.
"""

# Motor pin constants
F_ENA = 21 #'GPIO21'
F_IN1 = 20 #'GPIO20'
F_IN2 = 16 #'GPIO16'
F_IN3 = 26 #'GPIO26'
F_IN4 = 19 #'GPIO19'
F_ENB = 13 #'GPIO13'

B_ENA = 24 #'GPIO24'
B_IN1 = 23 #'GPIO23'
B_IN2 = 18 #'GPIO18'
B_IN3 = 22 #'GPIO22'
B_IN4 = 27 #'GPIO27'
B_ENB = 17 #'GPIO17'

MOTOR_SPEED = 0.5

# Camera parameters
IMG_FORMAT = 'RGB888'
IMG_SIZE = (1920, 1080)

# Lidar data
LIDAR_USB_HEADER = 'dev/ttyUSB0'
LIDAR_SCAN_SIZE = 2500
