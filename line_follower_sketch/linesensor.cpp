/**
 * @file linesensor.cpp
 * @brief File contains the implementation of the LineSensor class.
 *
 * File has implementations of the functions seen in theLineSensor class.
 *
 * @author Michał Zientek
 */

#include <Arduino.h>
#include "linesensor.h"
#include "motors.h"

/**
 * @brief Construct line sensor object.
 */
LineSensor::LineSensor() {

}

/**
  * @brief Destroy line sensor object.
  */
LineSensor::~LineSensor() {
  free(this->in);
}

/**
 * @brief Construct line sensor object with default parameters.
 * @param d1 first digital input pin.
 * @param d2 second digital input pin.
 * @param d3 third digital input pin.
 * @param d4 fourth digital input pin.
 * @param d5 fifth digital input pin.
 */
LineSensor::LineSensor(int d1, int d2, int d3, int d4, int d5) {
  // Initialize variables
  this->d1 = d1;
  this->d2 = d2;
  this->d3 = d3;
  this->d4 = d4;
  this->d5 = d5;
  this->in = new int[5];

  // Register digital pins
  pinMode(d1, INPUT);
  pinMode(d2, INPUT);
  pinMode(d3, INPUT);
  pinMode(d4, INPUT);
  pinMode(d5, INPUT);
}

/**
 * @brief Checks current position on the line.
 *
 * Function reads digital inputs and returns the recommended movement to correct the maneuver.
 */
Movement LineSensor::follow() {
  // Initialize and read data
  in[0] = digitalRead(this->d1); Serial.print(in[0]); Serial.print(' ');
  in[1] = digitalRead(this->d2); Serial.print(in[1]); Serial.print(' ');
  in[2] = digitalRead(this->d3); Serial.print(in[2]); Serial.print(' ');
  in[3] = digitalRead(this->d4); Serial.print(in[3]); Serial.print(' ');
  in[4] = digitalRead(this->d5); Serial.print(in[4]); Serial.print(' ');
  Serial.println();

  // Robot logic....

  return Movement::STOP;
}