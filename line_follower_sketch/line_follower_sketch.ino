#include "motors.h"

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

void setup() {

}

void loop() {
  leftMTs.moveForward();
  rightMTs.moveForward();
  delay(1000);

  leftMTs.stop();
  rightMTs.stop();
  delay(1000);

  leftMTs.moveBackward();
  rightMTs.moveBackward();
  delay(1000);

  leftMTs.stop();
  rightMTs.stop();
  delay(1000);
}
