#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
#include <ArduinoJson.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

/* DO NOT CHANGE THESE VALUES */
#define MAX_ANGLE 270
#define SERVOMIN  280
#define SERVOMAX  1583
#define USMIN  450
#define USMAX  2545
#define SERVO_FREQ 150

void setup() {
  pwm.begin();
  pwm.setOscillatorFrequency(25000000);
  pwm.setPWMFreq(SERVO_FREQ);

  /* Creating a sample json document */
  char local[] = "{\"data\": 1}";
  StaticJsonDocument<256> jsonDoc;
  deserializeJson(jsonDoc, local);
  
  delay(10);
}

String command = ""; /* "<MotorID(2)> <NewAngle(any)>" */
String incomingByte = "";
void loop() {
  while(Serial.available()) {
    incomingByte = Serial.read();
    command += incomingByte;
  }

  /* Return if no command was sent */
  if(command == "")
    return;

  int motorID = command.substring(0, 2).toInt();
  double newAngle = command.substring(3).toFloat();
  motorFunction(motorID, newAngle);
  command = "";
}

/*
 * Takes ID of motor and new angle it should be rotated to as inputs
 * Converts angle in degrees to a number represting length of PWM pulse using map()
 * Calculated pulse length is assigned to motor with provided ID using setPWM()
*/
void motorFunction(int motorNumber, double angle){
  int pulseLength = (int)map(angle, 0, MAX_ANGLE, SERVOMIN, SERVOMAX);
  pwm.setPWM(motorNumber, 0, pulseLength);
}
