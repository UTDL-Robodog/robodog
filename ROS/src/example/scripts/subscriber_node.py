#!/usr/bin/env
import rospy
from std_msgs.msg import String

def callback(data): # data is argument containing topic data
    rospy.loginfo("Received - " + str(data.data))

def subscriber():
 rospy.init_node("Subscriber_Node", anonymous=True) # initializes this node
 rospy.Subscriber("target_coordinates", String, callback) # initializes Subscriber object - (topic name, data type, callback function)
 rospy.spin() # runs node until ROS is shut down

if __name__=='__main__':
    try:
        subscriber()
    except rospy.ROSInterruptException: # if we ctrl+C to interrupt ROS
        pass
    except Exception as e:
        print(e)