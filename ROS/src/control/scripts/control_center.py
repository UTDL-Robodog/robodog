#!/usr/bin/env
import rospy
from std_msgs.msg import String
import json
import os

VALID_COMMANDS = ['off', 'walk', 'grab', 'return', 'standby']
MOTOR_SCHEMA = "../../../other/motors.json"

class RobotControl:
    def __init__(self):

        wd = os.path.dirname(__file__)
        with open(os.path.join(wd,MOTOR_SCHEMA)) as motor_json:
            self.motor_states = json.load(motor_json) # object to hold motor states

        self.mode = 'off' # current operating mode - Modes: off, walk, grab, return, standby

        rospy.init_node('control_center', anonymous=True)

        self.pub_motor_commands = rospy.Publisher('motor_commands', String, queue_size=10)
        rospy.Subscriber('mode_commands', String, self.update_mode)
        rospy.Subscriber('motor_feedback', String, self.update_motors)

    def update_mode(self, data): # update the operating mode
        if data.data in VALID_COMMANDS:
            self.mode = data.data
            rospy.loginfo('Operating mode changed to: ' + str(data.data))
        else:
            rospy.logwarn(str(data.data) + ' is not a valid operating mode')
    
    def update_motors(self, data): # update the motor states
        data_json = json.loads(data.data)
        if self.motor_states.keys() == data_json.keys() and self.motor_states != data_json: # verify that json keys are valid (same number of motors)
            self.motor_states = data_json
            rospy.loginfo('Motor angles updated')
        elif self.motor_states == data_json: # if format is valid but motor angles haven't changed, do nothing
            pass
        else: # if motor update is invalid
            rospy.logwarn('Invalid motor angle update')


    def run(self): # run the node's publisher
        r = rospy.Rate(1)
        while not rospy.is_shutdown():

            # WILL HOUSE LOGIC BODY FOR DECISION MAKING

            if self.mode == 'off':
                pass
            elif self.mode == 'walk':
                pass
            elif self.mode == 'grab':
                pass
            elif self.mode == 'return':
                pass
            elif self.mode == 'standby':
                pass
            
            print(self.mode)
            print(self.motor_states["1"]["angle"])
            r.sleep()

if __name__=='__main__':
    try:
        robot = RobotControl()
        robot.run()
    except rospy.ROSInterruptException: # if we ctrl+C to interrupt ROS
        pass
    except Exception as e:
        print(e)