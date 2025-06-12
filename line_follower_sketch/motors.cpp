/**
 * @file motors.cpp
 * @brief Implementation of the Motors functionality.
 *
 * File contains the implementation details of the Motors methods,
 * which handle logic for motor control.
 *
 * @author Michał Zientek
 */

#include <Arduino.h>
#include "motors.h"

/**
   * @brief Construct a new Motors object.
   */
Motors::Motors();

/**
  * @brief Construct a new Motors object and inititializes pins.
  * @param en The Arduino pwm pin connected to the motor driver.
  * @param in1 The Arduino input backward pin connected to the motor driver.
  * @param in2 The Arduino input forward pin connected to the motor driver.
  * @param speed The motor speed (0-255).
  */
Motors::Motors(int en, int in1, int in2, int speed) {
  // Set up object values
  this->en = en;
  this->in1 = in1;
  this->in2 = in2;
  this->speed = speed;

  // Register motor pins
  pinMode(en, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

  // Set speed
  analogWrite(en, speed);
}

/**
  * @brief Set the motor speed.
  * @param speed The new motor speed (0-255).
  */
void Motors::setSpeed(int speed) {
  // Update motor speed
  this->speed = speed;
  analogWrite(this->en, speed);
}

/**
 * @brief Get the motor speed.
 */
int Motors::getSpeed() {
  return this->speed;
}

/**
 * @brief Change spin direction to forward.
 */
void Motors::moveForward() {
  digitalWrite(this->in1, LOW);
  digitalWrite(this->in2, HIGH);
}

/**
  * @brief Change spin direction to backward.
  */
void Motors::moveBackward() {
  digitalWrite(this->in1, HIGH);
  digitalWrite(this->in2, LOW);
}

/**
  * @brief Stop spining.
  */
void Motors::stop() {
  digitalWrite(this->in1, LOW);
  digitalWrite(this->in2, LOW);
}