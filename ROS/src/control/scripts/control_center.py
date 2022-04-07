#!/usr/bin/env
import rospy
from std_msgs.msg import String

VALID_COMMANDS = ['off', 'walk', 'grab', 'return', 'standby']

class RobotControl:
    def __init__(self):
        self.motor_states = dict() # object to hold motor states
        self.mode = 'off' # current operating mode - Modes: off, walk, grab, return, standby

        rospy.init_node('control_center', anonymous=True)

        self.pub_motor_commands = rospy.Publisher('motor_commands', String, queue_size=10)
        rospy.Subscriber('mode_commands', String, self.update_mode)

    def update_mode(self, data):
        if data.data in VALID_COMMANDS:
            self.mode = data.data
            rospy.loginfo('Operating mode changed to: ' + str(data.data))
        else:
            rospy.logwarn(str(data.data) + ' is not a valid operating mode')

    def run(self):
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
            r.sleep()

if __name__=='__main__':
    try:
        robot = RobotControl()
        robot.run()
    except rospy.ROSInterruptException: # if we ctrl+C to interrupt ROS
        pass
    except Exception as e:
        print(e)