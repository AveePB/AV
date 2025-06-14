/**
 * @file ultrasonicsensor.h
 * @brief File contains the definition of the UltrasonicSensor class.
 *
 * File has UltrasonicSensor class, that gives us information about what's before the robot.
 *
 * @author Michał Zientek
 */

#ifndef ULTRASONICSENSOR_H
#define ULTRASONICSENSOR_H

const float SENSING_DISTANCE = 15.0;

/**
 * @enum UltrasonicSensorConst
 * @brief Defines constants for ultrasonic sensor.
 */
enum class UltrasonicSensorConst {
  TRIG = A1, ///< echo analog output analog pin
  ECHO = A0, ///< trig analog input pin
};

/**
 * @class UltrasonicSensor
 * @brief Allows for easy read of information from Ultrasonic sensor (Cytron).
 *
 * Class reads analog signal from the sensor.
 */
class UltrasonicSensor {
  public:

  /**
   * @brief Construct ultrasonic sensor object.
   */
  UltrasonicSensor();

  /**
   * @brief Construct ultrasonic sensor object with default parameters.
   * @param trig first analog output pin.
   * @param echo first analog input pin.
   * @param sensingDistance sensing distance of the ultrasonic sensor [cm].
   */
  UltrasonicSensor(int trig, int echo, float sensingDistance);

  /**
   * @brief Checks if there is obstacle next to the car.
   *
   * Function reads analog input signal and checks if the way is free.
   */
  bool isObstacle();

  private:
  float sensingDistance; ///< sensing distance of the ultrasonic sensor [cm]
  int trig; ///< analog output pin
  int echo; ///< analog input pin
};

#endif