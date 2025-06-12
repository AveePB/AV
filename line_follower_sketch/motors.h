/**
 * @file motors.h
 * @brief Set of motor related objects and methods.
 *
 * File has an enum MotorConst and Motor object. Those two elements
 * are used to control motors.
 *
 * @author Michał Zientek
 */

#pragma once
#ifndef MOTORS_H
#define MOTORS_H

/**
 * @enum MotorConst
 * @brief Defines constants for motor controls
 */
enum class MotorConst {
  SPEED = 100, ///< Motor speed (0-255)
  ENA = 3, ///< Left motors speed pin 
  ENB = 2, ///< Right motors speed pin
  IN1 = 24, ///< Left motors backward pin
  IN2 = 26, ///< Left motors forward pin
  IN3 = 28, ///< Right motors backward pin
  IN4 = 30, ///< Right motors forward pin
};

/**
 * @class Motors
 * @brief Controls two motors by using PWM signals.
 *
 * Class allows for smooth change of spining direction of the motor.
 */
class Motors {
  public:
  /**
   * @brief Construct a new Motors object.
   */
  Motors();

  /**
   * @brief Construct a new Motors object and inititializes pins.
   * @param en The Arduino pwm pin connected to the motor driver.
   * @param in1 The Arduino input backward pin connected to the motor driver.
   * @param in2 The Arduino input forward pin connected to the motor driver.
   * @param speed The motor speed (0-255).
   */
  Motors(int en, int in1, int in2, int speed);

  /**
   * @brief Set the motor speed.
   * @param speed The new motor speed (0-255).
   */
  void setSpeed(int speed);

  /**
   * @brief Get the motor speed.
   */
  int getSpeed();

  /**
   * @brief Change spin direction to forward.
   */
  void moveForward();

  /**
   * @brief Change spin direction to backward.
   */
  void moveBackward();

  /**
   * @brief Stop spining.
   */
  void stop();

  private:
  int en; ///< PWM pin used for speed control of the motor
  int in1; ///< Backward pin used to change spin direction
  int in2; ///< Forward pin used to change spin direction
  int speed; ///< Speed value (0-255)
};

#endif