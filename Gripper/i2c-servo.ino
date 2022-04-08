/*************************************************** 
  This is an example for our Adafruit 16-channel PWM & Servo driver
  Servo test - this will drive 8 servos, one after the other on the
  first 8 pins of the PCA9685

  Pick one up today in the adafruit shop!
  ------> http://www.adafruit.com/products/815
  
  These drivers use I2C to communicate, 2 pins are required to  
  interface.

  Adafruit invests time and resources providing this open source code, 
  please support Adafruit and open-source hardware by purchasing 
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.  
  BSD license, all text above must be included in any redistribution
 ****************************************************/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

/*
 * Find out what servos we are using and test them individually
 * Develop a naming and numbering scheme for each servo that will use this
 */

/* 
 *  Minimum PWM Pulse Length = 280
 *  Minimum Pulse Length in Microseconds = 450.2 (rounded down to 450)
 *  Maximum PWM Pulse Length = 1583
 *  Maximum Pulse Length in Microseconds = 2545.1 (rounded down to 2545)
 *  Actual Maximum angle the motor is able to traverse = 270.4 deg. Minimum is 0 deg.
*/
#define MAX_ANGLE 270
#define SERVOMIN  280
#define SERVOMAX  1583
#define USMIN  450
#define USMAX  2545
#define SERVO_FREQ 150

// our servo # counter
uint8_t servonum = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("8 channel Servo test!");
  pwm.begin();
  // Setting Oscillator Frequency as 25MHz gives observed Servo Frequency as 151.8 Hz
  pwm.setOscillatorFrequency(25000000);
  pwm.setPWMFreq(SERVO_FREQ);

  /*
   * Motor numbers and calculated motor angles must come to teensy board using some wire inputs
   * Initialize those over here
   * Which ports will be used for those inputs?
   */

  delay(10);
}

String command="";
int data=0;
int counter = 0;
void loop() {
  /*
   * Using the input ports on the teensy, send the input parameters to motorFunction to control any motor
   */
   
  /*
   * Test 1: Calibration of Motor
   * Code to test the minimum and maximum pulse lengths
   if(Serial.available())
   {
    data = Serial.parseInt();
     if (Serial.read() == '\n') {
      pwm.setPWM(0, 0, data);
      pwm.setPWM(1, 0, data);
      Serial.println(data);
      }
   }
   */

   /*
    * Test 2: Multiple Motors
    * 1. Does it work for one motor?
    * YES
    
    * 2. Does it work for multiple motors?
    * YES
    
    * 3. Do the motors get driven in parallel (at the same time) or one by one?
    * AT THE SAME TIME
    
    * 4. What happens when a motor is given a faulty angle (ex. beyond it's range)
    * DOES NOT ROTATE
    
    * 5. Can it handle different motors on the same bus? (we won't have all the same kind of motors)
    * THEORETICALLY YES. STILL NEED TO TEST WHEN THE MOTORS ARE AVAILABLE.
    
    * 6. How long does it take the motor to cover it's full range of motion (max time)? 
    * TRIED TO TIME USING CODE, BUT ALWAYS SHOWS 1ms
    * ACC. TO DATASHEET, SPEED = 0.12s / 60deg => 270deg SHOULD TAKE 540ms.
    * LINK TO DATASHEET = https://www.robotics.org.za/DS3235-270
    */
}

void motorFunction(int motorNumber, double angle){
  /*
   * We convert input angle to pulseLength
   * We pass pulseLength to setPWM so that servoNumber <motorNumber> will be HIGH from tick 0 to tick <pulseLength>
   */
  int pulseLength = (int)map(angle, 0, MAX_ANGLE, SERVOMIN, SERVOMAX);
  pwm.setPWM(motorNumber, 0, pulseLength);
}
