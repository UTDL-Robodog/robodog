#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

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
  delay(10);
}

String command="";
int data=0;
int counter = 0;
void loop() {
  // Call Motorfunction Here
}

void motorFunction(int motorNumber, double angle){
  int pulseLength = (int)map(angle, 0, MAX_ANGLE, SERVOMIN, SERVOMAX);
  pwm.setPWM(motorNumber, 0, pulseLength);
}
