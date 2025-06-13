/**
 * @file linesensor.h
 * @brief Contains LineSensor class.
 *
 * File has LineSensor class and allows for smooth read of information.
 *
 * @author Michał Zientek
 */

#pragma once
#ifndef LINESENSOR_H
#define LINESENSOR_H

#include "motors.h"

/**
 * @enum LineSensorConst
 * @brief Defines constants for line sensor read.
 */
enum class LineSensorConst {
  D1 = 44, ///< first digital input pin
  D2 = 46, ///< second digital input pin
  D3 = 48, ///< third digital input pin
  D4 = 50, ///< fourth digital input pin
  D5 = 52, ///< fifth digital input pin
};

/**
 * @class LineSensor
 * @brief Allows for easy read of information from Maker Line (Cytron).
 *
 * Class reads digital signal from the sensor in form of array (5 elements).
 */
class LineSensor {
  public:

  /**
   * @brief Construct line sensor object.
   */
  LineSensor();

  /**
   * @brief Destroy line sensor object.
   */
  ~LineSensor();

  /**
   * @brief Construct line sensor object with default parameters.
   * @param d1 first digital input pin.
   * @param d2 second digital input pin.
   * @param d3 third digital input pin.
   * @param d4 fourth digital input pin.
   * @param d5 fifth digital input pin.
   */
  LineSensor(int d1, int d2, int d3, int d4, int d5);

  /**
   * @brief Checks current position on the line.
   *
   * Function reads digital inputs and returns the recommended movement to correct the maneuver.
   */
  Movement follow();

  private:
  int d1; ///< first digital input pin
  int d2; ///< second digital input pin
  int d3; ///< third digital input pin
  int d4; ///< fourth digital input pin
  int d5; ///< fifth digital input pin
  int* in; ///< dynamicly allocated int array
};

#endif