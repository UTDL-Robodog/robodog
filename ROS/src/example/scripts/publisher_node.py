#!/usr/bin/env
import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('target_coordinates', String, queue_size=10) # initializes rospy publisher, first argument is the "topic" name, second is the datatype, and third is the queue size allowed to store
    rospy.init_node('publisher_node', anonymous=True) # initializes the node, first argument is the name of the node, second argument mean any nodes of the same name will get unique number
    rate = rospy.Rate(1) # rate at which the node will run (will be used later), 1 = 1Hz
    rospy.loginfo("Publisher Node Started") # rospy logging system
    while not rospy.is_shutdown(): # while ros node is running
        coords = "x = 1, y = 1" # message to be sent
        pub.publish(coords) # publish the message
        rate.sleep() # sleep for rest of cycle (1Hz in this case)

if __name__=='__main__':
    try:
        publisher()
    except rospy.ROSInterruptException: # if we ctrl+C to interrupt ROS
        pass
    except Exception as e:
        print(e)