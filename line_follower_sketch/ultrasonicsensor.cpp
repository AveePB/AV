/**
 * @file ultrasonicsensor.cpp
 * @brief File contains the implementation of the UltrasonicSensor class.
 *
 * File has UltrasonicSensor class, that gives us information about what's before the robot.
 *
 * @author Michał Zientek
 */

#include <Arduino.h>
#include "ultrasonicsensor.h"

/**
 * @brief Construct ultrasonic sensor object.
 */
UltrasonicSensor::UltrasonicSensor() {

}

/**
 * @brief Construct ultrasonic sensor object with default parameters.
 * @param trig first analog output pin.
 * @param echo first analog input pin.
 * @param sensingDistance sensing distance of the ultrasonic sensor [cm].
 */
UltrasonicSensor::UltrasonicSensor(int trig, int echo, float sensingDistance) {
  // Initialize variables
  this->trig = trig;
  this->echo = echo;
  this->sensingDistance = sensingDistance;

  // Register pins
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
}

/**
 * @brief Checks if there is obstacle next to the car.
 *
 * Function reads analog input signal and checks if the way is free.
 */
bool UltrasonicSensor::isObstacle() {
  // Read distance
  digitalWrite(this->trig, LOW);
  delayMicroseconds(2);

  digitalWrite(this->trig, HIGH);
  delayMicroseconds(10);

  digitalWrite(this->trig, LOW);

  // Transform received data
  float duration = pulseIn(this->echo, HIGH);
  float distance = (duration * .0343) / 2;

  // Print out data
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println();

  if (distance == 0.0) return false;

  return (distance <= this->sensingDistance);
}

