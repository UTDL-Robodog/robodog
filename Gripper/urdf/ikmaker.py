import ikpy.chain
import numpy as np
import ikpy.utils.plot as plot_utils

my_chain = ikpy.chain.Chain.from_urdf_file("01-myfirst.URDF")
target_position = [50, 0, 0]
print("The angles of each joints are : ", my_chain.inverse_kinematics(target_position))
real_frame = my_chain.forward_kinematics(my_chain.inverse_kinematics(target_position))
print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], target_position))