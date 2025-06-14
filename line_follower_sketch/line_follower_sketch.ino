#include "motors.h"
#include "linesensor.h"
#include "ultrasonicsensor.h"

// Initialize left motors
Motors leftMTs(static_cast<int>(MotorConst::ENA), 
  static_cast<int>(MotorConst::IN1),
  static_cast<int>(MotorConst::IN2),
  static_cast<int>(MotorConst::SPEED)
);

// Initialize right motors
Motors rightMTs(static_cast<int>(MotorConst::ENB), 
  static_cast<int>(MotorConst::IN3),
  static_cast<int>(MotorConst::IN4),
  static_cast<int>(MotorConst::SPEED)
);

// Initialize line sensor
LineSensor lineSensor(static_cast<int>(LineSensorConst::D1), 
  static_cast<int>(LineSensorConst::D2),
  static_cast<int>(LineSensorConst::D3),
  static_cast<int>(LineSensorConst::D4),
  static_cast<int>(LineSensorConst::D5)
);

// Initialize ultrasonic sensor
UltrasonicSensor ultrasonicSensor(static_cast<int>(UltrasonicSensorConst::TRIG),
  static_cast<int>(UltrasonicSensorConst::ECHO),
  SENSING_DISTANCE
);

void setup() {
  Serial.begin(9600);
}

void loop() {
  bool b = ultrasonicSensor.isObstacle();
  Serial.println(b);
}
